# My Django Project

## Project Overview
A Django web application with user authentication, dynamic templates, and responsive design 

## Features
Home Page: Customizable landing page with Tailwind CSS styling
Core App: Contains base templates and static files
Production-Ready Setup: Includes .env configuration and .gitignore
Modern Development: Pre-configured with Python virtual environment

## Prerequisites
- Python 3.8+
- Django 4.2+
- [Other dependencies]

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Extraordinarytechy/my-django-project.git
cd my-django-project
```

### 2. Set Up Virtual Environment
```bash
python -m venv env
source env/bin/activate  # Linux/Mac
# OR
env\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install -r src/requirements.txt
```

### 4. Configure Environment Variables
Create `.env` file in project root:
```ini
DJANGO_SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

## Running the Application

### Development Server
```bash
cd src
python manage.py runserver
```
Access at: http://localhost:8000

## Project Structure
```
my-django-project/
├── src/
│   ├── core/               # Main app
│   │   ├── migrations/     # Database migrations
│   │   ├── templates/      # HTML templates
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── my_django_project/  # Project config
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── manage.py
│   └── requirements.txt
├── .env.example            # Environment template
└── README.md
```

## Configuration
Modify these files for project-specific settings:
- `src/my_django_project/settings.py` - Django settings
- `src/core/urls.py` - Application URLs

## Testing
Run the test suite with:
```bash
python manage.py test
```

## Contributing
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


---

## Documentation
For detailed documentation, see:
- [Django Documentation](https://docs.djangoproject.com/)
