from django.http import JsonResponse
from django.shortcuts import render
import random
import time
import json
from agora_token_builder import RtcTokenBuilder
from django.views.decorators.csrf import csrf_exempt
from .models import RoomMember





def lobby(request):
    return render(request, 'videochat/lobby.html')


def room(request):
    return render(request, 'videochat/room.html')


def getToken(request):
    appId = "a843c82c381c4634815f6304ec46504d"
    appCertificate = "130c9021819d45c79c447f626786ee08"
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token': token, 'uid': uid}, safe=False)



@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(

        name = data['name'],
        uid = data['UID'],
        room_name = data['room_name']
    )
    return JsonResponse({'name':data['name']}, safe = False)


def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid = uid,
        room_name = room_name
    )
    name = member.name
    return JsonResponse({'name':name}, safe = False)

def deleteMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(

        uid = uid,
        room_name = room_name
    )
    member.delete()

    return JsonResponse({'member_deleted'}, safe = False)

