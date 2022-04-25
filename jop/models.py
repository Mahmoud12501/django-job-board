
from distutils.command.upload import upload
from django.db import models

''''
django model filed:
    - html widget
    - validation
    - db size

'''


'''
image upload
عشان نرفع صورة نستخدم     image=models.ImageField(upload_to=upload_img)
 
upload_to الصورة ههتحفظ فين 
ممكن تعمل فانكشن تظبط الحوار ده
زي الا تحت دي upload_img 
'''

def upload_img(instance,filname):
    img_name ,ext=filname.split('.')
    return f"jobs/{instance.id}.{ext}"
JOP_TYPE=(
    ('Full time','Full Time'),
    ('Part time','Part Time'),
)
# Create your models here.
class job(models.Model):   # class == tabel
    title=models.CharField(max_length=100) # colum
    # location
    Jop_type=models.CharField(max_length=15,choices=JOP_TYPE)
    Job_description=models.TextField(max_length=1000)
    Published_at=models.DateTimeField(auto_now=True)
    Vacancy=models.IntegerField(default=1)
    Salary=models.IntegerField(default=1)
    excperience=models.IntegerField(default=1)
    category=models.ForeignKey('Category',on_delete= models.CASCADE)
    image=models.ImageField(upload_to=upload_img)
    
    def __str__(self) :
        return self.title

class Category(models.Model):
        name=models.CharField(max_length=25)

        def __str__(self):
            return self.name
            
    