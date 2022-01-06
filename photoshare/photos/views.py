from django.shortcuts import render, redirect
from .models import Category, Photo
# Create your views here.
def gallery(req):
    category=req.GET.get('category')
    if category==None:
           photos=Photo.objects.all()
         
    else:
           photos=Photo.objects.filter(category__name=category)

    categories=Category.objects.all()
    context={'categories':categories, 'photos':photos}
    return render(req, 'photos/gallery.html', context)

def viewPhoto(req, pk):
    photo=Photo.objects.get(id=pk)
    return render(req, 'photos/photo.html', {'photo':photo})

def addPhoto(req):
    categories=Category.objects.all()

    if req.method == 'POST':
        data=req.POST
        image=req.FILES.get('image')

        if data['category'] != 'none':
            category=Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created=Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None

        photo=Photo.objects.create(
                category=category,
                desc=data['desc'],
                image=image,
        )
        return redirect('gallery')

    context={'categories':categories}
    return render(req, 'photos/add.html', context)