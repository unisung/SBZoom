from django.db import models

# Create your models here.
class GuModel(models.Model):
      guName = models.CharField(max_length=100)
      code = models.CharField(max_length=10)
      quarter = models.CharField(max_length=20)
      ilban = models.DecimalField(max_digits=10,decimal_places=0)
      franchise= models.DecimalField(max_digits=10,decimal_places=0)
      total = models.DecimalField(max_digits=10,decimal_places=0)
      sales = models.DecimalField(max_digits=10,decimal_places=0)
      
      def __str__(self):
        return self.guName + self.code+ self.quarter
      #출처: https://e-you.tistory.com/357 [Development:티스토리]

class GuNames(models.Model):
      guname = models.CharField(max_length=100)
      eng = models.CharField(max_length=20)
      lowerEng=models.CharField(max_length=20)

      def __str__(self):
          return self.guname +":"+ self.eng +":"+ self.lowerEng
