from django.db import models

class StatusSenha(models.Model):
    nome = models.CharField(max_length=100, null=False)

class Tipo(models.Model):
    nome = models.CharField(max_length=100, null=False)

class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=False)

class Senha(models.Model):
    senha = models.IntegerField(null=False)
    hora_data = models.DateTimeField()

    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, related_name='senha_tipo')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='senha_categoria')
    status_senha = models.ForeignKey(StatusSenha, on_delete=models.CASCADE, related_name='senha_status_senha')
