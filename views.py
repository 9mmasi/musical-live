from django.conf import settings
from django.http.response import Http404, HttpResponse
from Photo.models import Photo
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from.models import *
from.forms import *
from django.template.context import RequestContext


def login(request):
    return render_to_response('login.html', context=RequestContext(request))


def ShowGallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()

    context = {
        'photos': photos,
        'categories': categories
    }

    return render(request, 'gallery.html', context)

@login_required
def Addphoto(request):
    forms = AddPhotoForm(request.POST, request.FILES or None)
    
    if forms.is_valid():
        forms.save()
        return redirect('gallery')

    return render(request, 'addPhoto.html', {'forms': forms})

@login_required
def CreateCategory(request):
    forms = CreatecategoryForm(request.POST or None)

    if forms.is_valid():
        forms.save()
        return redirect('gallery')

    return render(request, 'createCat.html', {'forms': forms})



def ViewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)

    return render(request, 'photo.html', {'photo': photo})

@login_required
def UpdatePhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    forms = UpdatePhotoForm(instance=photo)

    if request.method == 'POST':
        forms = UpdatePhotoForm(request.POST ,request.FILES, instance=photo)
        if forms.is_valid():
            forms.save()
            return redirect('gallery')
   

    return render(request, 'addPhoto.html',{'forms':forms})

@login_required
def DeletePhoto(request,pk):
    photo=Photo.objects.get(id=pk)
    if request.method == "POST":
        photo.delete()
        return redirect('gallery')

    return render(request,'delete.html')        

def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read(),content_type='application/uploaded')
            response['Content-Disposition']='inline,filename='+os.path.basename(file_path)
            return response
    raise Http404    