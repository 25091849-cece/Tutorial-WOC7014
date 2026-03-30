# Sample Data Loader Documentation

## Overview

The Phone Radar database now includes a management command that automatically populates all models with realistic sample data. This is useful for testing, development, and demonstrations.

## Loading Sample Data

### Command Syntax
```powershell
python manage.py load_sample_data
```

### What Gets Loaded

#### 1. Users (2)
- **Admin User**: username=`admin`, password=`admin123`
- **Test User**: username=`reviewer`, password=`reviewer123`

#### 2. Brands (5)
- Apple (USA, 1976)
- Samsung (South Korea, 1938)
- Google (USA, 1998)
- OnePlus (China, 2013)
- Xiaomi (China, 2010)

#### 3. Phone Models (8)
- Apple iPhone 15 Pro Max
- Apple iPhone 15
- Samsung Galaxy S24 Ultra
- Samsung Galaxy S24
- Google Pixel 8 Pro
- Google Pixel 8
- OnePlus 12
- Xiaomi 14 Ultra

#### 4. Reviews (8)
- iPhone 15 Pro Max - Exceptional Performance (5⭐)
- Samsung Galaxy S24 Ultra - Best Android Phone (5⭐)
- Google Pixel 8 Pro - Best Camera Phone (5⭐)
- OnePlus 12 - Great Value Flagship (4⭐)
- iPhone 15 vs Galaxy S24 - Detailed Comparison (4⭐)
- Budget Phone Comparison - Xiaomi 14 Ultra (4⭐)
- Google Pixel 8 - Best Value Flagship (4⭐)
- Samsung Galaxy S24 - Solid Mid-Range Option (4⭐)

#### 5. Review Resources (7+)
Each review includes links to:
- Official specifications
- Technical reviews on GSMArena
- Camera comparisons
- Camera rating sites

## Features

✅ **Idempotent**: Safe to run multiple times - won't duplicate data
✅ **Comprehensive**: Covers all models with realistic data
✅ **Many-to-Many**: Reviews linked to multiple phone models
✅ **Resources**: Each review includes related links
✅ **Users**: Sample users for admin and content creation
✅ **Feedback**: Colored output showing what was created

## File Location

`PhoneReview/management/commands/load_sample_data.py`

## How It Works

The command:
1. Creates or reuses admin and test users
2. Creates 5 phone brands from different countries
3. Creates 8 phone models across different brands and platforms
4. Creates 8 reviews with realistic content and ratings
5. Establishes many-to-many relationships between reviews and models
6. Adds review resources (external links)

## Data Verification

After loading, verify data with:

```bash
python manage.py shell
>>> from PhoneReview.models import Brand, PhoneModel, Review, ReviewResource
>>> Brand.objects.count()  # Should be 5
>>> PhoneModel.objects.count()  # Should be 8
>>> Review.objects.count()  # Should be 8
>>> ReviewResource.objects.count()  # Should be 7+
```

## Accessing Sample Data via Admin

1. Start server: `python manage.py runserver`
2. Visit: `http://127.0.0.1:8000/admin/`
3. Login with:
   - Username: `admin`
   - Password: `admin123`
4. Browse all tables with sample data

## Sample Data Details

### Brands with Real Information
Each brand includes:
- Origin country
- Manufacturing since year
- Official website URL
- Company description

### Phone Models with Specifications
Each model includes:
- Brand (Foreign Key)
- Model name
- Launch date
- Platform (Android/iOS)
- Storage options
- Detailed description
- Specifications list

### Reviews with Content
Each review includes:
- Title
- Detailed article content
- Rating (1-5 stars)
- Author (User FK)
- Related phone models (M2M)
- Publication date (auto)

### Review Resources with Links
Each resource includes:
- Link title
- URL to official site or review
- Description of resource
- Linked to specific review

## Database Summary After Loading

```
✅ Brands: 5
✅ Phone Models: 8
✅ Reviews: 8
✅ Review Resources: 7+
✅ Users: 2
```

## Safe to Run Multiple Times

The command uses `get_or_create()` for all objects, which means:
- If data already exists, it won't be duplicated
- You can run it again without issues
- Perfect for testing and development

## Modifying Sample Data

To customize the sample data, edit:
`PhoneReview/management/commands/load_sample_data.py`

Then modify:
- `brands_data` list for brands
- `models_data` list for phone models
- `reviews_data` list for reviews
- `resources_data` list for resource links

## Example: Adding More Data

To add more sample data, follow the same pattern in `load_sample_data.py`:

```python
models_data = [
    {
        'brand': 'Brand Name',
        'model_name': 'Model Name',
        'launch_date': 'YYYY-MM-DD',
        'platform': 'Android',  # or iOS, Windows, Other
        'storage_options': 'Storage sizes',
        'description': 'Description',
        'specifications': 'Specs'
    },
    # ... more models
]
```

## Quick Start with Sample Data

```bash
# 1. Load sample data
python manage.py load_sample_data

# 2. Create superuser (if needed)
python manage.py createsuperuser

# 3. Start server
python manage.py runserver

# 4. Visit admin panel
# http://127.0.0.1:8000/admin/
```

## Troubleshooting

### Command Not Found
- Make sure you're in the project root directory
- Verify `PhoneReview/management/commands/load_sample_data.py` exists
- Check that `__init__.py` files exist in management and commands directories

### Data Not Showing in Admin
- Make sure migrations were run: `python manage.py migrate`
- Verify admin models are registered in `PhoneReview/admin.py`
- Check if you're logged in as admin user

### Duplicate Data Issues
- The command is safe to run multiple times
- It won't create duplicates due to `get_or_create()`
- If issues persist, delete `db.sqlite3` and run migrations again

---

**Created**: March 29, 2026
**Status**: Ready to Use ✅

