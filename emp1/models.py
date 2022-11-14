from django.db import models

class Emp(models.Model):

    name = models.CharField(max_length=200)
    desc= models.CharField(max_length=100)

    def __str__(self):

        return self.name+"  "+self.desc
    
        
