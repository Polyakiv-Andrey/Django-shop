# Django-shop

## Overview

Django Shop is a comprehensive e-commerce platform built with Django, allowing users to browse products, add them to a basket, and complete their purchase. The platform comes with a powerful admin panel for managing the storefront, products, orders, and more.

## Features

- **Product Catalog**: A well-organized product catalog with categories, filters, and search functionality.
- **Shopping Basket**: Functionality that allows customers to add items to a shopping basket and manage them before checkout.
- **Order Management**: Users can review their orders and track the delivery status.
- **Payment Integration**: Supports various payment methods including credit cards and online wallets.
- **Admin Panel**: A robust admin panel for managing products, orders, reviews, and site details.
- **User Notifications**: Automated email notifications for order status updates and communications.

## Technologies Used

### 1. [Django](https://www.djangoproject.com/)

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. In this project, Django serves as the backbone, handling the core functionality of the web application, including routing, views, and ORM for database interactions.

### 2. [Celery](https://pypi.org/project/celery/)

Celery is an asynchronous task queue/job queue system that is used in this project for handling background tasks, such as sending emails or processing tasks asynchronously to enhance performance.

### 3. [Redis](https://pypi.org/project/redis/)

Redis is an in-memory data structure store that acts as a broker for Celery in this project. It facilitates communication between different parts of the application by efficiently handling Celery's task queue.

### 4. [Sendgrid](https://pypi.org/project/sendgrid/)

Sendgrid is an email delivery service. In this project, Sendgrid may have been integrated to handle sending transactional emails, order confirmations, or other communication with users.

### 5. [Stripe](https://pypi.org/project/stripe/)

Stripe is a popular payment processing platform. In this project, Stripe integration could be used to handle online payments for merchandise purchases in the Django application.

### 6. [Psycopg2](https://pypi.org/project/psycopg2/)

Psycopg2 is a PostgreSQL adapter for Python. In this project, Psycopg2 is likely used to connect the Django application to a PostgreSQL database for data storage and retrieval.

### 7. [Requests](https://pypi.org/project/requests/)

Requests is a simple HTTP library for Python. In this project, Requests could be used for making HTTP requests to external APIs or services, possibly for fetching product information or other data.



## Images
![Screenshot 2024-01-15 at 16.08.19.png](static%2Fimages%2FScreenshot%202024-01-15%20at%2016.08.19.png)
![Screenshot 2024-02-15 at 17.32.14.png](static%2Fimages%2FScreenshot%202024-02-15%20at%2017.32.14.png)
![Screenshot 2024-02-15 at 17.33.28.png](static%2Fimages%2FScreenshot%202024-02-15%20at%2017.33.28.png)
![Screenshot 2024-02-15 at 17.34.23.png](static%2Fimages%2FScreenshot%202024-02-15%20at%2017.34.23.png)
![Screenshot 2024-02-15 at 17.35.03.png](static%2Fimages%2FScreenshot%202024-02-15%20at%2017.35.03.png)
![Screenshot 2024-02-15 at 17.36.18.png](static%2Fimages%2FScreenshot%202024-02-15%20at%2017.36.18.png)
![Screenshot 2024-02-15 at 17.36.42.png](static%2Fimages%2FScreenshot%202024-02-15%20at%2017.36.42.png)
![Screenshot 2024-02-15 at 17.37.36.png](static%2Fimages%2FScreenshot%202024-02-15%20at%2017.37.36.png)
![Screenshot 2024-02-15 at 17.38.06.png](static%2Fimages%2FScreenshot%202024-02-15%20at%2017.38.06.png)
![Screenshot 2024-02-15 at 17.38.24.png](..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Frd%2Fswqwf1q94z11v7m4j9vjcqy00000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_xugN2X%2FScreenshot%202024-02-15%20at%2017.38.24.png)
![Screenshot 2024-02-15 at 17.38.37.png](static%2Fimages%2FScreenshot%202024-02-15%20at%2017.38.37.png)
![Screenshot 2024-02-15 at 17.39.03.png](static%2Fimages%2FScreenshot%202024-02-15%20at%2017.39.03.png)
![Screenshot 2024-02-15 at 17.39.29.png](static%2Fimages%2FScreenshot%202024-02-15%20at%2017.39.29.png)


