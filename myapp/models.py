from django.db import models

# Create your models here.






class Post(models.Model):
    
    
    
    image= models.ImageField( upload_to='static')
    body = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering= ('-created_at',)
    
    def __str__(self):
        return self.body

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    



