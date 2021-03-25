from django.db import models
from django.urls import reverse
# Create your models here.


class Categoria(model.Model):
    nombre=models.CharField(max_length=200,db_index=True)
    slug=models.SlugField(max_length=200,unique=True)


    class Meta:
        ordering=('nombre',)
        verbose_name="Categoria"
        verbose_name_plural='Categorias'

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("tienda:lista_productos", args=[self.slug])

class Productos (model.Model):
    categoria=models.ForeignKey(Categoria,related_name='productos',on_delete=models.CASCADE  )
    
        
    
    