from time import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

# Usuaris
class User(AbstractUser):
    email = models.EmailField(unique=True)
    tipus = models.CharField(max_length=20, choices=[
        ('regular', 'Regular User'),
        ('organizer', 'Organizer User'),
    ])
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self):
        return self.username
    
            
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    
    
    
    
    
    
class RegularUser(models.Model):
    # better to restrict the completeness
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.usuari.username
    
class OrganitzadorUser(models.Model):
    # better to restrict the completeness
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plan = models.CharField(max_length=20, choices=[
        ('basic', 'Basic'),
        ('premium', 'Premium'),
        ('enterprise', 'Enterprise'),
    ])
    expDate = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    
    def clean(self):
        if self.plan != 'basic' and not self.expDate:
            raise ValueError('La tarifa no básica requiere una fecha de expiración')
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
# Perfil i preferències

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    points = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    nFestes = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    diesRatxa = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    ultimaFesta = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Perfil de {self.user.username}"
    
    def clean(self):
        if(self.ultimaFesta and self.ultimaFesta > timezone.now()):
            raise ValidationError('La última festa no pot ser en el futur')
        if(self.diesRatxa > 0 and not self.ultimaFesta):
           raise ValidationError('Si hi ha dies en ratxa, ha d\'haber una última festa')
        if(self.diesRatxa == 0 and self.ultimaFesta):
           raise ValidationError('Si no hi ha dies en ratxa, no pot haber una última festa')
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
class Preferencia(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idioma = models.CharField(max_length=2, choices=[
        ('ca', 'Catalan'),
        ('es', 'Spanish'),
        ('en', 'English'),
    ], default='ca')
    tipusUnitats = models.CharField(max_length=20, choices=[
        ('metric', 'Metric'),
        ('imperial', 'Imperial'),
    ], default='metric')
    aparenca = models.CharField(max_length=20, choices=[
        ('clar', 'Clar'),
        ('fosc', 'Fosc'),
        ('dispositiu', 'Dispositiu'),
        ('daltonic', 'Daltonic'),
    ], default='light')
    # todo add more preferences like notifications, privacy, etc.
    
    def __str__(self):
        return f"Preferències de {self.user.username}"