from django.shortcuts import render, redirect
from django_opencv_app.models import Image
from django_opencv_app.forms import ImageForm, ImageEditForm
import cv2
import numpy as np
from matplotlib import pyplot as plt

def IndexView(request):
    images = Image.objects.all().order_by("-id")
    context = {
        "images": images
    }
    return render(request, 'index.html', context)




def CreateImageView(request):
    form = ImageForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("django_opencv_app:homepage")

    context = {
        "form":form
    }
    return render(request, "imageadd.html", context)


def EditCv2ImageView(request, id):
    form = ImageEditForm(request.POST or None,request.FILES or None)
    image = Image.objects.get(id=id)
    
    if form.is_valid():
        image = Image.objects.get(id=id)

        # opencv start
        img_main  = cv2.imread(image.image.path, cv2.IMREAD_GRAYSCALE)
        thresh = form.cleaned_data['thresh']

        candidate_img = cv2.threshold(img_main, thresh, 255, cv2.THRESH_BINARY)[1]
        cv2.imwrite(image.modified_image.path, candidate_img)
        # opencv end

        return redirect("django_opencv_app:homepage")

    context = {
        "form" : form,
        "image" : image
    }
    return render(request, "imageedit.html", context)
