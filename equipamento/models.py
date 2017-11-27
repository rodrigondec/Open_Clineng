from django.db import models
from djmoney.models.fields import MoneyField
from core.models import TecnicoResponsavel
from local.models import Setor


class ContratoProprio(models.Model):
    descricao = models.TextField(max_length=800, null=True)
    valor = MoneyField(max_digits=8, decimal_places=2, default_currency='BRL')

    def __str__(self):
        return "Contrato"


from core.models import EmpresaResponsavel


class ContratoComodato(ContratoProprio):
    empresa = models.ForeignKey(EmpresaResponsavel)


class Equipamento(models.Model):
    nome = models.CharField(max_length=50)
    num_serie = models.CharField(max_length=100)
    reg_anvisa = models.CharField(max_length=100)
    ano_fabricacao = models.DateField("Ano fabricacao")
    data_aquisicao = models.DateField('Data aquisição')
    fabricante = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    setor = models.ForeignKey(Setor, related_name='equipamentos')
    custo = MoneyField(max_digits= 8, decimal_places=2, default_currency='BRL')
    historico = models.TextField(max_length=800)
    manual = models.FileField(upload_to="static/uploads/manuais")
    responsavel = models.ForeignKey(TecnicoResponsavel, related_name='equipamentos_responsavel')
    contrato = models.ForeignKey(ContratoProprio, related_name='equipamentos')

    def __str__(self):
        return self.nome



