from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.nombre
    
class Gasto(models.Model):
    descripcion = models.CharField(max_length=200)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="gastos")
    fecha = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.descripcion} - ${self.monto}"


