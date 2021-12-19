from django.db import models


# Create your models here.

class MyForm(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name', blank=True)
    comm = models.CharField(max_length=150, verbose_name='Communication', blank=True)
    mess = models.TextField(verbose_name='Message', blank=True)
    data = models.TimeField(auto_now_add=True)
    colled = models.BooleanField(verbose_name='Coll status', blank=True)
    my_comment = models.TextField(verbose_name='My comment', blank=True)

    def __str__(self):
        return str(self.name) + ' - ' + str(self.data)


