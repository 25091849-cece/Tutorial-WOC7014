# Phone Radar Website - Storyboard & User Flows

## User Flow Diagrams

### Flow 1: Visitor/Guest User Journey

```
Start
  ↓
Visit Home Page
  ↓
View List of Phone Reviews
  ↓
Click on Phone Review
  ↓
View Phone Details & Reviews
  ↓
Decision: Want to Add Review?
  ├─ NO → End (Browse only)
  │
  └─ YES
      ↓
      Click "Add Review"
      ↓
      Redirected to Login
      ↓
      No Account?
      ├─ YES → Go to Registration
      │         ↓
      │         Fill Registration Form
      │         ↓
      │         Account Created
      │         ↓
      │         Auto-Login
      │
      └─ NO → Continue to Login
              ↓
              Enter Credentials
              ↓
              Login Successful
              ↓
      (Login/Registration Both Paths Merge Here)
      ↓
      Fill Review Form
      (Select Phone Model, Write Review, Rate)
      ↓
      Submit Review
      ↓
      Review Added Successfully
      ↓
      Redirected to Review Detail Page
      ↓
      End
```

### Flow 2: Admin/Staff User Journey

```
Admin Login
  ↓
Access Admin Dashboard (/admin)
  ↓
Manage Brands
├─ Add New Brand
├─ Edit Brand Info
├─ Delete Brand (if no associated phones)
└─ View All Brands
  ↓
Manage Phone Models
├─ Add New Phone Model
├─ Select Brand
├─ Enter Specifications
├─ Edit Existing Models
└─ View All Models
  ↓
Manage Reviews
├─ View All Reviews
├─ Edit Reviews (if needed)
├─ Delete Inappropriate Reviews
└─ View Review Statistics
  ↓
End
```

### Flow 3: Registered User Dashboard

```
Authenticated User
  ↓
Click Dashboard/Profile
  ↓
View Options:
├─ My Reviews
│  ├─ View all my reviews
│  ├─ Edit my review
│  ├─ Delete my review
│  └─ View review statistics
│
├─ Add New Review
│  ├─ Select Phone/Model
│  ├─ Write Review Content
│  ├─ Add Rating
│  ├─ Add Links/References
│  └─ Submit
│
└─ Settings
   ├─ Update Profile
   └─ Change Password
```

## Storyboard Wireframes

### Page 1: Home Page
```
┌─────────────────────────────────────────────┐
│  PHONE RADAR LOGO  [Search] [Login/Register]│
├─────────────────────────────────────────────┤
│                                             │
│   Welcome to Phone Radar                    │
│   Your Source for Phone Reviews             │
│                                             │
├─────────────────────────────────────────────┤
│  Latest Reviews                             │
├─────────────────────────────────────────────┤
│ ┌─────────────────┐ ┌─────────────────┐    │
│ │ iPhone 15 Pro   │ │ Samsung Galaxy  │    │
│ │ Review Date:... │ │ Review Date:... │    │
│ │ Rating: ★★★★★  │ │ Rating: ★★★★☆  │    │
│ │ [Read More]     │ │ [Read More]     │    │
│ └─────────────────┘ └─────────────────┘    │
│                                             │
│ ┌─────────────────┐ ┌─────────────────┐    │
│ │ Google Pixel... │ │ OnePlus 12...   │    │
│ │ Review Date:... │ │ Review Date:... │    │
│ │ Rating: ★★★★★  │ │ Rating: ★★★★★  │    │
│ │ [Read More]     │ │ [Read More]     │    │
│ └─────────────────┘ └─────────────────┘    │
│                                             │
├─────────────────────────────────────────────┤
│ [Browse All Reviews] [Browse by Brand]      │
└─────────────────────────────────────────────┘
```

### Page 2: Phone List / Browse
```
┌─────────────────────────────────────────────┐
│  PHONE RADAR  [Search] [Filter by Brand]    │
├─────────────────────────────────────────────┤
│  All Phones                                 │
├─────────────────────────────────────────────┤
│ Brand Filter:                               │
│ [All] [Apple] [Samsung] [Google] [OnePlus] │
├─────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────┐ │
│ │ iPhone 15 Pro Max                       │ │
│ │ Brand: Apple | Launch: Sept 2023        │ │
│ │ Platform: iOS | Storage: 256GB-1TB      │ │
│ │ Reviews: 15 | Avg Rating: ★★★★★       │ │
│ │ [View Details] [Write Review]           │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Samsung Galaxy S24 Ultra                │ │
│ │ Brand: Samsung | Launch: Jan 2024       │ │
│ │ Platform: Android | Storage: 256GB-1TB  │ │
│ │ Reviews: 12 | Avg Rating: ★★★★☆       │ │
│ │ [View Details] [Write Review]           │ │
│ └─────────────────────────────────────────┘ │
│                                             │
└─────────────────────────────────────────────┘
```

### Page 3: Phone Detail & Reviews
```
┌─────────────────────────────────────────────┐
│  PHONE RADAR                                │
├─────────────────────────────────────────────┤
│  iPhone 15 Pro Max                          │
├─────────────────────────────────────────────┤
│ Brand: Apple                                │
│ Launch Date: Sept 22, 2023                  │
│ Platform: iOS 17                            │
│ Storage Options: 256GB, 512GB, 1TB          │
│ Avg Rating: ★★★★★ (Based on 15 reviews)   │
│                                             │
│ [Add Review] (Login Required)               │
├─────────────────────────────────────────────┤
│ Reviews:                                    │
├─────────────────────────────────────────────┤
│ ┌─────────────────────────────────────────┐ │
│ │ Author: John Doe | Date: Dec 15, 2023   │ │
│ │ Rating: ★★★★★                          │ │
│ │ "Excellent phone, great camera..."      │ │
│ │ [Read Full] [Like] [Comment]            │ │
│ └─────────────────────────────────────────┘ │
│                                             │
│ ┌─────────────────────────────────────────┐ │
│ │ Author: Jane Smith | Date: Dec 10, 2023 │ │
│ │ Rating: ★★★★☆                          │ │
│ │ "Good phone, battery could be better..." │ │
│ │ [Read Full] [Like] [Comment]            │ │
│ └─────────────────────────────────────────┘ │
└─────────────────────────────────────────────┘
```

### Page 4: User Registration
```
┌─────────────────────────────────────────────┐
│  PHONE RADAR - Register                     │
├─────────────────────────────────────────────┤
│                                             │
│  Create Your Account                        │
│                                             │
│  Username: [________________]               │
│                                             │
│  Email:    [________________]               │
│                                             │
│  Password: [________________]               │
│                                             │
│  Confirm:  [________________]               │
│                                             │
│  [✓] I agree to the Terms of Service       │
│                                             │
│  [Register]  [Already have account? Login] │
│                                             │
└─────────────────────────────────────────────┘
```

### Page 5: Add Review
```
┌─────────────────────────────────────────────┐
│  PHONE RADAR - Write a Review               │
├─────────────────────────────────────────────┤
│                                             │
│  Select Phone Model:                        │
│  [v iPhone 15 Pro Max        ]              │
│                                             │
│  Your Rating:                               │
│  ☆ ☆ ☆ ☆ ☆  (Click to rate)              │
│                                             │
│  Review Title:                              │
│  [________________]                         │
│                                             │
│  Review Content:                            │
│  ┌─────────────────────────────────────┐   │
│  │ Share your detailed thoughts about  │   │
│  │ this phone model...                 │   │
│  │                                     │   │
│  │                                     │   │
│  └─────────────────────────────────────┘   │
│                                             │
│  Related Links/Resources:                   │
│  [+ Add Link]                               │
│                                             │
│  [Submit Review] [Cancel]                  │
│                                             │
└─────────────────────────────────────────────┘
```

## Key Features Summary

1. **Homepage**: Display trending/latest phone reviews with quick access
2. **Browse**: Filter phones by brand, search functionality
3. **Details**: Comprehensive phone specs with associated reviews
4. **Authentication**: Secure login/registration system
5. **User Dashboard**: Manage personal reviews and preferences
6. **Admin Panel**: Full content management capabilities
7. **Responsive Design**: Works on desktop, tablet, and mobile devices

