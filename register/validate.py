
from django.core.validators import RegexValidator


alphaSpaces = RegexValidator(r'^[a-zA-Z ]+$','Only letters and spaces are allowed')
Numerics = RegexValidator(r'\+?\d[\d -]{8,12}\d','Please enter valid contact number')
pinnumber=RegexValidator(r'^[0-9]{6}$','enter valid pin')