from django.shortcuts import render,HttpResponse,redirect
from  . models import Addharno,Student
from . forms import Adharform,Studentform

# Create your views here.
def home(req):
    form=Adharform()
    form1=Studentform()
    return render(req,'app/home.html',{'form':form,'form1':form1})

def adhardata(req):
    if req.method == "POST":
        form = Adharform(req.POST)
        if form.is_valid():
            form.save()
            return redirect('/', {'form': form})
        else:
            msg = "Form is not valid"
            return render(req, 'app/home.html', {'error': msg})
    else:
        return render(req, 'app/home.html')
       
def student_form(req):
    if req.method == 'POST':
        form1= Studentform(req.POST)
        if form1.is_valid():
            form1.save()
            return redirect('/', {'form1': form1})
        else:
            msg = "Form is not valid"
            return render(req, 'app/home.html', {'error': msg})
    else:
        return render(req, 'app/home.html')
            


# def adhardata(req):
#     if req.method=="POST":
#        form=Adharform();
#        if form.is_valid():
#             form.save()
#             return render(req,'app/home.html',{'form':form})
#        else:
#            msg="form is not valid";
#            return render(req,'app/home.html',{'error':msg})
#     else:
#         return render(req,'app/home.html')
       

