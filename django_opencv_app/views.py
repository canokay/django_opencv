from django.shortcuts import render, redirect
from django.views.generic import View, ListView, CreateView
from django_opencv_app.forms import ImageForm, ImageEditForm
from django_opencv_app.models import Image
from django.http import HttpResponseRedirect
from django.shortcuts import render
import cv2
import numpy as np
from matplotlib import pyplot as plt


class ImageView(View):
    form_class = ImageEditForm
    initial = {'key': 'value'}
    template_name = 'imageedit.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        image = Image.objects.get(id=kwargs['id'])
        return render(request, self.template_name, {'form': form, 'image': image})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        image = Image.objects.get(id=kwargs['id'])
        if form.is_valid():
            img = cv2.imread(image.image.path, 0)
            img = cv2.threshold(img, form.cleaned_data['treshold'], 255, cv2.THRESH_TRUNC)[1]
            if form.cleaned_data['medianblur']:
                img = cv2.medianBlur(img, 5)

            cv2.imwrite(image.modified_image.path, img)
            return render(request, self.template_name, {'form': form, 'image': image})

        return render(request, self.template_name, {'form': form, 'image': image})


class ImageAddView(CreateView):
    form_class = ImageForm
    success_url = '/'
    template_name = 'imageadd.html'

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect('/edit/%s' % self.object.id)



class ImageListView(ListView):
    model = Image
    template_name = 'imagelist.html'

