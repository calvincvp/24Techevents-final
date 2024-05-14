from django.db import models
import datetime
import os

def getfilename(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

class Images(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=getfilename,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.name
    
class booking(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False)
    mobileno=models.BigIntegerField(null=False,blank=False)
    email=models.EmailField(max_length=150,null=False,blank=False)
    eventtype=models.CharField(max_length=150,null=False,blank=False)
    noofattendees=models.IntegerField(null=False,blank=False)
    dateofevent=models.DateField(max_length=150,null=False,blank=False)
    eventlocation=models.CharField(max_length=150,null=False,blank=False)
    

    
    def __str__(self) :
        return self.name
