from django.db import models

# Create your models here.
class Blog(models.Model):
  title = models.CharField(max_length= 100)
  writer = models.CharField(max_length= 10)
  body = models.TextField()
  pub_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title