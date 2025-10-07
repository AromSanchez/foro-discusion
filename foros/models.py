from django.db import models

# Create your models here.

class Tema(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='temas/', blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.titulo} by {self.autor}"


class Respuesta(models.Model):
    tema = models.ForeignKey(Tema, related_name='respuestas', on_delete=models.CASCADE)
    texto = models.TextField()
    autor = models.CharField(max_length=150)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Respuesta {self.pk} by {self.autor} on Tema {self.tema_id}"
