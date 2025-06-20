"""
WSGI config for bookmyseat project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookmyshow.settings')

application = get_wsgi_application()

# Optional: for platforms like Render that require `app` variable
app = application

# --- Auto-create superuser on deploy (only runs once, not during reloads) ---
if os.environ.get("RUN_MAIN") != "true":
    try:
        import bookmyshow.create_superuser
    except Exception as e:
        print(f"Error creating superuser: {e}")
