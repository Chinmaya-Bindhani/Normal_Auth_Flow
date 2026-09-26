# Auth Flow

A Django authentication system built with a **custom user model** using `email` as the login identifier instead of `username`.

## Features

- Custom user model (`CustomUser`) extending `AbstractBaseUser` and `PermissionsMixin`
- Email-based authentication (`USERNAME_FIELD = "email"`)
- Custom user manager (`create_user`, `create_superuser`)
- Session-based registration, login, and logout (Django forms + templates)
- Password confirmation and hashing handled in the form layer

## Tech Stack

- Python 3.12
- Django 5.2
- SQLite (default, dev)

## Project Structure

```
auth_flow/
├── auth_flow/          # Project settings
├── user/                # Auth app: models, forms, views, urls
│   ├── models.py         # CustomUser, CustomUserManager
│   ├── forms.py          # UserRegisterForm, MyLoginForm
│   ├── views.py           # register_view, login_view, logout_view, home_view
│   └── urls.py
├── templates/
│   ├── base.html
│   ├── home.html
│   └── accounts/
│       ├── login.html
│       └── register.html
├── manage.py
└── requirements.txt
```

## Setup

1. **Clone the repo**
   ```bash
   git clone <repo-url>
   cd auth_flow
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv env
   env\Scripts\activate      # Windows
   source env/bin/activate   # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the project root (see Environment Variables below)

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the dev server**
   ```bash
   python manage.py runserver
   ```

8. Visit `http://127.0.0.1:8000/`

## Environment Variables

Create a `.env` file with:

```
SECRET_KEY=your-secret-key-here
DEBUG=True
```

## How Authentication Works

- `CustomUser` replaces Django's default `User` model, using `email` as the unique login field instead of `username`.
- `CustomUserManager` handles user/superuser creation, including password hashing via `set_password()`.
- `UserRegisterForm` validates matching passwords and hashes the password before saving.
- `MyLoginForm` + `authenticate(username=email, password=password)` handles login — Django's `authenticate()` always uses the `username` kwarg internally, which maps to whatever `USERNAME_FIELD` is set to (`email` here).
- Session-based auth via `django.contrib.auth.login()` / `logout()` — no JWT/token auth in this flow.

## Key Settings

```python
AUTH_USER_MODEL = "user.CustomUser"
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "login"
```

## URLs

| Path | View | Description |
|---|---|---|
| `/register/` | `register_view` | Create a new account |
| `/login/` | `login_view` | Log in with email + password |
| `/logout/` | `logout_view` | Log out (requires login) |
| `/` | `home_view` | Protected home page |

## License

MIT