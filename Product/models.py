from django.urls import reverse
from django.db import models
from django.core.files.storage import default_storage as storage
from django.utils import timezone
from PIL import Image
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='Product/images/', null=False, blank=False)
    name = models.CharField(max_length=200, null=False, blank=False)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.name and self.description:
            return

        super(Product, self).save()
        if self.image:
            size = 300, 300
            image = Image.open(self.image)
            image.thumbnail(size, Image.ANTIALIAS)
            fh = storage.open(self.image.name, "w")
            format = 'png'  # You need to set the correct image format here
            image.save(fh, format)
            fh.close()

    def get_absolute_url(self):
        return reverse('prod-detail', kwargs={"id": self.id})


class Comment(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE)
    commenter_name = models.CharField(max_length=200)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)

    def __str__(self):
        return 'Comment {}'.format(self.commenter_name)


