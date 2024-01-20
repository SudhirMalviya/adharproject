from django.db import models

# Create your models here.
class Addharno(models.Model):
    addharno=models.IntegerField()
    def __str__(self):
        data=str(self.addharno)
        return data




class Student(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Mobile=models.IntegerField(default=0)
    Age=models.IntegerField(default=0)
    Address=models.CharField(max_length=100)
    Addharno=models.OneToOneField(Addharno, on_delete=models.CASCADE,primary_key=True)
    # Addharno=models.OneToOneField(Addharno, on_delete=models.PROTECT,primary_key=True)

