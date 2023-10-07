from django.shortcuts import render
from .forms import StudentModelForms
from .models import StudentModels

def home(request):

    if request.method=='POST':
        fm=StudentModelForms(request.POST)
        # stud=""
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            ag=fm.cleaned_data['age']
            reg=StudentModels(name=nm,age=ag)
            reg.save()
            fm=StudentModelForms()
    else:
        fm=StudentModelForms()
    stud=StudentModels.objects.all()
    return render(request,'home.html',{'fm':fm,'stud':stud})