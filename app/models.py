from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch  import receiver
from django.core.exceptions import ObjectDoesNotExist
import cloudinary
from cloudinary.models import CloudinaryField
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, default="avatar.svg")
    bio = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        db_table = 'profile'

    @receiver(post_save, sender=User)
    def update_create_profile(sender,instance,created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)

    def save_profile(self):
        self.save()

class TaxApplication(models.Model):
    client= models.OneToOneField(User, on_delete=models.CASCADE)
    TYPE = (('Renewal','Renewal',),('Appeal','Appeal'),('First Application','First Application'))
    application_type = models.CharField(max_length=50, choices=TYPE, null=True, blank=True)
    id_card = models.FileField(upload_to='doc/',null=True, blank=True)
    date_applied = models.DateTimeField(default=timezone.now())
    


