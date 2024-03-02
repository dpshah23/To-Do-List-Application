# ToDoList - Your Personal Task Manager

## Overview

Welcome to ToDoList, your go-to personal task manager built on Django. This application not only provides a secure and intuitive platform for managing your tasks but also incorporates user authentication to ensure your data remains private. With the ability to add, delete, and mark tasks as done, ToDoList simplifies your day-to-day organization.

## Features

### 1. **User Authentication**
   - Securely register and log in to your personalized ToDoList account.
   - Ensure the confidentiality of your tasks with user-specific authentication.

### 2. **Task Management**
   - **Add Tasks:** Easily add new tasks with a title, description, and due date.
   - **Delete Tasks:** Remove completed or unnecessary tasks effortlessly.
   - **Mark as Done:** Keep track of your accomplishments by marking tasks as done.

### 3. **Intuitive Interface**
   - User-friendly design and seamless navigation make managing tasks a breeze.
   - Clear separation of concerns in the `todolistapp`, static, and templates for enhanced organization.

## Project Structure

### - `todolist` (Django Project)
   - Root project folder containing settings, URLs, and other configurations.

### - `todolistapp` (Django App)
   - Main app handling task management, views, and templates.

### - `static`
   - Holds static files such as CSS and JavaScript for enhanced styling and interactivity.

### - `templates`
   - Contains HTML templates for rendering views and providing a polished user interface.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/todolist.git
   ```

2. Navigate to the project directory:

   ```bash
   cd todolist
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Django migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser for admin access:

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

8. Log in with your superuser credentials and start managing your tasks.

## Customization

Feel free to extend or customize the ToDoList application based on your specific requirements. If you encounter any issues or have questions, please [open an issue](https://github.com/dpshah23/todolist/issues) on the GitHub repository.

Enhance your productivity with ToDoList - because every task matters.
