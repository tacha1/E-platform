from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
# Create your models here.

class service(models.Model):
    title = models.CharField(max_length =30)
    service_image = models.ImageField(upload_to = 'landing_images/', null=True)
    description = models.CharField(max_length =300)
    details = models.CharField(max_length =1000, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    @classmethod
    def get_all_services(cls):
        all_services = cls.objects.all()
        return all_services

    def save_services(self):
        self.save()

    def delete_services(self):
        self.delete()

    @classmethod
    def search_by_title(cls,search_term):
        certain_user = cls.objects.filter(title__icontains = search_term)
        return certain_user
        
    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to = 'profile_photos/', null=True)
    names = models.CharField(max_length =30, null=True)
    email = models.EmailField(max_length=50, null=True)
    phone = models.CharField(max_length=12, null=True)
    title = models.CharField(max_length =30, null=True) 
    summary = models.CharField(max_length =1000, null=True)
    services = models.ForeignKey(service,on_delete=models.CASCADE, null=True)
    more_info = models.CharField(max_length =300, null=True)

    @classmethod
    def get_profile(cls):
        all_profiles = cls.objects.all()
        return all_profiles

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete() 

    def __str__(self):
        return str(self.user)

class Comments(models.Model):
    comment = models.CharField(max_length = 250)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    posted_by = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True)
    commented_service = models.ForeignKey(service, on_delete=models.CASCADE, null = True)

    def save_comments(self):
        self.save()

    def delete_comments(self):
        self.delete()

    def __str__(self):
        return self.posted_by

class Rating(models.Model):
    design = models.PositiveIntegerField(default = 0,validators = [MaxValueValidator(10)])
    usability = models.PositiveIntegerField(default = 0,validators = [MaxValueValidator(10)])
    content = models.PositiveIntegerField(default = 0,validators = [MaxValueValidator(10)])
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    service = models.IntegerField(default = 0)