from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from PhoneReview.models import Brand, PhoneModel, Review, ReviewResource

def index(request):
    """Home page view - Display latest reviews and popular brands"""
    latest_reviews = Review.objects.filter(is_active=True).order_by('-date_published')[:6]
    brands = Brand.objects.all()[:8]
    
    context = {
        'latest_reviews': latest_reviews,
        'brands': brands,
    }
    return render(request, 'home.html', context)


def phone_list(request):
    """Display all phones with filtering by brand"""
    phone_models = PhoneModel.objects.all()
    all_brands = Brand.objects.all()
    
    # Filter by brand if specified
    brand_id = request.GET.get('brand')
    if brand_id:
        phone_models = phone_models.filter(brand_id=brand_id)
    
    context = {
        'phone_models': phone_models,
        'all_brands': all_brands,
    }
    return render(request, 'phone_list.html', context)


def phone_detail(request, phone_id):
    """Display detailed information about a specific phone and its reviews"""
    phone = get_object_or_404(PhoneModel, id=phone_id)
    
    context = {
        'phone': phone,
    }
    return render(request, 'phone_detail.html', context)


def review_detail(request, review_id):
    """Display full review details (redirect to phone detail page with review)"""
    review = get_object_or_404(Review, id=review_id, is_active=True)
    phone = review.phone_models.first()
    
    if phone:
        return redirect('phone_detail', phone_id=phone.id)
    return redirect('home')


@login_required(login_url='login')
def add_review(request):
    """Add a new review - general page"""
    if request.method == 'POST':
        phone_model_id = request.POST.get('phone_models')
        title = request.POST.get('title')
        content = request.POST.get('content')
        rating = request.POST.get('rating')
        
        if not all([phone_model_id, title, content, rating]):
            messages.error(request, 'Please fill in all required fields.')
            phone_models = PhoneModel.objects.all()
            return render(request, 'add_review.html', {'phone_models': phone_models})
        
        try:
            phone_model = PhoneModel.objects.get(id=phone_model_id)
            review = Review.objects.create(
                title=title,
                content=content,
                rating=int(rating),
                author=request.user
            )
            review.phone_models.add(phone_model)
            
            # Add resources if provided
            resource_titles = request.POST.getlist('resource_title')
            resource_urls = request.POST.getlist('resource_url')
            
            for title, url in zip(resource_titles, resource_urls):
                if title and url:
                    ReviewResource.objects.create(
                        review=review,
                        title=title,
                        url=url
                    )
            
            messages.success(request, 'Review submitted successfully!')
            return redirect('phone_detail', phone_id=phone_model.id)
        except Exception as e:
            messages.error(request, f'Error creating review: {str(e)}')
    
    phone_models = PhoneModel.objects.all()
    context = {'phone_models': phone_models}
    return render(request, 'add_review.html', context)


@login_required(login_url='login')
def add_review_for_phone(request, phone_id):
    """Add a review for a specific phone"""
    phone = get_object_or_404(PhoneModel, id=phone_id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        rating = request.POST.get('rating')
        
        if not all([title, content, rating]):
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'add_review.html', {'phone_models': [phone]})
        
        try:
            review = Review.objects.create(
                title=title,
                content=content,
                rating=int(rating),
                author=request.user
            )
            review.phone_models.add(phone)
            
            # Add resources if provided
            resource_titles = request.POST.getlist('resource_title')
            resource_urls = request.POST.getlist('resource_url')
            
            for res_title, url in zip(resource_titles, resource_urls):
                if res_title and url:
                    ReviewResource.objects.create(
                        review=review,
                        title=res_title,
                        url=url
                    )
            
            messages.success(request, 'Review submitted successfully!')
            return redirect('phone_detail', phone_id=phone.id)
        except Exception as e:
            messages.error(request, f'Error creating review: {str(e)}')
    
    context = {'phone_models': [phone]}
    return render(request, 'add_review.html', context)


@login_required(login_url='login')
def edit_review(request, review_id):
    """Edit an existing review (author or admin only)"""
    review = get_object_or_404(Review, id=review_id)
    
    # Check if user is author or admin
    if request.user != review.author and not request.user.is_staff:
        messages.error(request, 'You do not have permission to edit this review.')
        return redirect('phone_detail', phone_id=review.phone_models.first().id)
    
    if request.method == 'POST':
        review.title = request.POST.get('title', review.title)
        review.content = request.POST.get('content', review.content)
        review.rating = int(request.POST.get('rating', review.rating))
        review.save()
        
        messages.success(request, 'Review updated successfully!')
        return redirect('phone_detail', phone_id=review.phone_models.first().id)
    
    context = {
        'review': review,
        'phone_models': PhoneModel.objects.all(),
        'is_edit': True
    }
    return render(request, 'edit_review.html', context)


@login_required(login_url='login')
def delete_review(request, review_id):
    """Delete a review (author or admin only)"""
    review = get_object_or_404(Review, id=review_id)
    
    # Check if user is author or admin
    if request.user != review.author and not request.user.is_staff:
        messages.error(request, 'You do not have permission to delete this review.')
        return redirect('phone_detail', phone_id=review.phone_models.first().id)
    
    phone_id = review.phone_models.first().id if review.phone_models.exists() else None
    
    if request.method == 'POST' or request.GET.get('confirm'):
        review.delete()
        messages.success(request, 'Review deleted successfully!')
        if phone_id:
            return redirect('phone_detail', phone_id=phone_id)
        return redirect('home')
    
    return redirect('phone_detail', phone_id=phone_id) if phone_id else redirect('home')


def register(request):
    """User registration view"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        terms = request.POST.get('terms')
        
        # Validation
        errors = []
        
        if not username:
            errors.append('Username is required.')
        elif User.objects.filter(username=username).exists():
            errors.append('Username already exists.')
        
        if not email:
            errors.append('Email is required.')
        elif User.objects.filter(email=email).exists():
            errors.append('Email already registered.')
        
        if not password1:
            errors.append('Password is required.')
        elif len(password1) < 8:
            errors.append('Password must be at least 8 characters.')
        
        if password1 != password2:
            errors.append('Passwords do not match.')
        
        if not terms:
            errors.append('You must agree to the Terms of Service.')
        
        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'register.html')
        
        # Create user
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            messages.success(request, 'Account created successfully! You can now login.')
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
    
    return render(request, 'register.html')


def login_view(request):
    """User login view"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        
        # Try to authenticate with username or email
        user = None
        if '@' in username:  # Assume it's email
            try:
                user_obj = User.objects.get(email=username)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                pass
        else:
            user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if not remember:
                request.session.set_expiry(0)
            messages.success(request, f'Welcome back, {user.username}!')
            next_page = request.GET.get('next', 'home')
            return redirect(next_page)
        else:
            messages.error(request, 'Invalid username/email or password.')
    
    return render(request, 'login.html')


@login_required(login_url='login')
def logout_view(request):
    """User logout view"""
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')


@login_required(login_url='login')
def user_profile(request):
    """User profile view"""
    context = {
        'user': request.user,
    }
    return render(request, 'user_profile.html', context)


@login_required(login_url='login')
def edit_profile(request):
    """Edit user profile view"""
    if request.method == 'POST':
        email = request.POST.get('email')
        
        # Check if email is already used by another user
        if User.objects.filter(email=email).exclude(id=request.user.id).exists():
            messages.error(request, 'This email is already in use.')
            return render(request, 'edit_profile.html')
        
        request.user.email = email
        request.user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('user_profile')
    
    return render(request, 'edit_profile.html')


@login_required(login_url='login')
def change_password(request):
    """Change password view"""
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')
        
        if not request.user.check_password(old_password):
            messages.error(request, 'Old password is incorrect.')
            return render(request, 'change_password.html')
        
        if new_password1 != new_password2:
            messages.error(request, 'New passwords do not match.')
            return render(request, 'change_password.html')
        
        if len(new_password1) < 8:
            messages.error(request, 'Password must be at least 8 characters.')
            return render(request, 'change_password.html')
        
        request.user.set_password(new_password1)
        request.user.save()
        messages.success(request, 'Password changed successfully!')
        return redirect('user_profile')
    
    return render(request, 'change_password.html')
