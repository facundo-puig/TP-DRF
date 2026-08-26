from django.db import models

class Gasto(models.Model):
    CATEGORIAS = [
        ('comida', 'Comida'),
        ('transporte', 'Transporte'),
        ('servicios', 'Servicios'),
        ('ropa', 'Ropa'),
        ('ocio', 'Ocio'),
        ('otro', 'Otro'),
    ]
    
    descripcion = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='otro')
    fecha = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.descripcion} - ${self.monto}"
