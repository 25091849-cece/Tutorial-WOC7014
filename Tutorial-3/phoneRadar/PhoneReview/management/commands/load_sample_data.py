from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from PhoneReview.models import Brand, PhoneModel, Review, ReviewResource


class Command(BaseCommand):
    help = 'Load sample data into the Phone Radar database'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🔄 Loading sample data...'))

        # Create a sample user if not exists
        user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@phoneradar.com',
                'first_name': 'Admin',
                'last_name': 'User',
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            user.set_password('admin123')
            user.save()
            self.stdout.write(self.style.SUCCESS('✅ Created admin user'))
        else:
            self.stdout.write('ℹ️  Admin user already exists')

        # Create test user
        test_user, created = User.objects.get_or_create(
            username='reviewer',
            defaults={
                'email': 'reviewer@phoneradar.com',
                'first_name': 'John',
                'last_name': 'Reviewer'
            }
        )
        if created:
            test_user.set_password('reviewer123')
            test_user.save()
            self.stdout.write(self.style.SUCCESS('✅ Created test user'))

        # Create Brands
        self.stdout.write('\n📱 Creating Brands...')
        brands_data = [
            {
                'name': 'Apple',
                'origin_country': 'United States',
                'manufacturing_since': 1976,
                'website_url': 'https://www.apple.com',
                'description': 'Apple Inc. is an American technology company that designs and manufactures consumer electronics.'
            },
            {
                'name': 'Samsung',
                'origin_country': 'South Korea',
                'manufacturing_since': 1938,
                'website_url': 'https://www.samsung.com',
                'description': 'Samsung Electronics is a South Korean multinational electronics company.'
            },
            {
                'name': 'Google',
                'origin_country': 'United States',
                'manufacturing_since': 1998,
                'website_url': 'https://www.google.com',
                'description': 'Google LLC is an American multinational technology company specializing in internet-related services and products.'
            },
            {
                'name': 'OnePlus',
                'origin_country': 'China',
                'manufacturing_since': 2013,
                'website_url': 'https://www.oneplus.com',
                'description': 'OnePlus is a Chinese smartphone manufacturer known for premium devices at affordable prices.'
            },
            {
                'name': 'Xiaomi',
                'origin_country': 'China',
                'manufacturing_since': 2010,
                'website_url': 'https://www.mi.com',
                'description': 'Xiaomi is a Chinese electronics company known for affordable yet feature-rich smartphones.'
            }
        ]

        brands = {}
        for brand_data in brands_data:
            brand, created = Brand.objects.get_or_create(
                name=brand_data['name'],
                defaults=brand_data
            )
            brands[brand.name] = brand
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✅ Created: {brand.name}'))
            else:
                self.stdout.write(f'  ℹ️  {brand.name} already exists')

        # Create Phone Models
        self.stdout.write('\n📱 Creating Phone Models...')
        models_data = [
            {
                'brand': 'Apple',
                'model_name': 'iPhone 15 Pro Max',
                'launch_date': '2023-09-22',
                'platform': 'iOS',
                'storage_options': '256GB, 512GB, 1TB',
                'description': 'Premium flagship smartphone with advanced camera system and A17 Pro chip',
                'specifications': 'A17 Pro Chip, 48MP Main Camera, ProMotion Display, USB-C, Action Button'
            },
            {
                'brand': 'Apple',
                'model_name': 'iPhone 15',
                'launch_date': '2023-09-22',
                'platform': 'iOS',
                'storage_options': '128GB, 256GB, 512GB',
                'description': 'Standard flagship iPhone with modern features',
                'specifications': 'A16 Bionic Chip, Dual Camera, Dynamic Island, USB-C'
            },
            {
                'brand': 'Samsung',
                'model_name': 'Galaxy S24 Ultra',
                'launch_date': '2024-01-31',
                'platform': 'Android',
                'storage_options': '256GB, 512GB, 1TB',
                'description': 'Premium Android flagship with S Pen and advanced AI features',
                'specifications': 'Snapdragon 8 Gen 3, 200MP Camera, 120Hz Display, IP68 Rating'
            },
            {
                'brand': 'Samsung',
                'model_name': 'Galaxy S24',
                'launch_date': '2024-01-31',
                'platform': 'Android',
                'storage_options': '256GB, 512GB',
                'description': 'Excellent mid-range flagship from Samsung',
                'specifications': 'Snapdragon 8 Gen 3, 50MP Main Camera, 120Hz AMOLED Display'
            },
            {
                'brand': 'Google',
                'model_name': 'Pixel 8 Pro',
                'launch_date': '2023-10-04',
                'platform': 'Android',
                'storage_options': '128GB, 256GB, 512GB',
                'description': 'Google\'s flagship with advanced computational photography',
                'specifications': 'Google Tensor G3, Advanced AI, 50MP Camera, 120Hz Display'
            },
            {
                'brand': 'Google',
                'model_name': 'Pixel 8',
                'launch_date': '2023-10-04',
                'platform': 'Android',
                'storage_options': '128GB, 256GB',
                'description': 'Standard Pixel phone with excellent camera performance',
                'specifications': 'Google Tensor G3, 50MP Camera, OLED Display, 7 Years of Updates'
            },
            {
                'brand': 'OnePlus',
                'model_name': '12',
                'launch_date': '2023-12-05',
                'platform': 'Android',
                'storage_options': '256GB, 512GB',
                'description': 'Fast and smooth Android flagship at competitive price',
                'specifications': 'Snapdragon 8 Gen 3, AMOLED Display, 50MP Camera, OxygenOS'
            },
            {
                'brand': 'Xiaomi',
                'model_name': '14 Ultra',
                'launch_date': '2024-02-25',
                'platform': 'Android',
                'storage_options': '512GB, 1TB',
                'description': 'Premium Xiaomi with Leica camera partnership',
                'specifications': 'Snapdragon 8 Gen 3, Leica Camera, 120Hz Display, IP68 Rating'
            }
        ]

        phone_models = {}
        for model_data in models_data:
            brand = brands[model_data.pop('brand')]
            model, created = PhoneModel.objects.get_or_create(
                brand=brand,
                model_name=model_data['model_name'],
                defaults=model_data
            )
            phone_models[f"{brand.name} {model.model_name}"] = model
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✅ Created: {brand.name} {model.model_name}'))
            else:
                self.stdout.write(f'  ℹ️  {brand.name} {model.model_name} already exists')

        # Create Reviews
        self.stdout.write('\n⭐ Creating Reviews...')
        reviews_data = [
            {
                'title': 'iPhone 15 Pro Max - Exceptional Performance',
                'content': 'The iPhone 15 Pro Max is an exceptional smartphone with incredible performance and camera capabilities. The A17 Pro chip handles everything effortlessly, and the camera system is outstanding. The ProMotion display is incredibly smooth. Highly recommended for anyone wanting a premium experience.',
                'rating': 5,
                'author': user,
                'models': ['Apple iPhone 15 Pro Max'],
                'is_active': True
            },
            {
                'title': 'Samsung Galaxy S24 Ultra - Best Android Phone',
                'content': 'The Galaxy S24 Ultra is an absolute powerhouse. With the Snapdragon 8 Gen 3, it provides blazing-fast performance. The 200MP camera is incredible and takes stunning photos. The S Pen is a great addition for productivity. This is the best Android phone available right now.',
                'rating': 5,
                'author': test_user,
                'models': ['Samsung Galaxy S24 Ultra'],
                'is_active': True
            },
            {
                'title': 'Google Pixel 8 Pro - Best Camera Phone',
                'content': 'The Pixel 8 Pro has the best computational photography system I\'ve ever used. The Night Sight mode is incredible, and the Magic Eraser feature actually works. Despite being slightly more expensive, the software experience and camera justify the cost. A must-have for photography enthusiasts.',
                'rating': 5,
                'author': user,
                'models': ['Google Pixel 8 Pro'],
                'is_active': True
            },
            {
                'title': 'OnePlus 12 - Great Value Flagship',
                'content': 'OnePlus 12 offers flagship performance at a reasonable price. The Snapdragon 8 Gen 3 delivers smooth performance, and OxygenOS is clean and fast. Battery life is solid, and charging is quick. If you want a powerful phone without breaking the bank, this is it.',
                'rating': 4,
                'author': test_user,
                'models': ['OnePlus 12'],
                'is_active': True
            },
            {
                'title': 'iPhone 15 vs Galaxy S24 - Detailed Comparison',
                'content': 'I\'ve been comparing these two flagships for weeks. Both are excellent, but for different reasons. The iPhone 15 offers superior software optimization and ecosystem integration. The Galaxy S24 Ultra provides more customization and feature richness. Choose based on whether you prefer iOS or Android.',
                'rating': 4,
                'author': user,
                'models': ['Apple iPhone 15', 'Samsung Galaxy S24'],
                'is_active': True
            },
            {
                'title': 'Budget Phone Comparison - Xiaomi 14 Ultra',
                'content': 'The Xiaomi 14 Ultra delivers premium features at a mid-range price. The Leica camera system is fantastic, and the build quality is excellent. Performance is smooth thanks to the Snapdragon 8 Gen 3. A great option if you want flagship features without flagship prices.',
                'rating': 4,
                'author': test_user,
                'models': ['Xiaomi 14 Ultra'],
                'is_active': True
            },
            {
                'title': 'Google Pixel 8 - Best Value Flagship',
                'content': 'The standard Pixel 8 is an excellent choice. While not as feature-packed as the Pro, it still has a great camera and the latest Google Tensor chip. The promise of 7 years of software updates is a game-changer. Great value for the price.',
                'rating': 4,
                'author': user,
                'models': ['Google Pixel 8'],
                'is_active': True
            },
            {
                'title': 'Samsung Galaxy S24 - Solid Mid-Range Option',
                'content': 'The Galaxy S24 is a well-balanced phone. It has most of the features of the Ultra but at a lower price. Camera is great, performance is excellent, and the design is premium. A solid choice for those who don\'t need the S Pen or the Ultra camera setup.',
                'rating': 4,
                'author': test_user,
                'models': ['Samsung Galaxy S24'],
                'is_active': True
            }
        ]

        reviews = []
        for review_data in reviews_data:
            models = review_data.pop('models')
            review, created = Review.objects.get_or_create(
                title=review_data['title'],
                author=review_data['author'],
                defaults=review_data
            )
            
            # Add phone models to the review
            for model_name in models:
                phone_model = phone_models.get(model_name)
                if phone_model:
                    review.phone_models.add(phone_model)
            
            reviews.append(review)
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✅ Created: {review.title}'))
            else:
                self.stdout.write(f'  ℹ️  Review "{review.title}" already exists')

        # Create Review Resources
        self.stdout.write('\n🔗 Creating Review Resources...')
        resources_data = [
            {
                'review_title': 'iPhone 15 Pro Max - Exceptional Performance',
                'resources': [
                    {
                        'title': 'Apple iPhone 15 Pro Max Official Specs',
                        'url': 'https://www.apple.com/iphone-15-pro/specs/',
                        'description': 'Official specifications from Apple'
                    },
                    {
                        'title': 'iPhone 15 Pro Max Review on GSMArena',
                        'url': 'https://www.gsmarena.com/apple_iphone_15_pro_max-12055.php',
                        'description': 'Detailed technical review'
                    }
                ]
            },
            {
                'review_title': 'Samsung Galaxy S24 Ultra - Best Android Phone',
                'resources': [
                    {
                        'title': 'Samsung Galaxy S24 Ultra Specs',
                        'url': 'https://www.samsung.com/us/smartphones/galaxy-s24-ultra/specs/',
                        'description': 'Official Samsung specifications'
                    },
                    {
                        'title': 'S24 Ultra Camera Comparison',
                        'url': 'https://www.gsmarena.com/samsung_galaxy_s24_ultra-12103.php',
                        'description': 'Camera and performance analysis'
                    }
                ]
            },
            {
                'review_title': 'Google Pixel 8 Pro - Best Camera Phone',
                'resources': [
                    {
                        'title': 'Pixel 8 Pro Official Page',
                        'url': 'https://store.google.com/us/product/pixel_8_pro_specs/',
                        'description': 'Google\'s official Pixel 8 Pro page'
                    },
                    {
                        'title': 'Photography Comparison',
                        'url': 'https://www.dxomark.com/google-pixel-8-pro/',
                        'description': 'Expert camera comparison'
                    }
                ]
            },
            {
                'review_title': 'OnePlus 12 - Great Value Flagship',
                'resources': [
                    {
                        'title': 'OnePlus 12 Specifications',
                        'url': 'https://www.oneplus.com/12/specs',
                        'description': 'Full OnePlus 12 specifications'
                    }
                ]
            }
        ]

        for resource_group in resources_data:
            review_title = resource_group['review_title']
            review = Review.objects.filter(title=review_title).first()
            
            if review:
                for resource_data in resource_group['resources']:
                    resource, created = ReviewResource.objects.get_or_create(
                        review=review,
                        title=resource_data['title'],
                        defaults=resource_data
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f'  ✅ Created resource: {resource.title}'))
                    else:
                        self.stdout.write(f'  ℹ️  Resource "{resource.title}" already exists')

        self.stdout.write(self.style.SUCCESS('\n✅ Sample data loaded successfully!'))
        self.stdout.write(self.style.WARNING('\n📊 Summary:'))
        self.stdout.write(f'   • Brands: {Brand.objects.count()}')
        self.stdout.write(f'   • Phone Models: {PhoneModel.objects.count()}')
        self.stdout.write(f'   • Reviews: {Review.objects.count()}')
        self.stdout.write(f'   • Resources: {ReviewResource.objects.count()}')
        self.stdout.write(f'   • Users: {User.objects.count()}')

