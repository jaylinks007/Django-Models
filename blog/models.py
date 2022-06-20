from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Published")
)

class Post(models.Model):
    title=models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now= True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title