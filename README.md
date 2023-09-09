# django-auth
Complete Authentication API with JWT in Django REST Framework

(Custom user model, User Registration, User Login with JWT tokens, Email Verification, Reset Password, User details views)

> Create django project(djangoauthapi1)
> Create django app('account')
> Add 'account' to 'settings.py'
> pip install djangorestframework
> Add 'rest_framework', in 'INSTALLED_APPS' in 'settings.py'
> pip install djangorestframework-simplejwt
> Add necessary code to 'settings.py' (Copy from simplejwt documentation)
> Add 'rest_framework_simplejwt', in INSTALLED_APPS in 'settings.py'
> Add code to 'settings.py' from detting od simplejet
> pip install django-cors-headers(This is for frontend)
> Add 'corsheaders', in INSTALLED_APPS in 'settings.py'
> Add 'corsheaders.middleware.CorsMiddleware', in middleware in 'settings.py'
> Add CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:9000",
] in 'settings.py'

> Add 'AUTH_USER_MODEL = 'account.User'' in 'settings.py'
> Create model in 'models.py' for custom user ('https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#a-full-example')
> Run migrations
> Wite code for 'admin.py' ('https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#a-full-example')
> Create 'serializer.py' and 'urls.py' files inside the app 'account'
> Include account.urls to base 'urls.py'
> Create views for different purposes
> Create urls for 'account'
> Add 'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ) in 'settings.py' in rest_framework section

> Add code in 'serializer.py'
> Create new file in 'account' named 'renderers.py' to show error for every mistake
> Add the renderers class in view.py
> To generate token write code in views.py
> Create views for 'change password' in 'views.py'
> Create serializer for 'change password' in 'serializer.py'
> Create urls for 'change password' in 'urls.py'
> Different urls are used for different purpose
> I have also the postman collection.
