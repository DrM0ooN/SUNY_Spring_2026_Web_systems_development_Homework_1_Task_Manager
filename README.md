# Task Manager - Django Application

A simple Django web application for managing tasks. Users can login, view their incomplete tasks, add new tasks, and mark tasks as completed.

## Features

- **User Authentication**: Secure login and logout
- **Task Management**: Create, view, and complete tasks
- **User-Specific Tasks**: Each user sees only their own tasks
- **Bootstrap UI**: Clean and responsive interface

## Requirements

- Python 3.8+
- Django 4.2.0

## Installation

1. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

2. **Apply migrations**
   ```
   python manage.py migrate
   ```

3. **Create a superuser** (admin account)
   ```
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin account. You can use:
   - Username: `admin`
   - Password: `admin` (or any password you prefer)

## Running the Application

Start the development server:
```
python manage.py runserver
```

Then open your browser and go to: `http://127.0.0.1:8000`

## Using the Application

1. **Login**: Enter your username and password on the login page
2. **View Tasks**: The home page shows all incomplete tasks
3. **Add Task**: Click "Add New Task" to create a new task
4. **Complete Task**: Click "Mark Complete" next to a task to mark it as done
5. **Logout**: Click "Logout" in the top navigation

## Admin Panel

Access the Django admin panel at: `http://127.0.0.1:8000/admin`

Use your superuser credentials to manage tasks and users from the admin interface.

## Project Structure

```
task_manager/
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── task_manager/          # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # URL routing
│   ├── wsgi.py            # WSGI configuration
│   └── __init__.py
├── tasks/                 # Main app
│   ├── models.py          # Task model definition
│   ├── views.py           # View logic
│   ├── forms.py           # Form definitions
│   ├── urls.py            # App URL routing
│   ├── admin.py           # Admin configuration
│   ├── apps.py            # App configuration
│   ├── templates/
│   │   └── tasks/         # HTML templates
│   │       ├── base.html       # Base template
│   │       ├── login.html      # Login page
│   │       ├── task_list.html  # Tasks list page
│   │       └── add_task.html   # Add task page
│   ├── migrations/        # Database migrations
│   └── __init__.py
└── db.sqlite3             # SQLite database (created after migration)
```

## Database Schema

### Task Model
- `id`: Auto-generated primary key
- `user`: Foreign key to User (each task belongs to a user)
- `title`: Task title (max 200 characters)
- `description`: Optional task description
- `completed`: Boolean flag for completion status (default: False)
- `created_at`: Timestamp when task was created
- `updated_at`: Timestamp of last update

## Notes

- Incomplete tasks are displayed on the home page
- Completed tasks are hidden from the main view (they're still in the database)
- Django's built-in authentication system is used for user management
- SQLite is used as the default database (suitable for development)
