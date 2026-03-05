from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError
from .models import Preferencia, Usuari, RegularUsuari, OrganitzadorUsuari, Perfil

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class RegisterAccount(View):
    def get(self, request):
        return JsonResponse({
            "test": "true",
        })
        
    def post(self, request):
        # check if the args are correct
        if 'nom' not in request.POST or 'correu' not in request.POST or 'contrasenya' not in request.POST or 'tipus' not in request.POST:
            return JsonResponse({
                "error": "Falten arguments",
            }, status=400)
        nom = request.POST['nom']
        correu = request.POST['correu']
        contrasenya = request.POST['contrasenya']
        tipus = request.POST['tipus']
        
        try:
            user = Usuari.objects.create(nom=nom, correu=correu, contrasenya=contrasenya, tipus=tipus)
            perfil = Perfil.objects.create(usuari=user)
            prefencia = Preferencia.objects.create(usuari=user)
        
            subclass = None
            if tipus == 'regular':
                subclass = RegularUsuari.objects.create(usuari=user)
            else:
                subclass = OrganitzadorUsuari.objects.create(usuari=user, tarifa='basic')
            
            user.save()
            perfil.save()
            subclass.save()
            prefencia.save()
            
            return JsonResponse({
                "message": "Usuari creat correctament",
            }, status=201)
            
        except (ValidationError, ValueError) as e:
            error = e.message_dict if hasattr(e, 'message_dict') else str(e)
            return JsonResponse({
                "error": error,
            }, status=400)
        