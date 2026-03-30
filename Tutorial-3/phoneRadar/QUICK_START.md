# Phone Radar - Quick Start Guide

## Prerequisites
- Python 3.8+
- Django 6.0.3
- Virtual environment activated: `.venv`

---

## Step 1: Start the Development Server

Open PowerShell in the project directory and run:

```powershell
python manage.py runserver
```

Expected output:
```
Starting development server at http://127.0.0.1:8000/
```

---

## Step 2: Test the Main Page

Open your browser and navigate to:

```
http://127.0.0.1:8000/index
```

Expected response:
```
This is the main page for Phone Radar website
```

---

## Step 3: Create a Superuser (Admin Account)

In a new PowerShell window (keep server running in the first), run:

```powershell
python manage.py createsuperuser
```

Follow the prompts:
- Username: (enter your choice, e.g., `admin`)
- Email: (enter your email)
- Password: (enter a secure password)
- Password (again): (confirm password)

Example:
```
Username: admin
Email: admin@phoneradar.com
Password: ****
Password (again): ****
Superuser created successfully.
```

---

## Step 4: Access the Admin Panel

In your browser, navigate to:

```
http://127.0.0.1:8000/admin/
```

Login with the superuser credentials you just created.

---

## Step 5: Add Test Data

### Add a Brand

1. Click on **Brands** in the admin panel
2. Click **+ Add Brand**
3. Fill in the form:
   - **Name**: Apple
   - **Origin Country**: United States
   - **Manufacturing Since**: 1976
   - **Website URL**: https://www.apple.com
   - **Description**: Apple Inc. is a technology company

4. Click **Save**

### Add Phone Models

1. Click on **Phone Models** in the admin panel
2. Click **+ Add Phone Model**
3. Fill in the form:
   - **Brand**: Apple
   - **Model Name**: iPhone 15 Pro Max
   - **Launch Date**: 2023-09-22
   - **Platform**: iOS
   - **Storage Options**: 256GB, 512GB, 1TB
   - **Description**: Premium flagship smartphone
   - **Specifications**: A17 Pro chip, 48MP main camera, ProMotion display, etc.

4. Click **Save**

Repeat to add more brands and models (e.g., Samsung Galaxy S24, Google Pixel 8).

### Add Reviews

1. Click on **Reviews** in the admin panel
2. Click **+ Add Review**
3. Fill in the form:
   - **Title**: iPhone 15 Pro Max - Exceptional Performance
   - **Content**: This is an amazing phone with incredible camera capabilities...
   - **Rating**: 5 (Click stars to rate)
   - **Author**: admin (automatically selected if editing own review)
   - **Phone Models**: Check iPhone 15 Pro Max and any other phones this review covers
   - **Is Active**: ✓ (checked)

4. Click **Add another Review Resource** to add links:
   - **Title**: Apple Official Specs
   - **URL**: https://www.apple.com/iphone-15-pro/specs/
   - **Description**: Official specifications from Apple

5. Click **Save**

---

## Admin Interface Features

### Brand Management
- **List**: View all brands with filtering by country
- **Search**: Find brands by name or country
- **Edit**: Modify brand information
- **Delete**: Remove brands (if no associated phones)

### Phone Model Management
- **List**: View all models with filtering by brand and platform
- **Search**: Find models by name or brand
- **Edit**: Modify phone specifications
- **Delete**: Remove phone models

### Review Management
- **List**: View all reviews with filtering by rating, date, and status
- **Filter by Brand**: See reviews related to specific brands
- **Search**: Find reviews by title, content, or author
- **Edit**: Modify review content and associations
- **Add Resources**: Attach links directly to reviews
- **Toggle Active**: Deactivate inappropriate reviews

---

## Database Models at a Glance

### Brand
Stores phone manufacturer information
- Name (unique)
- Origin country
- Manufacturing since (year)
- Website URL
- Description

### PhoneModel
Stores phone model information
- Linked to Brand (Foreign Key)
- Model name
- Launch date
- Platform (Android/iOS/Windows/Other)
- Storage options
- Specifications and description

### Review
Stores phone reviews
- Title and content
- Rating (1-5 stars)
- Author (linked to User)
- Date published
- Can cover multiple phone models (Many-to-Many)
- Active/inactive status

### ReviewResource
Stores links and resources related to reviews
- Title and URL
- Description
- Linked to Review (Foreign Key)

---

## Key Validation Rules

### Review Rating
- Must be between 1 and 5 stars

### Brand Manufacturing
- Year must be >= 1900

### Phone Model
- Must have a unique combination of brand + model name
- Launch date is required
- Platform must be selected from: Android, iOS, Windows, Other

### URLs
- All URL fields accept standard web URLs

---

## Common Admin Tasks

### Filtering
- Click filter options on the right side of list view
- Filter by brand, date, rating, platform, etc.

### Searching
- Use the search box at the top
- Search across: name, title, content, username, etc.

### Bulk Actions
- Select multiple items with checkboxes
- Use the action dropdown at the bottom

### Exporting Data
- The admin interface supports viewing all data
- Can use Django shell for advanced exports

---

## Troubleshooting

### Admin login fails
- Verify superuser was created: `python manage.py createsuperuser`
- Check username/password

### Database issues
- Reset database: Delete `db.sqlite3` and run `python manage.py migrate`
- Create new superuser after reset

### Server won't start
- Verify port 8000 is not in use
- Run: `python manage.py runserver 8001` to use a different port

### Model changes
- After modifying models.py: `python manage.py makemigrations`
- Then: `python manage.py migrate`

---

## Next Development Steps

1. **Create Templates** for displaying phone list and reviews
2. **Implement User Registration** form for new users
3. **Add Login/Logout** functionality
4. **Build Frontend Pages** for browsing phones and reviews
5. **Create Review Form** for authenticated users to add reviews
6. **Add Search & Filter** functionality on frontend
7. **Implement User Dashboard** for personal reviews

---

## File Locations

- **Admin Configuration**: `PhoneReview/admin.py`
- **Data Models**: `PhoneReview/models.py`
- **Main App View**: `main/views.py`
- **URL Routing**: `phoneRadar/urls.py` and `main/urls.py`
- **Settings**: `phoneRadar/settings.py`
- **Database**: `db.sqlite3`

---

## Useful Django Commands

```powershell
# Run development server
python manage.py runserver

# Create superuser
python manage.py createsuperuser

# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Access Django shell (interactive Python with Django)
python manage.py shell

# Check for issues
python manage.py check
```

---

**Ready to start?** Run `python manage.py runserver` and navigate to the admin panel!

