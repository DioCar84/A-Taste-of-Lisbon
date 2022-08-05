from django.shortcuts import render
from restaurant.models import Photo 

# Create your views here.
def blog(request):
    blog_image = Photo.objects.get(title='Blog Test')
    context = {'blog_image': blog_image, }
    return render(request, 'blog/blog_home.html', context)
