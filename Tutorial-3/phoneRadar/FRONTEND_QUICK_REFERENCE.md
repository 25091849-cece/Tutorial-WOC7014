# Frontend Pages Quick Reference

## File Structure
```
phoneRadar/
├── templates/
│   ├── base.html                  # Main layout template
│   ├── home.html                  # Home page
│   ├── phone_list.html            # Browse phones
│   ├── phone_detail.html          # Phone details & reviews
│   ├── add_review.html            # Write new review
│   ├── edit_review.html           # Edit existing review
│   ├── register.html              # User registration
│   ├── login.html                 # User login
│   ├── user_profile.html          # User profile
│   ├── edit_profile.html          # Edit profile
│   └── change_password.html       # Change password
├── main/
│   ├── views.py                   # Updated with all views
│   ├── urls.py                    # Updated with all routes
│   └── ...
└── ...
```

## Page Summary

| Page | URL | Required Auth | Purpose |
|------|-----|---------------|---------|
| Home | `/` | No | Welcome page with latest reviews |
| Phone List | `/phones/` | No | Browse all phones |
| Phone Detail | `/phones/<id>/` | No | View phone & reviews |
| Add Review | `/reviews/add/` | Yes | Create new review |
| Edit Review | `/reviews/<id>/edit/` | Yes* | Edit own review |
| Delete Review | `/reviews/<id>/delete/` | Yes* | Delete own review |
| Register | `/register/` | No | Create account |
| Login | `/login/` | No | Login to account |
| Logout | `/logout/` | Yes | Logout from account |
| User Profile | `/profile/` | Yes | View user profile |
| Edit Profile | `/profile/edit/` | Yes | Edit user info |
| Change Password | `/profile/change-password/` | Yes | Change password |

*Author or admin only

## Color Palette

- **Primary**: #667eea (Purple Blue)
- **Secondary**: #764ba2 (Dark Purple)
- **Success**: #27ae60 (Green)
- **Error**: #e74c3c (Red)
- **Warning**: #f39c12 (Orange)
- **Info**: #3498db (Blue)
- **Background**: #f5f5f5 (Light Gray)
- **Text**: #333 (Dark Gray)

## Component Classes

### Buttons
```html
<!-- Primary Button -->
<a href="#" class="btn btn-primary">Click Me</a>

<!-- Secondary Button -->
<a href="#" class="btn btn-secondary">Click Me</a>

<!-- Large Button -->
<button class="btn btn-primary btn-lg">Large Button</button>
```

### Cards
```html
<div class="card">
    <div class="card-header">Header</div>
    <div class="card-body">Content</div>
    <div class="card-footer">Footer</div>
</div>
```

### Forms
```html
<div class="form-group">
    <label>Label:</label>
    <input type="text" required>
    <div class="error-message">Error text</div>
</div>
```

### Ratings
```html
<div class="rating">
    ★★★★☆
    <span class="rating-count">4/5</span>
</div>
```

## Template Features

### Responsive Grid
- Auto-fit grid layout (min 300px cards)
- Mobile-first design
- Flexbox-based for alignment

### Navigation
- Sticky header
- User status display
- Conditional login/logout links
- Logo links to home

### Message Display
```html
{% if messages %}
    {% for message in messages %}
        <div class="success-message">{{ message }}</div>
    {% endfor %}
{% endif %}
```

### User Authentication Display
```html
{% if user.is_authenticated %}
    <!-- Show for logged-in users -->
{% else %}
    <!-- Show for guests -->
{% endif %}
```

### Conditional Permissions
```html
{% if user.is_authenticated and user == review.author or user.is_staff %}
    <!-- Show edit/delete buttons -->
{% endif %}
```

## Key Template Tags Used

- `{% extends 'base.html' %}` - Inherit from base template
- `{% block content %}...{% endblock %}` - Content block
- `{% url 'name' %}` - Generate URLs from route names
- `{% if %}...{% endif %}` - Conditionals
- `{% for %}...{% endfor %}` - Loops
- `{{ variable }}` - Display variables
- `|truncatewords:N` - Truncate text
- `|date:"format" %}` - Format dates
- `|length` - Get length
- `|pluralize` - Plural forms
- `{% csrf_token %}` - CSRF protection
- `{% load tags %}` - Load custom filters/tags

## Styling Approach

All CSS is embedded in `base.html` within `<style>` tags for simplicity:
- Mobile-first responsive design
- CSS Grid and Flexbox
- CSS variables and gradients
- Smooth transitions and animations

## JavaScript Included

### Review Form
- Dynamic star rating display
- Character counter
- Add/remove resource fields
- Form validation

### Profile
- Form submission handling
- Confirm dialogs for delete

## Accessibility Features

- Semantic HTML structure
- Form labels linked to inputs
- Color contrast compliance
- Keyboard navigation support
- Skip navigation links (optional)

## Browser Compatibility

Tested and compatible with:
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers

## Performance Optimizations

- Minimal external dependencies
- Embedded CSS (no HTTP requests)
- Optimized images (using emoji instead)
- Lazy loading for reviews
- Efficient template inheritance

## Common Issues & Solutions

### Issue: CSS not loading
**Solution**: Verify `base.html` is in `templates/` folder and `DIRS` in settings.py is correct

### Issue: URLs not found
**Solution**: Check `main/urls.py` has all routes and `phoneRadar/urls.py` includes them

### Issue: Templates not rendering
**Solution**: Verify `INSTALLED_APPS` in settings.py includes `'main'` and `'PhoneReview'`

### Issue: Static files (images, CSS)
**Solution**: For production, configure Django static files system

### Issue: Login redirects not working
**Solution**: Ensure `login_url='login'` in `@login_required` decorator matches URL name

## Testing the Frontend

### Basic Flow
1. Visit `http://localhost:8000` → Home page
2. Click "Register" → Create account
3. Login with new account
4. Browse phones
5. Click phone → See details
6. Click "Write Review" → Add review
7. View profile → See your review
8. Edit/delete review
9. Logout

### Admin Testing
1. Access Django admin: `http://localhost:8000/admin/`
2. Add brands and phones
3. View and moderate reviews
4. Create sample data

## Customization Tips

### Change Colors
- Find color hex in `base.html` `<style>` section
- Replace all instances of color code
- Update gradient backgrounds

### Modify Navigation
- Edit `<nav>` section in `base.html`
- Add/remove menu items
- Update conditional links

### Add/Remove Fields
- Update form templates
- Modify view POST handling
- Update model validators

### Adjust Layout
- Change grid columns in CSS
- Modify padding/margins
- Update card widths

## Future Enhancements

See `FRONTEND_IMPLEMENTATION.md` for detailed roadmap and next steps.

