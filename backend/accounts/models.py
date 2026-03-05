from time import timezone

from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

# Usuaris
class Usuari(models.Model):
    nom = models.CharField(max_length=150, unique=True)
    correu = models.EmailField(unique=True)
    contrasenya = models.CharField(max_length=128)
    correuverificat = models.BooleanField(default=False)
    tipus = models.CharField(max_length=20, choices=[
        ('regular', 'Regular User'),
        ('organizer', 'Organizer User'),
    ])
    
    def __str__(self):
        return self.nom
    
    def clean(self):
        self.nom = self.nom.strip().replace(' ', '_')
        self.correu = self.correu.strip().lower()
        if(self.nom == ''):
            raise ValueError('El nom no pot estar buit')
            
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
    
class RegularUsuari(models.Model):
    # better to restrict the completeness
    usuari = models.OneToOneField(Usuari, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.usuari.nom
    
    
class OrganitzadorUsuari(models.Model):
    # better to restrict the completeness
    usuari = models.OneToOneField(Usuari, on_delete=models.CASCADE)
    tarifa = models.CharField(max_length=20, choices=[
        ('basic', 'Basic'),
        ('premium', 'Premium'),
        ('enterprise', 'Enterprise'),
    ])
    dataExpiracio = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.usuari.nom    
    
    def clean(self):
        if self.tarifa != 'basic' and not self.dataExpiracio:
            raise ValueError('La tarifa no básica requiere una fecha de expiración')
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
    
# Perfil i preferències

class Perfil(models.Model):
    usuari = models.OneToOneField(Usuari, on_delete=models.CASCADE)
    descripcio = models.TextField(blank=True)
    punts = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    nFestes = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    diesRatxa = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    ultimaFesta = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Perfil de {self.usuari.nom}"
    
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
    usuari = models.OneToOneField(Usuari, on_delete=models.CASCADE)
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
        return f"Preferències de {self.usuari.nom}"