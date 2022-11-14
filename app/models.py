from django.db import models


class overspeed(models.Model):
    oid = models.IntegerField()
    Create_Date = models.CharField(max_length=200)
    Plat_Nomor = models.CharField(max_length=200)
    Speed = models.CharField(max_length=200)
    foto = models.CharField(max_length=200)
    id_speed= models.CharField(max_length=200)
    waktu = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.oid}--{self.Create_Date}"

    