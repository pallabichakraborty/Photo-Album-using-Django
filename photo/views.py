# Code Reference: https://github.com/buckyroberts/Viberr

from django.views import generic
from .models import Photo
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from .forms import UserForm,PhotoForm
from django import forms

# List of all allowed photo extensions
IMAGE_TYPES =['png','gif','jpg','jpeg']

# View for the default page for viewing photos
# View available for unauthenticated users as well
def index(request):
    # Fetch all the Photos from the library
    all_photos = Photo.objects.all()
    # Data to be passed to the HTML page
    context = {
                #All photos in the library
                'all_photo': all_photos,
                # If the user is authenticated or not. If authenticated then returns true else false
                'user_authenticated':request.user.is_authenticated()
              }
    #After the Photo upload is successful redirect to default page
    return render(request,'photo/index.html',context)

# View for showing the photos uploaded by an authenticated user
def userphotoview(request):
    #If user is not authenticated, then redirect to Login Page
    if not request.user.is_authenticated():
        return render(request, 'photo/login.html')
    else:
        # Return photos which have been uploaded by the user
        photos = Photo.objects.filter(user_id=request.user)
        return render(request, 'photo/user_photo.html', {'photos': photos,'user_authenticated':request.user.is_authenticated()})

# Detail View for a Photo
class DetailView(generic.DetailView):
    template_name = "photo/details.html"
    model=Photo

# View for Photo Upload
def photoupload(request):
        # Photo Form generated with initial values set for user_id and photo_caption
        form = PhotoForm(request.POST or None, request.FILES or None,initial={"user_id":request.user,"photo_caption":"No Caption"})
        # If form is valid then go ahead else redirect to Photo Upload Page
        if form.is_valid():
            photo = form.save(commit=False)
            photo.photo_file = request.FILES['photo_file']
            # Check the file type to check for the extension
            file_type = photo.photo_file.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_TYPES:
                context = {
                    'photo': photo,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, GIF or JPEG',
                }
                return render(request, 'photo/photo_form.html', context)
            # Save the photo object if everything is okay
            photo.save()
            # Redirect to the default photo page if the Photo upload is successful
            return render(request, 'photo/details.html',{'photo':photo,})
        # Variables form and the user uploaded file passed to the HTML file
        context={
            "form" : form,
            'user_authenticated':request.user.is_authenticated()
        }
        return render(request, 'photo/photo_form.html', context)

# View to update the details of the Photo object
class PhotoUpdate(UpdateView):
    model=Photo
    fields = ['photo_caption']

#View to delete a Photo Object
class PhotoDelete(DeleteView):
    model=Photo
    # After successful deletion , redirect to default Photo page
    success_url = reverse_lazy('photo:index')


# View  to simulate registration form
def register(request):
    # Generate user form with the values provided
    form = UserForm(request.POST or None)
    # If form is valid then go ahead else redirect to registration form again
    if form.is_valid():
        user = form.save(commit=False)
        # Save username, password in the user table
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        # Authenticate user and redirect to the User Photo Upload page
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                photo = Photo.objects.filter(user_id=request.user)
                return render(request, 'photo/user_photo.html', {'photos': photo})
    context = {
        "form": form,
    }
    return render(request, 'photo/registration_form.html', context)

# View to authenticate user login
def login_user(request):
    #Authenticate user
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        # If the user is registered then proceed else output error
        if user is not None:
          login(request, user)
          photo = Photo.objects.filter(user_id=request.user)
          return render(request, 'photo/user_photo.html', {'photos': photo,'user_authenticated':request.user.is_authenticated()})
        else:
            return render(request, 'photo/login.html', {'error_message': 'Invalid login'})
    return render(request, 'photo/login.html')

# View to simulate logout
def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {"form": form,}
    # Redirect to login form
    return render(request, 'photo/login.html', context)