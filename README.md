# QR Code Menu for Restaurants

This project allows restaurants to generate unique QR codes for their menu, offering a faster, more hygienic, and eco-friendly solution for customers to view the menu. By scanning a simple QR code, customers can view the menu on their smartphones, reducing the need for physical menus, minimizing wait times, and reducing paper waste.

## Features

- **Unique QR Code Generation:** Generate a unique QR code for your restaurant’s menu.
- **Customer Convenience:** Customers can instantly access the menu via a QR code, reducing wait times.
- **Eco-Friendly:** No need for paper menus, helping to reduce waste.
- **Hygienic:** Minimize physical contact by allowing customers to view the menu on their devices.

## Project Requirements

Before running the project, make sure you have the following installed:

- Python 3.8 or higher
- PostgreSQL (for the database)
- Virtual environment tools (venv)
- .env file (python-decouple)

### Project Dependencies

You can install all required dependencies using the provided `requirements.txt`.

1. **Python Decouple:** For environment variables.
2. **PostgreSQL:** Relational database for storing restaurant data.
3. **Pillow and qrcode:** To handle image generation for QR codes.
4. **Gunicorn:** WSGI server for deploying the application.

## Project Setup

### Step 1: Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Database Migrations

```bash
python3 manage.py migrate
```

### Step 4: Create a Superuser

```bash
python3 manage.py createsuperuser
```

### Step 5: Collect Static Files

```bash
python3 manage.py collectstatic
```

### Step 6: Run the Server Locally

```bash
python3 manage.py runserver
```

### Step 7: If using Gunicorn - Production

```bash
gunicorn django_qr_project.wsgi:application
```

### Step 8: Setup Project and Run - Deployment on Render

```bash
python3 manage.py setup_project_and_run
```

## Known Issues & Solutions

| **Issue**                                                                               | **Solution**                                                                                                                    |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| PostgreSQL on Render offers free hosting for 30 days. After that, you can choose a paid plan. | After 30 days, run the project locally to check if it works.                                                                          |
| Render does not allow to run pre-deployment commands in the free plan.                        | Create a custom command and list down all the commands you want to run before deployment and then the command to run the WSGI server. |

## Deployment

For production deployment, I recommend using Gunicorn as the WSGI server and PostgreSQL for the database.

If you are hosting on Render or a similar platform, ensure you configure your environment variables, PYTHON_VERSION and database connection settings correctly.
