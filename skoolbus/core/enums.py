from django.db.models import TextChoices


class Gender(TextChoices):
    MALE = 'MALE'
    FEMALE = 'FEMALE'

class Course(TextChoices):
    CHEMICAL_ENGINEERING = 'CHEMICAL ENGINEERING'
    MECHANICAL_ENGINEERING = 'MECHANICAL ENGINEERING'
    FOOD_ENGINEERING = 'FOOD ENGINEERING'


class TransactionType(TextChoices):
    FUNDING = 'FUNDING'
    PAYMENT = 'PAYMENT'

class TransactionStatus(TextChoices):
    SUCCESS = 'SUCCESSS'
    FAILED = 'FAILED'
    PENDING = 'PENDING'