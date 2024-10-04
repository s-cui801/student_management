# Student Management System

This is a Django-based web application for managing student information.

## Features

- User authentication and authorization
- Student information management
- Pagination
- Error handling and validation


## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/s-cui801/student_management.git
    ```
2. Navigate to the project directory:
    ```bash
    cd student_management
    ```
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
6. Apply migrations:
    ```bash
    python manage.py migrate
    ```
7. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```
8. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:8000/students/`.
2. Log in with the superuser credentials.
3. Start managing students, courses, and grades.


