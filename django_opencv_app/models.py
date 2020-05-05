from django.db import models


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(null=False, max_length=40)
    modified_image = models.ImageField(upload_to='modified_images/', null=True, blank=True)
    
    def __str__(self):
        return self.title

    def save(self):
        self.modified_image.save(self.image.name, self.image, save=False)
        super(Image, self).save()

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'