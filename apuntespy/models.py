from django.db import models
from django.urls import reverse
from .validations.validators import tag_unico, tip_unico

# Create your models here.
class Tag(models.Model):
    tag_text = models.CharField(max_length=200, validators=[tag_unico])
    def  __str__(self):
        return self.tag_text

    def get_absolute_url(self):
        return reverse('apuntespy:tag_list')



class Tip(models.Model):
    tags = models.ManyToManyField(Tag, related_name="tips")
    tip_nombre = models.CharField(max_length=200, validators=[tip_unico])
    tip_descripcion = models.TextField()
    tip_ejemplo = models.TextField()

    def get_absolute_url(self):
        return reverse('apuntespy:results', kwargs={'pk': self.pk})
    def  __str__(self):
        return self.tip_nombre