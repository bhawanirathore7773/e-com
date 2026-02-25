# Corporate Business Website (Django)

Production-style corporate website built with Django 4+ and Bootstrap 5.

## Features
- Responsive, mobile-first Bootstrap UI
- Sticky navbar, footer quick links, and hover effects
- Home, About, Products, Product Detail (with image gallery), Contact, Gallery, News pages
- Product + inquiry backend models
- Slug-based SEO-friendly URLs
- Django admin for product/content management
- Image upload support (products, galleries, blog)
- Contact form validation and success/error messages
- Sample fixture data

## Project structure
```
config/                  # Django project settings and global routes
corporate/               # Main app
  fixtures/              # Sample dummy data
  migrations/            # Initial migration
  static/                # CSS/JS
  templates/             # HTML templates
manage.py
requirements.txt
```

## Quick start
1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Create admin user:
   ```bash
   python manage.py createsuperuser
   ```
5. (Optional) Load sample content:
   ```bash
   python manage.py loaddata corporate/fixtures/sample_data.json
   ```
6. Start server:
   ```bash
   python manage.py runserver
   ```

## Media files
Uploaded images are saved under `media/`. In development, Django serves them with `DEBUG=True`.

## Notes
- Update `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, and `DJANGO_ALLOWED_HOSTS` for production.
- Replace sample image paths in fixtures with real uploaded assets.
