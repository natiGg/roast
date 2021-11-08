import uuid
from django.db import models
from authentication.models import User
# Create your models here

class Level(models.Model):

    LEVEL_CHOICES = (
        ('comedian', 'comedian'),
        ('pro', 'pro'),
        ('amatuer', 'amatuer'),
        ('roaster', 'roaster'),
        ('spectator', 'spectator'),
    )
    type = models.CharField(max_length=50, choices=LEVEL_CHOICES,default=LEVEL_CHOICES[4][0])
    def __str__(self):
        return u"%s" % (self.type)   

class Reaction(models.Model):
    
    REACTION_CHOICES = (
        ('haha', 'Funny'),
        ('ohhh', 'amazed'),
        ('nahh', 'Not Funny'),

    )
    reaction = models.CharField(max_length=50, choices=REACTION_CHOICES)

class Roast(models.Model):
   
    id = models.IntegerField(primary_key=True,unique=True,blank=False)
    STAGE_CHOICES = (
        ('special', 'special'),
        ('Far', 'Far'),
        ('Very close', 'close'),
        ('to be roasted', 'tobe'),
    )  
    stage = models.CharField(max_length=50, choices=STAGE_CHOICES)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    is_special=models.BooleanField(default=False)

 
class UserProfile(models.Model):

    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50,unique=False)
    last_name = models.CharField(max_length=10, unique=False)
    phone_number = models.CharField(max_length=50, unique=True, null=False, blank=False)
    profile_pic = models.ImageField(null=True,blank=True,upload_to="media/profiles/")
    age = models.PositiveIntegerField(null=False, blank=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    level = models.ForeignKey(Level,on_delete=models.CASCADE,related_name='level')
    bio = models.CharField(max_length=250,unique=False)
    class Meta:
        '''
        to set table name in database
        '''
        db_table = "profile"

class Comment(models.Model):
    id = models.IntegerField(primary_key=True,unique=True,blank=False)
    commenter = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    comment = models.TextField(blank=False)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    reaction = models.ForeignKey(Reaction,on_delete=models.CASCADE,related_name='commentreact')
   
class Joke(models.Model):

    id = models.IntegerField(primary_key=True,unique=True,blank=False)
    caption = models.TextField(blank=False)
    photo = models.ImageField(blank=True,upload_to='media/jokes_photo/')
    reaction = models.ForeignKey(Reaction,on_delete=models.CASCADE,related_name="reacted")  
    date_posted = models.DateField(auto_now_add=True)
    time_posted = models.TimeField(auto_now_add=True)
    posted_by = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    stage = models.OneToOneField(Roast,on_delete=models.CASCADE)
