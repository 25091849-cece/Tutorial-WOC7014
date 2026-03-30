# Phone Radar - Database Schema & Architecture Diagrams

## Database Schema (ER Diagram)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│                        PHONE RADAR DATABASE                            │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘


                            ┌──────────────────┐
                            │      Brand       │
                            ├──────────────────┤
                            │ id (PK)          │
                            │ name             │
                            │ origin_country   │
                            │ manufacturing... │
                            │ website_url      │
                            │ description      │
                            │ created_at       │
                            │ updated_at       │
                            └──────────────────┘
                                    ▲
                                    │ 1
                                    │
                            ◄───────┼─────────┐
                                    │ N       │
                            ┌───────▼──────────┴────────┐
                            │    PhoneModel            │
                            ├──────────────────────────┤
                            │ id (PK)                  │
                            │ brand_id (FK to Brand)   │
                            │ model_name               │
                            │ launch_date              │
                            │ platform                 │
                            │ storage_options          │
                            │ description              │
                            │ specifications           │
                            │ created_at               │
                            │ updated_at               │
                            └──────────┬───────────────┘
                                       │
                                       │ N (ManyToMany)
                                       │
                    ┌──────────────────┴──────────────────┐
                    │                                     │
                    │  Review_PhoneModel (Junction Table)│
                    │  ├─ review_id (FK)                 │
                    │  └─ phonemodel_id (FK)             │
                    │                                     │
                    └──────────────────┬──────────────────┘
                                       │
                                       │ M
                                       │
                            ┌──────────▼──────────┐
                            │      Review        │
                            ├────────────────────┤
                            │ id (PK)            │
                            │ title              │
                            │ content            │
                            │ rating (1-5)       │
                            │ author_id (FK)     │
                            │ date_published     │
                            │ updated_at         │
                            │ is_active          │
                            └──────────┬─────────┘
                                       │
                                       │ 1
                                       │
                    ┌──────────────────┼──────────────────┐
                    │                  │                  │
                    │                  │            ┌─────▼─────────────┐
                    │                  │            │ ReviewResource    │
                    │                  │            ├───────────────────┤
                    │                  │            │ id (PK)           │
                    │                  │            │ review_id (FK)    │
                    │                  │            │ title             │
                    │                  │            │ url               │
                    │                  │            │ description       │
                    │                  │            │ created_at        │
                    │                  │            └───────────────────┘
                    │                  │
                    │            ┌─────▼──────────────┐
                    │            │  Django User       │
                    │            │  (auth.User)       │
                    │            ├────────────────────┤
                    │            │ id (PK)            │
                    │            │ username           │
                    │            │ email              │
                    │            │ first_name         │
                    │            │ last_name          │
                    │            │ password           │
                    │            │ is_staff           │
                    │            │ is_superuser       │
                    │            │ date_joined        │
                    │            │ last_login         │
                    │            └────────────────────┘
                    │
                    └─── One User → Many Reviews

```

## Relationship Flows

### Foreign Key Relationships (1:N)
```
Brand (1) ──────────────────────> (N) PhoneModel
  "One brand has many models"

User (1) ──────────────────────> (N) Review
  "One user writes many reviews"

Review (1) ──────────────────────> (N) ReviewResource
  "One review has many resources/links"
```

### Many-to-Many Relationship (N:N)
```
Review (N) ──┐
             ├──────[Junction Table]──────────> PhoneModel (N)
             │   review_phonemodel           
             │   ├─ review_id
             │   └─ phonemodel_id
             │
"Many reviews can cover many phone models"
"Many phone models can be reviewed in many reviews"
```

## Application Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         Django Application                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│   ┌──────────────────────────────────────────────────────────────┐    │
│   │                    URL Routing Layer                         │    │
│   ├──────────────────────────────────────────────────────────────┤    │
│   │                                                              │    │
│   │  phoneRadar/urls.py                                          │    │
│   │  ├─ /admin/              ───> Django Admin                   │    │
│   │  └─ /                    ───> include('main.urls')           │    │
│   │                                                              │    │
│   │  main/urls.py                                               │    │
│   │  └─ /index               ───> main.views.index              │    │
│   │                                                              │    │
│   │  PhoneReview/urls.py (To be developed)                       │    │
│   │  ├─ /phones/             ───> phone list view                │    │
│   │  ├─ /phones/<id>/        ───> phone detail view              │    │
│   │  ├─ /reviews/            ───> review list view               │    │
│   │  ├─ /reviews/<id>/       ───> review detail view             │    │
│   │  └─ /reviews/add/        ───> add review view                │    │
│   │                                                              │    │
│   └──────────────────────────────────────────────────────────────┘    │
│                                                                         │
│   ┌──────────────────────────────────────────────────────────────┐    │
│   │                    Views/Logic Layer                         │    │
│   ├──────────────────────────────────────────────────────────────┤    │
│   │                                                              │    │
│   │  main/views.py:                                              │    │
│   │  └─ index(request) ──> renders main page                     │    │
│   │                                                              │    │
│   │  PhoneReview/views.py (To be developed):                     │    │
│   │  ├─ phone_list(request)                                      │    │
│   │  ├─ phone_detail(request, id)                                │    │
│   │  ├─ review_list(request)                                     │    │
│   │  ├─ review_detail(request, id)                               │    │
│   │  └─ add_review(request)                                      │    │
│   │                                                              │    │
│   └──────────────────────────────────────────────────────────────┘    │
│                                                                         │
│   ┌──────────────────────────────────────────────────────────────┐    │
│   │                    Models/ORM Layer                          │    │
│   ├──────────────────────────────────────────────────────────────┤    │
│   │                                                              │    │
│   │  PhoneReview/models.py:                                      │    │
│   │  ├─ Brand                                                    │    │
│   │  ├─ PhoneModel                                               │    │
│   │  ├─ Review                                                   │    │
│   │  └─ ReviewResource                                           │    │
│   │                                                              │    │
│   │  Django Auth (User, Group, Permission)                       │    │
│   │                                                              │    │
│   └──────────────────────────────────────────────────────────────┘    │
│                                                                         │
│   ┌──────────────────────────────────────────────────────────────┐    │
│   │                 Admin Interface Layer                        │    │
│   ├──────────────────────────────────────────────────────────────┤    │
│   │                                                              │    │
│   │  PhoneReview/admin.py:                                       │    │
│   │  ├─ BrandAdmin                                               │    │
│   │  ├─ PhoneModelAdmin                                          │    │
│   │  ├─ ReviewAdmin                                              │    │
│   │  ├─ ReviewResourceAdmin                                      │    │
│   │  └─ ReviewResourceInline                                     │    │
│   │                                                              │    │
│   └──────────────────────────────────────────────────────────────┘    │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
                                   │
                                   │
                                   ▼
                        ┌──────────────────────┐
                        │   SQLite Database    │
                        │   (db.sqlite3)       │
                        ├──────────────────────┤
                        │ Brand Table          │
                        │ PhoneModel Table     │
                        │ Review Table         │
                        │ ReviewResource Table │
                        │ Junction Table (M2M) │
                        │ User Table           │
                        │ ... (other tables)   │
                        └──────────────────────┘
```

## Request/Response Flow

### Example: View Phone Reviews

```
1. User Request
   └─> GET http://127.0.0.1:8000/phones/

2. Django URL Routing
   └─> phoneRadar/urls.py
       └─> main/urls.py OR PhoneReview/urls.py
           └─> Matches pattern, routes to view

3. View Execution
   └─> PhoneReview/views.py::phone_list()
       ├─> Query database for PhoneModel objects
       │   └─> ORM translates to SQL
       │       └─> SELECT * FROM PhoneReview_phonemodel
       │
       ├─> Get related Brand info via ForeignKey
       │   └─> For each phone, fetch Brand details
       │
       ├─> Count related Reviews via M2M
       │   └─> Get all reviews linked to each phone
       │
       └─> Render template with data
           └─> templates/phones/list.html

4. Database Query
   └─> SQLite executes SQL
       └─> Returns PhoneModel records with relations

5. Response Generation
   └─> Template renders HTML with phone data
       └─> HTTP Response with rendered HTML

6. Client Receives
   └─> Browser renders HTML page
       └─> User sees phone list
```

## Data Flow Example: Adding a Review

```
Step 1: User Inputs
┌─────────────────────┐
│ Review Form         │
├─────────────────────┤
│ Title: "Great!"     │
│ Content: "..."      │
│ Rating: 5           │
│ Models: [iPhone15]  │
│ Resources: [URL1]   │
└────────┬────────────┘
         │
         ▼
Step 2: POST Request
        POST /reviews/add/
        + Form Data + User Session

         │
         ▼
Step 3: Django View
        ├─ Validates form data
        ├─ Gets current user from session
        ├─ Creates Review instance
        │  └─ Sets author = request.user
        ├─ Saves Review to database
        ├─ Adds M2M relationships
        │  └─ Links selected PhoneModels
        ├─ Creates ReviewResource instances
        │  └─ Links resources to Review
        └─ Saves to database

         │
         ▼
Step 4: Database Operations
        ├─ INSERT Review
        │  INTO PhoneReview_review
        │  (title, content, rating, author_id, ...)
        │
        ├─ INSERT Review_PhoneModel
        │  INTO PhoneReview_review_phonemodels
        │  (review_id, phonemodel_id)
        │
        └─ INSERT ReviewResource
           INTO PhoneReview_reviewresource
           (review_id, title, url, ...)

         │
         ▼
Step 5: Response
        ├─ Redirect to review detail page
        ├─ Display success message
        └─ Show newly created review

         │
         ▼
Step 6: Database Verification
        SELECT * FROM PhoneReview_review WHERE id = ?
        └─ Returns newly created review with all relations
```

## Query Examples

### Get all phones for a brand
```python
brand = Brand.objects.get(name="Apple")
phones = brand.phone_models.all()
```

SQL Translation:
```sql
SELECT * FROM PhoneReview_phonemodel 
WHERE brand_id = (SELECT id FROM PhoneReview_brand WHERE name = 'Apple')
```

### Get all reviews for a phone model
```python
phone = PhoneModel.objects.get(model_name="iPhone 15 Pro")
reviews = phone.reviews.all()
```

SQL Translation:
```sql
SELECT r.* FROM PhoneReview_review r
JOIN PhoneReview_review_phonemodels rp ON r.id = rp.review_id
WHERE rp.phonemodel_id = (SELECT id FROM PhoneReview_phonemodel WHERE model_name = 'iPhone 15 Pro')
```

### Get all reviews by a user
```python
user = User.objects.get(username="john")
reviews = user.reviews.all()
```

SQL Translation:
```sql
SELECT * FROM PhoneReview_review 
WHERE author_id = (SELECT id FROM auth_user WHERE username = 'john')
```

### Get resources for a review
```python
review = Review.objects.get(id=1)
resources = review.resources.all()
```

SQL Translation:
```sql
SELECT * FROM PhoneReview_reviewresource 
WHERE review_id = 1
```

---

## Tables Summary

| Table | Records | Purpose |
|-------|---------|---------|
| Brand | N | Phone manufacturers |
| PhoneModel | N | Phone models from brands |
| Review | N | Review articles |
| ReviewResource | N | Links/resources for reviews |
| Review_PhoneModel | N*M | Many-to-many relationships |
| User | N | Users registered on site |
| Session | N | User session data |
| Admin | N | Django admin log entries |

---

**Generated**: March 29, 2026
**Diagram Type**: Database & Architecture Schema
**Status**: Complete & Ready for Reference

