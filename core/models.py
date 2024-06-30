from django.db import models
from django.utils.text import slugify
# Create your models here.
from django.db import models
from django.utils.text import slugify

class movie(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True)
    tag1 = models.CharField(max_length=500, null=True, blank=True)
    tag2 = models.CharField(max_length=500, null=True, blank=True)
    tag3 = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    trailer = models.CharField(max_length=5000, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_related_movies(self):
        return movie.objects.filter(tag1=self.tag1).exclude(id=self.id)

class Favorite(models.Model):
    session_id = models.CharField(max_length=32)
    movie = models.ForeignKey(movie, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('session_id', 'movie')

    
class cast(models.Model):
    movie = models.ForeignKey('movie', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cast/')
    def __str__(self):
        return self.name
    

# class Favorite(models.Model):
#     session_id = models.CharField(max_length=32)
#     movie = models.ForeignKey(movie, on_delete=models.CASCADE)
#     added = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         unique_together = ('session_id', 'movie')