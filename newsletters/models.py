from django.db import models
#import PythonMagick  
# Create your models here.
class UploadModel(models.Model):
    
    title=models.CharField(max_length=140)
    date=models.DateTimeField()
    file = models.FileField(upload_to='uploads/%Y/%m/%d/%H/%M/%S/')
    image = models.FileField(upload_to='uploads/image/%Y/%m/%d/%H/%M/%S/')
	
	
    def __unicode__(self):
		return self.title      
		
		
	#// not working as of now, need to manually convert pdf file to png using "save.py" and upload to image
    #def save(self, *args, **kwargs):    
    #    img = PythonMagick.Image()
    #    img.density("300")
	#    img.read(file)
    #    image=img.write("test.png")
    #    return super(models.Model, self).save(*args, **kwargs) 