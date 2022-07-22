from django.contrib import admin
from .models import(
    User, 
    # Student,
    SchoolPin,
    SchoolProfile,
    Year,
    Course,
    Teacher,
    CourseMaterial,
    Programme,
    Transactions,
    Document
    # StudentWallet


) 

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'password', 'slug')


# class StudentProfileAdmin(admin.ModelAdmin):
#     list_display = ('user','first_name', 'last_name', 'gender', 'phone_number')


admin.site.register(User, UserAdmin)

# admin.site.register(Student, StudentProfileAdmin)
admin.site.register(SchoolPin)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Year)
admin.site.register(SchoolProfile)
admin.site.register(CourseMaterial)
admin.site.register(Programme)
admin.site.register(Transactions)
admin.site.register(Document)
