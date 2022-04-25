from django.shortcuts import render
from .models import job
# Create your views here.

def jop_list(requist):
    jop_list=job.objects.all()
    contxt={'jops':jop_list}
    # print(jop_list)

    return render(requist,'jop/jopList.html',contxt)

def jop_dtail(requist,id):
    jop_dtail=job.objects.get(id=id)
     
    context={'detail':jop_dtail}

    return render(requist,'jop/jopDetail.html',context)