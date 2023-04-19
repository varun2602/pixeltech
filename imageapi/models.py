from django.db import models


# Create your models here.
class UserResponse(models.Model):
    user_name = models.CharField(max_length = 100, blank = True, null = True)
    user_response = models.CharField(max_length = 100, blank = True, null = True, default = 'timeout')
    response_image = models.CharField(max_length = 100, null = True, blank = True, default = '')

    def __str__(self):
        return f"{self.user_response} {self.response_image}"
