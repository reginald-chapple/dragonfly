from django.contrib.auth.models import BaseUserManager

class AppUserManager(BaseUserManager):
    """
    Overriding BaseUserManager
    """
    use_in_migrations = True
    use_for_related_fields = True

    def create_user(self, username, email, first_name, last_name, password, **kwargs):
        if not username:
            raise ValueError('User name field is required')
        
        if not email:
            raise ValueError('Email field is required')

        if not first_name:
            raise ValueError('First name field is required')

        if not last_name:
            raise ValueError('Last name field is required')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, first_name=first_name, last_name=last_name, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, first_name, last_name, password, **extra_fields)