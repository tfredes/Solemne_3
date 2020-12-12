from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    publishedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    image = models.ImageField(upload_to = 'uploads/', default='uploads/default.jpg')

    def __str__(self):
        return self.title
        
    def addComment(self):
        self.comments = self.comments + 1
        return self
    
    def addCountComment(self, count):
        self.comments = self.comments + count
        return self