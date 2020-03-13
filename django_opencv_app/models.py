from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(null=False, max_length=40)
    modified_image = models.ImageField(upload_to='modified_images/', null=True, blank=True)


    def save(self):
        self.modified_image.save(self.image.name, self.image, save=False)
        super(Image, self).save()

