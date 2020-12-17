# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone

class TblAdmin(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    last_login = models.DateTimeField()
    
    class Meta:
        
        db_table = 'tbl_admin'

class Tblproduct(models.Model):
	name = models.CharField(max_length=50)
	price = models.CharField(max_length=50)
	quantity = models.IntegerField(11)
	created_date = models.DateTimeField(auto_now_add=True)

	class Meta:

		db_table = 'tbl_product'	