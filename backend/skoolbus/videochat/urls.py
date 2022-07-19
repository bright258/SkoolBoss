from django.urls import path
from .views import (
    room,
    lobby,
    getToken,
    createMember,
    getMember
    )
app_name = 'videochat'

urlpatterns = [ 

    path('vid/', room ),
    path('', lobby),
    path('get_token/', getToken),
    path('create_member/', createMember),
    path('get_member/', getMember)



]