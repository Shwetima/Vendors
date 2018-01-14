from django.core.validators import RegexValidator


alphaSpaces = RegexValidator(r'^[a-zA-Z ]+$','Only letters and spaces are allowed')
Numerics = RegexValidator(r'\+?\d[\d -]{8,12}\d','Please enter valid contact number')
decimals= RegexValidator(r'^[1-9]\d*(\.\d+)?$', 'Only numers and floating numbers allowed')
no=RegexValidator(r'^[0-9]*$','enter valid number')
alphanumeric = RegexValidator(r'^[0-9a-zA-Z ]*$', 'Only alphanumeric characters are allowed.')
Number=RegexValidator(r'^[0-9]\d*(\.\d+)?$','Please Enter only Number')
