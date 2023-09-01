from django.shortcuts import render,redirect
from .models import todo
from .forms import todoForm


# Create your views here.
def index(request):
    if request.method == "POST":
        a = todoForm(request.POST)
        if a.is_valid:
            a.save()
    a = todoForm()
    b = todo.objects.all()

    return render(request,"index.html",{"form":a, 'data':b})


def delete(request,id):
    c = todo.objects.get(id=id)
    c.delete()
    return redirect("index")






# from django.shortcuts import render, redirect
# from .models import todo
# from .forms import todoForm

# # Create your views here.


# def index(request):
#     if request.method == "POST":
#         a = todoForm(request.POST)
#         if a.is_valid:
#             a.save()
#     a = todoForm()
#     b = todo.objects.all()
    
#     return render(request,'index.html',{'form' : a,'data':b})


# def delete(request, id):
#     c =todo.objects.get(id=id)
#     c.delete()
#     return redirect('index')
   