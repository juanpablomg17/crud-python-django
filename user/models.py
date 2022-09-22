from django.db import models  
class User(models.Model):  
    eid = models.CharField(primary_key=True, max_length=20)
    ename = models.CharField(max_length=100)  
    elastname = models.CharField(max_length=100)  
    eage = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    frecuencia_cardiaca = models.CharField(max_length=100)
    saturacion_oxigeno = models.CharField(max_length=100)
    nivel_stress = models.CharField(max_length=100)

    class Meta:  
        db_table = "user"  