from django.db import models

class Cid(models.Model):
    codigo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.codigo

