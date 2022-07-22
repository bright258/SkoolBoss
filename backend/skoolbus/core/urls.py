from django.urls import path
from .views import (
    Register,
    Login,
    PinView,
    SchoolProfileView,
    CourseView,
    CourseMaterialView,
    GetProfileView,
    GetTeacherView,
    UpdateProfileView,
    DepositFundsView,
    TransactionView,
    PayFeesView,
    PaystackWebhookView,
    TeacherView,
    UpdateTeacherView,
    DocumentView
   
    

)

urlpatterns =[ 
    path('register/',Register.as_view()),
    path('login/',Login.as_view() ),
    path('pin/', PinView.as_view()),
    path('create/schoolprofile/', SchoolProfileView.as_view()),
    path('course/', CourseView.as_view()),
    path('materials/', CourseMaterialView.as_view()),
    path('profile/get/<int:pk>', GetProfileView.as_view()),
    path('update/profile/<int:pk>', UpdateProfileView.as_view()),
    path('funding/', DepositFundsView.as_view()),
    path('transactions/<int:pk>', TransactionView.as_view()),
    path('payfees/<int:pk>', PayFeesView.as_view()),
      path(
        "payment/paystack/webhook/",
        PaystackWebhookView.as_view(),
        name="paystack-webhook",
    ),
    path('teacher/profile/<int:pk>',GetTeacherView.as_view()),
    path('teacher/profile/create/', TeacherView.as_view()),
    path('teacher/update/<int:pk>/', UpdateTeacherView.as_view()),
    path('document/', DocumentView.as_view())
] 