from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):              
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):             
        return self.choice_text

class Comment(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)   
    comment = models.CharField(max_length=300)

    def __str__(self):           
        return self.user, self.comment, self.question    

class Post_Comment(models.Model):
    user = models.ForeignKey(User)
    question = models.ForeignKey(Question)   
    new_comment = models.CharField(max_length=300)

    def __str__(self):             
        return self.user, self.comment, self.question

class File_Upload(models.Model):    
    upload_file = models.FileField(upload_to='upload_files')
   