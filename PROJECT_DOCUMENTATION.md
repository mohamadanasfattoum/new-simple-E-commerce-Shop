# Project Documentation: Muckie E-Commerce

## Overview
Muckie E-Commerce is a Django-based web application designed to manage an online store. It provides a modular structure for handling product data, API endpoints, and database operations.

## Technical Details

### Framework and Language
- **Framework**: Django
- **Language**: Python

### Database
- **Type**: SQLite
- **Migrations**: Managed using Django's migration framework

### API
- **Type**: RESTful API
- **Endpoints**: Defined in `products/api.py`

### Directory Structure
- `project/`: Contains core project settings and configurations.
- `products/`: Contains the product app, including models, serializers, views, and URLs.
- `migrations/`: Tracks database schema changes.
- `manage.py`: Django's command-line utility.

## Models Update

### Stock Model
- **Fields**:
  - `quantity`: IntegerField to store the stock quantity.
  - `last_updated`: DateTimeField to track the last update time.
  - `products`: ManyToManyField linking multiple products to a stock.

### Product Model
- **Fields**:
  - `name`: CharField for the product name.
  - `short_description`: TextField for a brief description.
  - `description`: TextField for a detailed description.
  - `price`: DecimalField for the product price.
  - `stock`: OneToOneField linking the product to a single stock instance.

These updates enhance the relationship between products and stock, allowing for more flexible inventory management.

## Setup Instructions

1. Clone the repository and navigate to the project directory.
2. Install dependencies using `pip install -r requirements.txt`.
3. Apply database migrations with `python manage.py migrate`.
4. Start the development server using `python manage.py runserver`.

## Development Guidelines

- Follow PEP 8 coding standards.
- Use meaningful commit messages.
- Write unit tests for new features in `products/tests.py`.

## Deployment

- Ensure all migrations are applied.
- Use a production-ready database (e.g., PostgreSQL).
- Configure `ALLOWED_HOSTS` and other production settings in `project/settings.py`.

## Contact
For questions or support, please contact the project maintainer.