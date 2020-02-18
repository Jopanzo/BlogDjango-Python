from django.shortcuts import render
from .models import Blog
from .forms import BlogModelForm



def blog_view(request):
    obj = Blog.objects.get(id=1)
    context = {
        'object' : obj,
        }
    return render(request,'blog.html',context)
# Create your views here.
def blog_create_view(request):
    
    context = {}
    return render(request,'create.html',context)

#def blog_create_view(request):
#    form = BlogModelForm(request.POST or None)
#    if form.is_valid():
#        form.save()
#        form = BlogModelForm()
#    context = {
#        'form': form
#        }
#    return render(request,'create.html',context)
