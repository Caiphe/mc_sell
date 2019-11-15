from django.db import models
from django.contrib.auth.models import User
from PIL import Image

''' This is the model to create a users profile  '''


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.png", upload_to="profile_pics")

    def __str__(self):
        return f'{ self.user.username } Profile'

    ''' Here I'm overridng the save method of the profile image,
    and resizing the images if it is greater the 300 in height and width
    To avoid having huge images in our system
    '''

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 330 or img.width > 330:
            output_size = (330, 330)
            img.thumbnail(output_size)
            img.save(self.image.path)
