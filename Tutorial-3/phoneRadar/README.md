# Phone Radar - Phone Reviews Website

A Django-based website for reviewing phone brands and models. Users can browse phone reviews, register as members, and contribute their own reviews and related resources.

## Project Overview

**Phone Radar** is a comprehensive web application built with Django that allows users to:
- Browse and read phone reviews
- Register as members and create accounts
- Log in to add new phones, models, and reviews
- Link reviews to multiple phone models
- Share resources and links related to reviews
- Access an admin panel for content management

## Technology Stack

- **Framework**: Django 6.0.3
- **Database**: SQLite3
- **Backend Language**: Python 3.8+
- **ORM**: Django ORM
- **Authentication**: Django built-in auth system

## Project Structure

```
phoneRadar/
├── db.sqlite3                      # SQLite database
├── manage.py                       # Django management script
│
├── phoneRadar/                     # Main project folder
│   ├── settings.py                # Project settings
│   ├── urls.py                    # Main URL configuration
│   ├── wsgi.py                    # WSGI configuration
│   └── asgi.py                    # ASGI configuration
│
├── main/                           # Main app (homepage)
│   ├── views.py                   # Index view
│   ├── urls.py                    # Main app URL routing
│   ├── admin.py                   # Admin configuration
│   ├── models.py                  # App models
│   └── migrations/                # Database migrations
│
├── PhoneReview/                   # Phone review app
│   ├── models.py                  # Brand, PhoneModel, Review, ReviewResource
│   ├── admin.py                   # Admin interface configuration
│   ├── views.py                   # Views (to be developed)
│   ├── urls.py                    # URL routing (to be developed)
│   └── migrations/                # Database migrations
│
├── templates/                      # HTML templates (to be developed)
│
└── Documentation Files:
    ├── SITEMAP.md                 # Website structure and navigation
    ├── STORYBOARD.md              # User flows and wireframes
    ├── QUICK_START.md             # How to use the application
    ├── IMPLEMENTATION_SUMMARY.md   # Complete implementation details
    ├── REQUIREMENTS_CHECKLIST.md   # Requirements verification
    └── README.md                   # This file
```

## Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. **Navigate to project directory**
   ```powershell
   cd C:\Users\Asus\Documents\GitHub\Tutorial-WOC7014\Tutorial-3\phoneRadar
   ```

2. **Activate virtual environment** (if not already activated)
   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. **Install dependencies** (if needed)
   ```powershell
   pip install django
   ```

4. **Start the development server**
   ```powershell
   python manage.py runserver
   ```

5. **Access the application**
   - Main page: http://127.0.0.1:8000/index
   - Admin panel: http://127.0.0.1:8000/admin/

### Initial Setup

1. **Create a superuser account**
   ```powershell
   python manage.py createsuperuser
   ```
   Follow the prompts to set username, email, and password.

2. **Access Django Admin**
   - Go to http://127.0.0.1:8000/admin/
   - Log in with your superuser credentials

3. **Add test data**
   - Create brands (e.g., Apple, Samsung, Google)
   - Add phone models for each brand
   - Write reviews and link them to phone models
   - Add related resources/links to reviews

## Data Models

### Brand
Stores information about phone manufacturers

| Field | Type | Description |
|-------|------|-------------|
| name | String | Unique brand name |
| origin_country | String | Country where brand originates |
| manufacturing_since | Integer | Year manufacturing began (≥1900) |
| website_url | URL | Brand website (optional) |
| description | Text | Brand description (optional) |
| created_at | DateTime | Auto-set creation timestamp |
| updated_at | DateTime | Auto-updated modification timestamp |

### PhoneModel
Stores information about specific phone models

| Field | Type | Description |
|-------|------|-------------|
| brand | FK | Foreign key to Brand |
| model_name | String | Name of phone model |
| launch_date | Date | Date phone was launched |
| platform | Choice | OS: Android, iOS, Windows, Other |
| storage_options | String | Available storage sizes |
| description | Text | Model description |
| specifications | Text | Technical specifications |
| created_at | DateTime | Auto-set creation timestamp |
| updated_at | DateTime | Auto-updated modification timestamp |

### Review
Stores phone reviews

| Field | Type | Description |
|-------|------|-------------|
| title | String | Review title |
| content | Text | Review content/article |
| rating | Integer | Rating 1-5 stars |
| author | FK | Foreign key to User |
| phone_models | M2M | Many-to-many to PhoneModel |
| date_published | DateTime | Auto-set publication date |
| updated_at | DateTime | Auto-updated modification timestamp |
| is_active | Boolean | Whether review is visible (default: True) |

### ReviewResource
Stores links and resources related to reviews

| Field | Type | Description |
|-------|------|-------------|
| review | FK | Foreign key to Review |
| title | String | Resource title |
| url | URL | Link to external resource |
| description | Text | Resource description (optional) |
| created_at | DateTime | Auto-set creation timestamp |

## Key Relationships

### Foreign Keys
- **PhoneModel → Brand**: Many phone models belong to one brand
- **Review → User**: Many reviews written by one user
- **ReviewResource → Review**: Many resources linked to one review

### Many-to-Many
- **Review ↔ PhoneModel**: One review can cover multiple phone models; one model can be in multiple reviews

## Admin Interface Features

### Brand Management
- Add, edit, delete brands
- Filter by country and creation date
- Search by name and country
- View manufacturing information

### Phone Model Management
- Add, edit, delete phone models
- Associate with brands
- Filter by brand and platform
- Search by model name
- Manage specifications

### Review Management
- Add, edit, delete reviews
- Manage review status (active/inactive)
- Link reviews to multiple phone models
- Add/edit review resources inline
- Filter by rating, date, status, and brand
- Search reviews by title, content, or author
- Auto-assign current user as author

### Review Resource Management
- Add, edit, delete resources
- Link resources to reviews
- Manage external links and references

## API Endpoints

### Currently Implemented
- `/index` - Main page with HTTP response

### To Be Developed
- Phone list and filtering
- Phone detail view
- Review list and filtering
- Review detail view
- User registration
- User login/logout
- Add review form
- User dashboard

## Authentication & Permissions

The application uses Django's built-in authentication system:

- **Anonymous Users**: Can view phone list and reviews
- **Registered Users**: Can add reviews and resources
- **Staff Users**: Can manage other users' reviews
- **Superuser**: Full admin access to all features

Future implementation will include:
- Custom permission system
- Review moderation workflow
- User role management

## File Descriptions

### Documentation
- **SITEMAP.md** - Complete website structure with all pages and navigation flows
- **STORYBOARD.md** - User journey flows (guest, registered, admin) with wireframe designs
- **QUICK_START.md** - Step-by-step guide to using the application
- **IMPLEMENTATION_SUMMARY.md** - Detailed implementation information
- **REQUIREMENTS_CHECKLIST.md** - Verification of all project requirements

### Code Files
- **phoneRadar/settings.py** - Django settings with app registration
- **phoneRadar/urls.py** - Main URL configuration
- **main/views.py** - Main app view (index endpoint)
- **main/urls.py** - Main app URL routing
- **PhoneReview/models.py** - All data models
- **PhoneReview/admin.py** - Admin interface configuration

## Useful Commands

```powershell
# Start development server
python manage.py runserver

# Create superuser
python manage.py createsuperuser

# Create database migrations (after model changes)
python manage.py makemigrations

# Apply migrations to database
python manage.py migrate

# Access Django interactive shell
python manage.py shell

# Run tests
python manage.py test

# Check project for issues
python manage.py check

# Create a backup of database
python manage.py dumpdata > backup.json

# Restore from backup
python manage.py loaddata backup.json
```

## Testing

### Test Main Endpoint
1. Start server: `python manage.py runserver`
2. Open browser: http://127.0.0.1:8000/index
3. Expected: "This is the main page for Phone Radar website"

### Test Admin Interface
1. Create superuser: `python manage.py createsuperuser`
2. Visit: http://127.0.0.1:8000/admin/
3. Login with superuser credentials
4. Test CRUD operations on all models

### Test Database Models
```python
python manage.py shell
>>> from PhoneReview.models import Brand, PhoneModel, Review, ReviewResource
>>> from django.contrib.auth.models import User

# Create test data
>>> brand = Brand.objects.create(
...     name="Apple",
...     origin_country="USA",
...     manufacturing_since=1976
... )

>>> print(Brand.objects.all())
# Should show: <QuerySet [<Brand: Apple>]>
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Port 8000 already in use | Use: `python manage.py runserver 8001` |
| Database errors | Delete `db.sqlite3` and run `python manage.py migrate` |
| Admin won't load | Verify superuser exists: `python manage.py createsuperuser` |
| Model changes not reflecting | Run: `python manage.py makemigrations && python manage.py migrate` |
| Import errors | Verify apps in INSTALLED_APPS in settings.py |

## Future Development

### Phase 1: Frontend (In Progress)
- [ ] Homepage template with latest reviews
- [ ] Phone list and detail pages
- [ ] Review list and detail pages
- [ ] User dashboard

### Phase 2: User Features
- [ ] Custom registration form
- [ ] User profile management
- [ ] Review creation form
- [ ] Permission system

### Phase 3: Advanced Features
- [ ] Search and advanced filtering
- [ ] Review ratings and sorting
- [ ] User comments on reviews
- [ ] Review recommendations
- [ ] Email notifications

### Phase 4: APIs & Integration
- [ ] RESTful API
- [ ] Mobile app support
- [ ] Social media integration
- [ ] Analytics dashboard

## Requirements Met ✅

1. ✅ Website planning with sitemap and storyboard
2. ✅ Django project "phoneradar" created
3. ✅ Main app with /index endpoint
4. ✅ PhoneReview app with complete data models
5. ✅ Brand, PhoneModel, Review, ReviewResource models
6. ✅ Many-to-many relationship (Review ↔ PhoneModel)
7. ✅ Admin site with full CRUD capabilities for all tables

## License

This project is for educational purposes.

## Author

Created as part of Tutorial-WOC7014, Tutorial-3

## Support

For issues or questions, refer to:
- Documentation files (SITEMAP.md, STORYBOARD.md, QUICK_START.md)
- Django official documentation: https://docs.djangoproject.com/
- Django Admin documentation: https://docs.djangoproject.com/en/6.0/ref/contrib/admin/

---

**Last Updated**: March 29, 2026
**Status**: Development Phase - Backend Complete

