# Phone Radar Website - Sitemap

## Website Structure

```
Phone Radar (Root)
│
├── Home / Index
│   └── Display list of latest phone reviews
│   └── Navigation links to all sections
│
├── Phone Reviews
│   ├── List Page (/phones)
│   │   └── Browse all phone reviews
│   │   └── Filter by brand
│   │   └── Search functionality
│   │
│   └── Detail Page (/phones/<id>)
│       └── Display phone specifications
│       └── Display associated reviews
│       └── Link to add new review (authenticated users only)
│
├── Brands
│   ├── Brands List Page (/brands)
│   │   └── Display all phone brands
│   │   └── Filter and search
│   │
│   └── Brand Detail Page (/brands/<id>)
│       └── Display brand information
│       └── List all phones from this brand
│
├── Reviews
│   ├── Reviews List Page (/reviews)
│   │   └── Display all reviews
│   │   └── Sort by date, rating
│   │
│   ├── Review Detail Page (/reviews/<id>)
│   │
│   └── Add Review Page (/reviews/add) [Authenticated Users Only]
│       └── Form to create new review
│       └── Link phones to review
│
├── User Authentication
│   ├── Register Page (/register)
│   │   └── User registration form
│   │
│   ├── Login Page (/login)
│   │   └── User login form
│   │
│   └── Logout (/logout)
│       └── Session termination
│
├── User Dashboard (/dashboard) [Authenticated Users Only]
│   ├── My Reviews
│   ├── Add New Phone [Admin/Staff Only]
│   ├── Add New Review
│   └── Edit/Delete My Reviews
│
└── Admin Panel (/admin)
    ├── Manage Brands
    ├── Manage Phone Models
    ├── Manage Reviews
    └── Manage Users

```

## Navigation Flow

### Unauthenticated Users:
- Home → Browse Phones/Reviews → View Details → Login/Register → Contribute

### Authenticated Users:
- Home → Browse Phones/Reviews → View Details → Add Review → Dashboard

### Admin Users:
- Full access to admin panel for managing all content

