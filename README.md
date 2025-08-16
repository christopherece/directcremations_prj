# Direct Cremation | Funeral Services Website

A modern, compassionate funeral services website built with Django and Materialize CSS. This website provides a professional platform for funeral homes to showcase their services, manage obituaries, and support families during difficult times.

## Features

### 🌟 Core Features
- **Homepage** with hero section, action boxes, and testimonials
- **Obituaries** with search, filtering, and tribute messages
- **Service Planning** guides and information
- **Arrange a Service** form with email notifications
- **Farewell Calculator** for cost estimation
- **Contact** page with form and business information
- **Admin Panel** for managing all content

### 🎨 Design
- **Theme**: Gold (#D4AF37) and Black (#000000) color scheme
- **Framework**: Materialize CSS for modern, responsive design
- **Typography**: Lora and Montserrat fonts
- **Mobile-first**: Fully responsive design
- **Professional**: Elegant and compassionate tone

### 🛠 Technical Stack
- **Backend**: Django 4.2+
- **Frontend**: Materialize CSS, HTML5, JavaScript
- **Database**: SQLite (development) / PostgreSQL (production)
- **Forms**: Django Forms with validation
- **Media**: Local storage (configurable for S3)

## Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Setup Instructions

1. **Clone or download the project**
   ```bash
   cd funeralsite_prj
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the website**
   - Website: http://127.0.0.1:8000/
   - Admin Panel: http://127.0.0.1:8000/admin/

## Django Models

### Obituary
Stores information about deceased individuals and their services.

### TributeMessage
Manages tribute messages from visitors (with approval system).

### ServicePackage
Defines different funeral service packages and pricing.

### ServiceExtra
Additional services that can be added to packages.

### PrePlanSubmission
Handles service arrangement requests from families.

### ContactMessage
Stores contact form submissions.

### Testimonial
Manages customer testimonials and reviews.

## Admin Features

### Content Management
- **Obituaries**: Add, edit, and manage obituary listings
- **Tributes**: Approve or reject tribute messages
- **Services**: Manage service packages and pricing
- **Messages**: View and respond to contact submissions
- **Testimonials**: Feature testimonials on the homepage

### Bulk Actions
- Approve/unapprove tribute messages
- Mark submissions as processed
- Feature/unfeature testimonials
- Mark messages as read

## Pages & URLs

- `/` - Homepage
- `/obituaries/` - Obituaries listing
- `/obituary/<id>/` - Individual obituary page
- `/funeral-planning/` - Planning guides
- `/arrange-service/` - Service arrangement form
- `/farewell-calculator/` - Cost calculator
- `/contact/` - Contact page
- `/about/` - About us page
- `/our-approach/` - Our approach page
- `/admin/` - Admin panel

## Customization

### Colors
Update the CSS variables in `templates/base.html`:
```css
:root {
    --gold: #D4AF37;
    --black: #000000;
    --dark-gray: #333333;
    --light-gray: #f5f5f5;
    --white: #ffffff;
}
```

### Email Configuration
Update email settings in `settings.py` for production:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your-smtp-server.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@domain.com'
EMAIL_HOST_PASSWORD = 'your-password'
```

### Media Storage
For production, configure S3 storage in `settings.py`:
```python
# Add django-storages to requirements.txt
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = 'your-access-key'
AWS_SECRET_ACCESS_KEY = 'your-secret-key'
AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
```

## Deployment

### Environment Variables
Create a `.env` file for production settings:
```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=your-database-url
EMAIL_HOST=your-smtp-server
EMAIL_HOST_USER=your-email
EMAIL_HOST_PASSWORD=your-password
```

### Production Checklist
- [ ] Set `DEBUG = False`
- [ ] Configure proper database (PostgreSQL)
- [ ] Set up email backend
- [ ] Configure static file serving
- [ ] Set up media file storage
- [ ] Configure HTTPS
- [ ] Set up monitoring and logging

### Deployment Platforms
This project is ready for deployment on:
- **Render** (recommended)
- **DigitalOcean App Platform**
- **Railway**
- **Heroku**
- **AWS Elastic Beanstalk**

## Support

For questions or support:
- Review the Django documentation
- Check the Materialize CSS documentation
- Contact the development team

## License

This project is created for educational and commercial use. Please ensure you have proper licensing for any production deployment.

---

*Built with compassion and care for families during their most difficult times.*
