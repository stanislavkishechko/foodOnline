import os

from django.core.exceptions import ValidationError

def allow_only_images_validator(value):
    ext = os.path.splitext(value.name)[1]
    print(ext)
    valid_extensions = ['.jpg', '.jpeg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsuported file extension. Allowed extensions: ' + str(valid_extensions))