from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    count = User.objects.count()
    return render(request,'home.html',{
        'count':count
    })

# def signup(request):
#     return render(request,'registration/signup.html')

def signup(request):
    if request.method  == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():#password မှန်လား username မှန်လားတွေပါစစ်ပေးတာ
            form.save()
            return redirect('home')
    else:#if method is get method
        form = UserCreationForm()
    return render(request,'registration/signup.html',{
        'form':form
    })
   