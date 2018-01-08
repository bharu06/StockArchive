from django.contrib import admin
from stock_archive.models import*

class CompanyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Company._meta.fields]
    search_fields = ['symbol']

class CompanyDetailAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CompanyDetail._meta.fields]
    search_fields = ['symbol']

admin.site.register(Company, CompanyAdmin)
admin.site.register(CompanyDetail, CompanyDetailAdmin)
