const APP_ID = "a843c82c381c4634815f6304ec46504d"
const TOKEN = sessionStorage.getItem('token')
const CHANNEL = sessionStorage.getItem('room')
let UID = sessionStorage.getItem('UID')
let NAME = sessionStorage.getItem('name')

const client = AgoraRTC.createClient({mode :'rtc', codec:'vp8'})

let localTracks = []
let remoteUsers = {}

let joinAndDisplayLocalStream = async()=>{
    document.getElementById('room-name').innerText = CHANNEL

    client.on('user-published', handleUserJoined)
    client.on('user-left, handleUserLeft')

    try{
        UID = await client.join(APP_ID, CHANNEL, TOKEN, UID)
    }catch(error){
        console.log(error)
        window.open('/','_self')
    }

    localTracks = await AgoraRTC.createMicrophoneAndCameraTracks()

    let member = await createMember()

    let player = `<div  class="video-container" id="user-container-${UID}">
    <div class="video-player" id="user-${UID}"></div>
    <div class="username-wrapper"><span class="user-name">${member.name}</span></div>
 </div>
        `
    document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)
    localTracks[1].play(`user-${UID}`)
    await client.publish([localTracks[0], localTracks[1]])
}

let getMember = async(user) =>{

    let response = await fetch(`/get_member/?UID= ${user.uid}&room_name = ${CHANNEL}`)
    let member = await response.json()
    return member
}



let handleUserJoined = async(user, mediaType)=>{

    remoteUsers[user.uid] = user
    await client.subscribe(user, mediaType)

    if (mediaType === 'video'){

        let player = document.getElementById(`user-container-${user.id}`)
        if (player != null ){

            player.remove()

        }

        let member = await getMember(user)
        player = `
        <div  class="video-container" id="user-container-${user.uid}">
            <div class="video-player" id="user-${user.uid}"></div>
            <div class="username-wrapper"><span class="user-name">${member.name}</span></div>
        </div>
        
        `
        document.getElementById('video-streams').insertAdjacentHTML('beforeend',player) 
        user.videoTrack.play(`user-${user.uid}`)

    }

    if (mediaType === 'audio'){
        user.audioTrack.play()
    }
}


let handleUserLeft = async(user)=>{
    delete remoteUsers[user.uid]
    document.getElementById(`user-container-${user.uid}`).remove()


}


let deleteMember = async ()=>{

    let response = await fetch('/delete_member/',
    
    {
        method:'POST',
        headers:{
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'name':NAME, 'room_name':CHANNEL, 'UID':UID})
        
    })
    let member = await response.json()
}


let leaveAndRemoveLocalStream = async() =>{

    for (let i = 0; localTracks.length > i; i++){

        localTracks[i].stop()
        localTracks[i].close

        await client.leave()
        deleteMember()
        window.open('/', '_self')
    }
}

let toggleCamera = async(e) =>{

    console.log('TOGGLE CAMERA TRIGGERED')
    if (localTracks[1].muted){
        await localTracks[1].setMuted(false)
        e.target.style.backgroundColor = 'fff'

    }else{
        await localTracks[1].setMuted(true)
        e.target.style.backgroundColor = 'rgb(255, 80, 80, 1)'
    }
}


let toggleMic = async(e)=>{

    console.log('TOGGLE MIC TRIGGERD')
    if (localTracks[0].muted){
        await localTracks[0].setMuted(false)
        e.target.style.backgroundColor = 'rgb(255, 80, 80,80,1)'
    }else{

        await localTracks[0].setMuted(true)
        e.target.style.backgroundColor = 'rgb(255, 80, 80, 1)'
    }
}


let createMember = async()=>{
    let response = await fetch(
        '/create_member/',
        {headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'name': NAME, 'room_name':CHANNEL, 'UID': UID,})
        })
    let member = await response.json()
    return member
}

window.addEventListener('beforeunload', deleteMember)

joinAndDisplayLocalStream()

document.getElementById('leave-btn').addEventListener('click', leaveAndRemoveLocalStream)
document.getElementById('camera-btn').addEventListener('click', toggleCamera)
document.getElementById('mic-btn').addEventListener('click', toggleMic)