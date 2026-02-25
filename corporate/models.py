from django.db import models
from django.urls import reverse


class Product(models.Model):
    """Core product model managed by admins."""

    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, max_length=160)
    image = models.ImageField(upload_to='products/')
    short_description = models.CharField(max_length=220)
    description = models.TextField()
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse('corporate:product_detail', kwargs={'slug': self.slug})


class ProductImage(models.Model):
    """Additional gallery images for product detail pages."""

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to='products/gallery/')
    caption = models.CharField(max_length=120, blank=True)

    def __str__(self) -> str:
        return f"{self.product.name} image"


class Inquiry(models.Model):
    """Stores contact and product inquiry submissions."""

    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=150, blank=True)
    subject = models.CharField(max_length=160)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Inquiries'

    def __str__(self) -> str:
        return f"{self.name} - {self.subject}"


class GalleryImage(models.Model):
    """Images for a standalone gallery page."""

    title = models.CharField(max_length=120)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.title


class BlogPost(models.Model):
    """Simple blog/news content model."""

    title = models.CharField(max_length=180)
    slug = models.SlugField(unique=True, max_length=190)
    summary = models.CharField(max_length=240)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True)
    published_at = models.DateField()
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self) -> str:
        return reverse('corporate:blog_detail', kwargs={'slug': self.slug})
