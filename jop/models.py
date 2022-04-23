
from django.db import models

''''
django model filed:
    - html widget
    - validation
    - db size

'''
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
    
    def __str__(self) :
        return self.title