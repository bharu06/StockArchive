from django.db import models

class Company(models.Model):
    date = models.DateTimeField()
    symbol = models.CharField(max_length=200)
    open_cost = models.FloatField(null = True)
    close_cost = models.FloatField(null = True)
    low_cost = models.FloatField(null = True)
    high_cost = models.FloatField(null = True)
    volume_cost = models.FloatField(null = True)

    class Meta:
        db_table = 'company'

class CompanyDetail(models.Model):
    symbol = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    market_cap = models.FloatField(null=True)
    sector = models.CharField(max_length=200)
    industry = models.CharField(max_length=250)

    class Meta: 
        db_table = 'company_details'