from django.shortcuts import render,redirect
from testapp.forms import movieform
from testapp.models import Movie

# Create your views here.
def homeview(request):
    return render (request,'testapp/home.html')
def addmovieview(request):
    form=movieform()
    if request.method=='POST':
        form=movieform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home')
    return render (request,'testapp/addmovie.html',{'form':form})
def movielistview(request):
    movies=Movie.objects.all()
    return render(request,'testapp/movielist.html',{'movies':movies})
