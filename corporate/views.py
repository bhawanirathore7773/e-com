from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from .forms import InquiryForm
from .models import BlogPost, GalleryImage, Product


def home(request):
    """Corporate homepage with featured products and overview sections."""
    context = {
        'featured_products': Product.objects.filter(featured=True)[:6],
        'latest_posts': BlogPost.objects.filter(is_published=True)[:3],
    }
    return render(request, 'core/home.html', context)


def about(request):
    return render(request, 'core/about.html')


def products(request):
    return render(request, 'core/products.html', {'products': Product.objects.all()})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'core/product_detail.html', {'product': product})


def contact(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your inquiry has been submitted successfully.')
            return redirect('corporate:contact')
        messages.error(request, 'Please correct the errors below and resubmit the form.')
    else:
        form = InquiryForm()

    return render(request, 'core/contact.html', {'form': form})


def gallery(request):
    return render(request, 'core/gallery.html', {'images': GalleryImage.objects.all()})


def blog_list(request):
    posts = BlogPost.objects.filter(is_published=True)
    return render(request, 'core/blog_list.html', {'posts': posts})


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    return render(request, 'core/blog_detail.html', {'post': post})
