from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
from .managers import CustomUserManager
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.conf import settings
from .enums import (
    Gender,
    Course,
    TransactionType,
    TransactionStatus
) 



class User(AbstractUser):
    email = models.EmailField(_('email'),unique = True)
    slug = models.SlugField()
    
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD: str = 'email'

    objects = CustomUserManager()
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)
        return super(User, self).save(*args, **kwargs)


class Base(models.Model):
    created_at = models.DateTimeField(auto_now= True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True


class Programme(Base):
    name = models.CharField(max_length = 200, choices = Course.choices)


class Year(Base):
    
    year = models.IntegerField(default= 1)


class CourseMaterial(Base):
    name = models.CharField(max_length = 200, null = True)
    course_material = models.FileField(upload_to = 'then')



class Course(Base):
    name = models.CharField(max_length = 200, choices = Course.choices)
    credit_hours = models.CharField(max_length = 300)
    course_code = models.CharField(max_length = 200)
    estimated_course_hours = models.CharField(max_length= 200)
    course_timetable = models.ImageField(upload_to = 'then')
    current_year = models.ForeignKey(Year, on_delete= models.CASCADE, related_name= 'currentyear')
    course_outline = models.FileField(upload_to= 'pdfs')
    programme = models.ForeignKey(Programme, on_delete= models.CASCADE, blank = True, null = True)
    materials = models.ManyToManyField(CourseMaterial, null = True)

class Teacher(Base):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name= 'teacher', null = True )
    first_name = models.CharField(max_length= 200, null =True)
    last_name = models.CharField(max_length = 200, null = True)
    profile = models.TextField(max_length = 3000, null = True)
    course = models.ManyToManyField(Course)
    salary = models.DecimalField(max_digits= 10, decimal_places= 2, null = True)
    school = models.CharField(max_length = 200, null = True)
    gender = models.CharField(_('gender'), default = Gender.MALE, choices = Gender.choices,max_length = 200, null = True, blank = True)
    phone_number = models.CharField(_('phonenumber'), max_length = 200, null = True, blank = True)
    programme = models.ForeignKey(Programme, on_delete= models.CASCADE, null = True, blank = True)
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    image = models.ImageField(upload_to ='then', null = True)
    duration = models.IntegerField(default = 3, null = True)







class SchoolProfile(Base):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name= 'school', null = True)
    name_of_school = models.CharField(max_length = 300, blank = True)
    first_name = models.CharField(_('firstname'),max_length = 200, null = True, blank = True)
    last_name = models.CharField(_('lastname'),max_length = 200, null = True, blank = True)
    gender = models.CharField(_('gender'), default = Gender.MALE, choices = Gender.choices,max_length = 200, null = True, blank = True)
    phone_number = models.CharField(_('phonenumber'), max_length = 200, null = True, blank = True)
    programme = models.ForeignKey(Programme, on_delete= models.CASCADE, null = True, blank = True)
    duration = models.IntegerField(default = 3, null = True)
    start_date = models.DateField(null = True)
    end_date = models.DateField(null = True)
    school_bio = models.TextField(max_length = 3000, blank = True)
    schools_map = models.FileField(upload_to = 'then', blank = True, null = True)
    school_fees = models.DecimalField(max_digits = 11, decimal_places= 2, null = True, blank = True)
    wallet = models.DecimalField(max_digits = 11, decimal_places = 2, null = True)
    currency = models.CharField(max_length = 50, default = 'NGN', null = True)
    recipient_code = models.CharField(max_length = 200, null = True)
    year = models.ForeignKey(Year, on_delete= models.CASCADE, related_name= 'year_of_study', null = True, blank = True)
    course = models.ManyToManyField(Course, null = True, blank = True)
    image = models.ImageField(upload_to ='then', null = True)
    
    def checkpin(self, pin):
        l = SchoolPin.objects.select_related('user').get(user = self.user).showpin()
        print(self.name_of_school)
        print(l)


class Transactions(Base):
    user = models.ForeignKey(SchoolProfile, on_delete= models.CASCADE, related_name = 'transact', null = True )
    amount = models.DecimalField(max_digits= 11, decimal_places= 2, null = True)
    narration = models.CharField(max_length = 200)
    transaction_type = models.CharField(max_length = 200, choices = TransactionType.choices)
    transaction_status = models.CharField(max_length  = 200, choices = TransactionStatus.choices, default = TransactionStatus.SUCCESS)
    paystack_reference = models.CharField(max_length = 200, blank = True, null = True)
    destination = models.IntegerField(blank = True, null = True)


   
class SchoolPin(Base):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name = 'user')
    pin = models.CharField(_('pin'),max_length = 100)
    
    
    def showpin(self):
        return self.pin


    
 
