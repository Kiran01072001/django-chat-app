# Add this to the existing settings.py content
INSTALLED_APPS = [
    ...
    'chat',
    'channels',  # Add this for WebSocket support
]

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ASGI configuration for WebSocket
ASGI_APPLICATION = 'chat_project.asgi.application'
