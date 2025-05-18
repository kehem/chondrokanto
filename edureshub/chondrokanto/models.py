from django.db import models

# Create your models here.
class info(models.Model):
    banner_title = models.CharField(max_length=100)
    banner_sub_title = models.CharField(max_length=100)
    banner_image = models.ImageField(upload_to='banner/')
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    facebook = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    instagram = models.CharField(max_length=100)
    youtube = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    slogan = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    

class category(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    description = models.TextField()
    banner = models.ImageField(upload_to='category/')
    icon = models.ImageField(upload_to='category/')
    
    def __str__(self):
        return self.title



class album(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='album/')
    category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class video(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='video/')
    video_link = models.CharField(max_length=300)
    album = models.ForeignKey(album, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    hide = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
class blog(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog/')
    content = models.TextField()
    category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title