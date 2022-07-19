import json
from codecs import lookup
from django.forms import ValidationError
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import (
    
    CreateAPIView, 
    RetrieveAPIView,
    UpdateAPIView,
    ListAPIView
)
from .tasks import handle_webhook
from .serializers import ( 
    
    SchoolPinSerializer,
    TeacherSerializer,
    UserSerializer,
    # ProfileSerializer,
    SchoolProfileSerializer,
    CourseSerializer,
    CourseMaterialSerializer,
    DepositFunds,
    TransactionSerializer,
    PayFeesSerializer,
    
   
 )

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import (
    # StudentWallet,
    Transactions,
    User,
    #  Student,
     SchoolPin,
     SchoolProfile,
     Course,
     CourseMaterial,
     Teacher
     
     )
from django.contrib.auth import authenticate
from rest_framework.response import Response

class Register(CreateAPIView):
    permission_classes = [ 
        AllowAny
    ]
    serializer_class = UserSerializer
    queryset = User

    

# class ProfileView(CreateAPIView):
#     permission_classes = [ 
#         AllowAny
#     ] 
#     serializer_class = ProfileSerializer
#     queryset = Student


class Login(APIView):

    
    permission_classes= [ 
        AllowAny
    ]


    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user_data = User.objects.get(email = email)
        user = authenticate(email = email, password = password)
        if user:
            return Response({

                'token':user.auth_token.key,
                'email' : email,
                'id' : user_data.id,
                'username': user_data.username



            })
        else:
            return Response({'error':'you are not registered'})



    
class PinView(CreateAPIView):
    permission_classes = [ 
        AllowAny
    ]
    serializer_class = SchoolPinSerializer
    queryset = SchoolPin


class SchoolProfileView(CreateAPIView):
    permission_classes = [ 
        AllowAny
    ]
    serializer_class = SchoolProfileSerializer
    queryset = SchoolProfile.objects.all()

class CourseView(CreateAPIView):

    permission_classes =  [ 
        AllowAny
    ]
    serializer_class = CourseSerializer
    queryset = Course

class CourseMaterialView(CreateAPIView):
    permission_classes = [ 
        AllowAny
        
    ]
    serializer_class = CourseMaterialSerializer
    queryset = CourseMaterial

class GetProfileView(RetrieveAPIView):
   permission_classes = [ 
       IsAuthenticated
   ]
   serializer_class = SchoolProfileSerializer
   queryset = SchoolProfile.objects.all()

class UpdateProfileView(UpdateAPIView):
    permission_classes = [ 
        IsAuthenticated
    ]
    serializer_class = SchoolProfileSerializer
    queryset = SchoolProfile.objects.all()

class DepositFundsView(CreateAPIView):
    permission_classes = [ 
        IsAuthenticated
    ]
    serializer_class = DepositFunds
    queryset = Transactions.objects.all()

class GetTeacherView(RetrieveAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [ 
        AllowAny
    ]
    queryset = Teacher.objects.all()

class TeacherView(CreateAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [ 
        IsAuthenticated
    ]
    queryset = Teacher.objects.all()

class TransactionView(RetrieveAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [ 
        AllowAny
    ]
    queryset = Transactions.objects.all()

    

class PayFeesView(CreateAPIView):
    permission_classes = [ 
        AllowAny
    ]
    serializer_class = PayFeesSerializer
    queryset = Transactions.objects.all()


class PaystackWebhookView(APIView):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body.decode("utf-8"))

        handle_webhook(data)

        return Response(data={})
