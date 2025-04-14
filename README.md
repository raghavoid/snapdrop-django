# Snapdrop

Snapdrop is a Django-based web application that allows users to instantly share files, images, videos, and messages across devices on the same network.It is a peer-to-peer, open-source solution that requires no setup or signup.

## Features

- **File Upload and Download**: Upload files and download them securely.
- **User Authentication**: Sign up, log in, and log out functionality with email-based authentication.
- **Responsive Design**: Optimized for both desktop and mobile devices.
- **Session-Based File Tracking**: Tracks uploaded files during user sessions.
- **Database Cleanup**: Automatically removes orphaned file entries from the database.
- **Custom Authentication Backend**: Email-based authentication using Django's `BaseBackend`.
- 
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/snapdrop.git
   cd snapdrop
   
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   
4. Install dependencies:
   pip install -r requirements.txt

5. Apply migrations:
   ```bash
   python manage.py migrate

7. Run the development server:
   ```bash
   python manage.py runserver

9. Open your browser and navigate to http://127.0.0.1:8000.

## Usage

**Sign Up**: Create an account using your email and password.
**Log In**: Access the application with your credentials.
**Upload Files**: Use the upload page to share files.
**Download Files**: Download files shared by other users.
**Logout**: Securely log out of your account.

## Key Files

- views.py: Contains the core logic for file upload, download, login, and signup.
- models.py: Defines the database models for users and uploaded files.
- forms.py: Handles form validation for user signup.
- auth_backend.py: Implements email-based authentication.
- middleware.py: Cleans up uploaded files after user sessions.

## Technologies Used
Backend: Django 5.2
Frontend: HTML, CSS, JavaScript (with Tailwind CSS for styling)
Database: SQLite
Authentication: Custom email-based authentication
