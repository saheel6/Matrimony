from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError




# Create your models here.
class Religion(models.Model):
    religion=models.CharField(max_length=50)
    
    def __str__(self):
        return self.religion
    
class Community(models.Model):
    community=models.CharField(max_length=100)
    
    def __str__(self):
        return self.community
    
class Livingcoutry(models.Model):
    livingcountry=models.CharField(max_length=100)
    
    def __str__(self):
        return self.livingcountry
    
    
class Gender(models.Model):
      gender=models.CharField(max_length=50,default="m or f")
      
      def __str__(self):
          return self.gender
      
class Livewithfamily(models.Model):
    Live=models.CharField(max_length=10)
    
    def __str__(self):
        return self.Live
    
class Maritalstatus(models.Model):
    status=models.CharField(max_length=50)
    
     
    def __str__(self):
        return self.status
    
    
class Diet(models.Model):
    diets = models.CharField(max_length=100)
    
     
    def __str__(self):
        return self.diets
    
    
class Height(models.Model):
    height = models.IntegerField()
    
     
    def __str__(self):
        return str(self.height)
    
      


class CustomUser(AbstractUser):
    # Add your custom fields here
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.IntegerField(default=0)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, null=True, blank=True)
    living_country = models.ForeignKey(Livingcoutry, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE, null=True, blank=True)
    livewithfamily = models.ForeignKey(Livewithfamily, on_delete=models.CASCADE,null=True, blank=True)
    maritalstatus = models.ForeignKey(Maritalstatus, on_delete=models.CASCADE,null=True, blank=True)
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE,null=True, blank=True)
    height = models.ForeignKey(Height, on_delete=models.CASCADE,null=True, blank=True)
    city = models.CharField(max_length=100,null=True)
    age = models.IntegerField(default=18)
    qualification = models.CharField(max_length=100,null=True)
    job = models.CharField(max_length=100,null=True)
    selfdescription = models.CharField(max_length=1000,null=True,verbose_name='self description')
    photo = models.ImageField(upload_to="userphotos",null=True, blank=True)
    likes = models.ManyToManyField('self', through='Like', symmetrical=False)
    is_subscribed = models.BooleanField(default=False)
    
    
    @property
    def gender_name(self):
      return self.gender.name


    
    
    
class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    liked_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='liked_by')

    
    
class Chat(models.Model):
  sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sender')
  recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='recipient') 
  message = models.CharField(max_length=500)
  created_at = models.DateTimeField(auto_now_add=True)
  
  
  
  def save(self, *args, **kwargs):
    sender_subscribed = self.sender.is_subscribed 
    recipient_subscribed = self.recipient.is_subscribed
    
    if sender_subscribed and recipient_subscribed:
      super().save(*args, **kwargs) 
    else:
      raise ValidationError("Both users must be subscribed to chat")
    
    
    
class Subscription(models.Model):
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  subscription_type = models.CharField(max_length=20)
  start_date = models.DateTimeField(auto_now_add=True) 
  end_date = models.DateTimeField()
  card_number = models.CharField(max_length=16)
  
  
  
class Preference(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    preferred_gender = models.ForeignKey(Gender,on_delete=models.CASCADE, null=True, blank=True)
    preferred_religion = models.ForeignKey(Religion, on_delete=models.CASCADE, null=True, blank=True)
    preferred_community = models.ForeignKey(Community, on_delete=models.CASCADE, null=True, blank=True)
    preferred_maritalstatus = models.ForeignKey(Maritalstatus, on_delete=models.CASCADE,null=True, blank=True)
    min_height = models.IntegerField(null=True)
    max_height = models.IntegerField(null=True)
    min_age=models.IntegerField(null=True)
    max_age=models.IntegerField(null=True)

  
  
  
  
  

    
# class profile(models.Model):
    

    
    
    
    
    
    
    
    