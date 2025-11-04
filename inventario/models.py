from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(
        upload_to='categorias/',
        help_text='Imagen representativa de la categoría'
    )
    activa = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.PROTECT,
        related_name='productos',
        help_text='Categoría a la que pertenece el producto'
    )
    precio = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        help_text='Precio del producto en dólares'
    )
    stock = models.PositiveIntegerField(
        default=0,
        help_text='Cantidad disponible del producto'
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - {self.marca}"
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['nombre']