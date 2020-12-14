from django.db import models

class Cadastro(models.Model):
    cid_Numero = models.CharField(max_length=10)
    cid_Descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.cid_Numero

