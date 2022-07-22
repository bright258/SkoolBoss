from django import views
from rest_framework import serializers

from .enums import TransactionStatus, TransactionType
from .models import (
    Teacher,
    User, 
    SchoolPin,
    SchoolProfile,
    Course,
    CourseMaterial,
    Programme,
    Transactions,
    Document
    
    )
from rest_framework.authtoken.models import Token
from .utils  import (
    check_list, 
    uniuyo_list, 
    unical_list, 
    uniuyo_details, 
    unical_details,  
    get_balance,
    uniuyo_teachers_list,
    unical_teachers_list
)
from .services import paystack

class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = [ 'email', 'password', 'username', 'id']

    def create(self, validated_data):
        user = User(
            email=validated_data["email"], username=validated_data["username"]
        )
        user.set_password(validated_data["password"])
        user.save()
        Token.objects.create(user=user)
        return user


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = [ 
            'programme',
            'duration',
            'start_date',
            'end_date',
            
            'first_name',
            'last_name',
            'gender',
            'phone_number',
            'image'
            



        ]
        extra__kwargs = {
            'school':{'read_only':'True'},
            'salary':{'read_only':'True'},
            'schools_map':{'read_only':'True'},
            'school_bio':{'read_only':'True'}

        }   


    def create(self, validated_data):
        user = self.context['request'].user
        profile = Teacher.objects.create(user = user, **validated_data)
        profile.save
        return profile

class SchoolPinSerializer(serializers.Serializer):
    pin = serializers.CharField(max_length = 200, validators = [check_list])
    id = serializers.ReadOnlyField()

    class Meta:
        model = SchoolPin
        fields = [ 'pin']
    


    def create(self, validated_data,*args, **kwargs):
        user = self.context['request'].user
        pin = SchoolPin.objects.create(user = user, **validated_data)
        print(pin.user)

        
        pin.save()
        return pin

    def save(self, **kwargs):
        # user = User.objects.get(pk = 19 )
        user = self.context['request'].user
        
        pin = self.validated_data['pin']
        
            
        payload = { 
            'type':'nuban',
            'name':'Bright Bassey',
            'account_number': 3140249243,
            'bank_code':"011"

        }
        recipient_code = paystack.create_transfer_recipient(payload)
            
        if pin in uniuyo_list:
            SchoolProfile.objects.create(
            user = user, 
            name_of_school = 'Uniuyo', 
            schools_map = 'then/images_2.jpeg', 
            school_bio = uniuyo_details['rating'],
            recipient_code = recipient_code,
            school_fees = '6000')
        
        elif pin in unical_list:
            
            
            SchoolProfile.objects.create(user =user, 
            name_of_school = "Unical", 
            schools_map = 'then/images(3).jpeg', 
            school_bio = unical_details['rating'],
            recipient_code = recipient_code, 
            school_fees = '5000')
        
        elif pin in uniuyo_teachers_list:
            Teacher.objects.create(
                user = user,
                salary = '7000',
                school = 'Uniuyo'
             

            )

        elif pin in unical_teachers_list:
            Teacher.objects.create(
            user = user,
            school = 'Unical',
            salary = '8000'

            
            
            )
        else:
            pass
        print(pin)
        
        return super().save(**kwargs)

    

class SchoolProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    image_url = serializers.ReadOnlyField()
    # documents = serializers.Hyperlink(url = image_url, obj = image_url)


    class Meta:
        model = SchoolProfile
        fields = [ 
            'id',
            'name_of_school',
            'programme',
            'duration',
            'start_date',
            'end_date',
            'school_bio',
            'schools_map',
            'school_fees',
            'wallet',
            'first_name',
            'last_name',
            'gender',
            'phone_number',
            'documents',
            'image',
            'image_url'
            


        ]
        extra_kwargs = {
            'name_of_school':{'read_only':'True'},
            'school_bio': {'read_only': 'True'},
            'school_fees': {'read_only': 'True'},
            'schools_map': {'read_only' : 'True'},
            'recipient_code': {'read_only': 'True'},
            'wallet': {'read_only':'True'}


        
        
        }

    def create(self, validated_data):
        user = self.context['request'].user
        p = SchoolProfile.objects.create(user = user, **validated_data) 
       
        p.save()
        print(user)
        

        return p

    def update(self, instance, validated_data):
        # instance.duration = validated_data['duration']
        

        instance.save()
        profile = SchoolProfile.objects.update(**validated_data)

        return  profile

    

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):

        user = self.context['request'].user
        p = Course.objects.create(user = user, **validated_data)
        p.save()
        return p

class CourseMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseMaterial
        fields = '__all__'

    
    def create(self, validated_data):
        user = self.context['request'].user
        p = CourseMaterial.objects.create(user = user, **validated_data )
        p.save()
        return p
      
    
class DepositFunds(serializers.ModelSerializer):
    amount = serializers.IntegerField()
    email = serializers.EmailField()
    narration = serializers.CharField()

    class Meta:
        model = Transactions
        fields = ['amount', 'email', 'transaction_type', 'narration']
       

    def save(self, **kwargs):
        user = self.context['request'].user
        tran = SchoolProfile.objects.select_related('user').get(user = user)
        wallet = tran.wallet
       
        validated_data = self.validated_data
        # print(bal)

        payload = { 
            'amount': validated_data['amount'],
            'email': validated_data['email'],
            'currency': 'NGN'
        }
        ref = paystack.initialize_transaction(payload)
        print(ref)

        Transactions.objects.create(
            user = tran,
            amount = validated_data['amount'],
            narration = validated_data['narration'],
            transaction_type = TransactionType.FUNDING,
            paystack_reference = ref

        )
        wallet = SchoolProfile.objects.get(user = user).wallet
        SchoolProfile.objects.select_related('user').update(wallet = wallet + validated_data['amount'])


        return ref

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'


class PayFeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ['amount',
         'narration']

    def save(self, **kwargs):

        user = self.context['request'].user
        payer = SchoolProfile.objects.select_related('user').get(user = user)
        wallet = payer.wallet
        
        
        validated_data = self.validated_data
        recipient_code = payer.recipient_code

        # if bal < validated_data['amount']:
        #     raise serializers.ValidationError({'detail': 'insufficient_funds'})
        
        

        payload = {

            'source':'balance',
            'amount': validated_data['amount'],
            'recipient_code': recipient_code,
            'currency':'NGN'
        }
        rel = paystack.initialize_transfer(payload)
        print(rel)

        Transactions.objects.create(
            transaction_type = TransactionType.PAYMENT,
            **validated_data


        )
        # wallet2 = SchoolProfile.objects.get(user = user).wallet
        SchoolProfile.objects.select_related('user').update(wallet = wallet - validated_data['amount'])

        return payer
        

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = [  
            'file',
            'name',
            'image_url'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('file')
        representation.pop('name')
        return representation