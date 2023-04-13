from django.contrib.auth.models import User

from django.db import models


# Create your models here.

class Hackathon(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    background_image = models.ImageField(upload_to='static/hackathons/background_images/')
    hackathon_image = models.ImageField(upload_to='static/hackathons/hackathon_images/')
    TYPE_CHOICES = [('image', 'Image'), ('file', 'File'), ('link', 'Link')]
    submission_type = models.CharField(max_length=5, choices=TYPE_CHOICES)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    reward_prize = models.DecimalField(max_digits=10, decimal_places=2)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hackathon', blank=True, null=True)

    def __str__(self):
        return self.title
    
class Submission(models.Model):
    name = models.CharField(max_length=200)
    summary = models.TextField()
    TYPE_CHOICES = [('image', 'Image'), ('file', 'File'), ('link', 'Link')]
    submission_type = models.CharField(max_length=5, choices=TYPE_CHOICES)
    image_submission = models.ImageField(upload_to='submissions/images/', null=True, blank=True)
    file_submission = models.FileField(upload_to='submissions/files/', null=True, blank=True)
    link_submission = models.URLField(null=True, blank=True)
    hackathon = models.ManyToManyField(Hackathon, related_name='submissions')

    def __str__(self):
        return self.name


