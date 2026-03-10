import json

from django.db import IntegrityError
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError
from .models import Preferencia, User, RegularUser, OrganitzadorUser, Perfil

def _request_payload(request):
    """Support both JSON and form-encoded request bodies."""
    if request.content_type and "application/json" in request.content_type:
        try:
            return json.loads(request.body or "{}")
        except json.JSONDecodeError:
            return None
    return request.POST.dict()


def _extract_common_fields(payload):
    username = payload.get("username") or payload.get("nom")
    email = payload.get("email") or payload.get("correu")
    password = payload.get("password") or payload.get("contrasenya")
    first_name = payload.get("first_name", "")
    return username, email, password, first_name


def _build_base_user(payload, user_type):
    username, email, password, first_name = _extract_common_fields(payload)
    if not username or not email or not password:
        return None, JsonResponse(
            {
                "error": "Missing required fields: username/email/password",
                "accepted_aliases": {
                    "username": ["username", "nom"],
                    "email": ["email", "correu"],
                    "password": ["password", "contrasenya"],
                },
            },
            status=400,
        )

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        tipus=user_type,
    )
    Perfil.objects.create(user=user)
    Preferencia.objects.create(user=user)
    return user, None


@method_decorator(csrf_exempt, name='dispatch')
class RegisterRegularUser(View):
    def post(self, request):
        payload = _request_payload(request)
        if payload is None:
            return JsonResponse({"error": "Invalid JSON body"}, status=400)

        try:
            user, error_response = _build_base_user(payload, user_type="regular")
            if error_response:
                return error_response

            RegularUser.objects.create(user=user)
            return JsonResponse(
                {
                    "message": "Regular user created",
                    "user_id": user.id,
                    "tipus": user.tipus,
                },
                status=201,
            )
        except IntegrityError:
            return JsonResponse(
                {"error": "Username or email already exists"},
                status=400,
            )
        except (ValidationError, ValueError) as e:
            error = e.message_dict if hasattr(e, 'message_dict') else str(e)
            return JsonResponse({"error": error}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class RegisterAdministratorUser(View):
    def post(self, request):
        payload = _request_payload(request)
        if payload is None:
            return JsonResponse({"error": "Invalid JSON body"}, status=400)

        plan = payload.get("plan", "basic")
        exp_date = payload.get("expDate")

        try:
            user, error_response = _build_base_user(payload, user_type="organizer")
            if error_response:
                return error_response

            # For now, administrator users are represented by OrganitzadorUser.
            OrganitzadorUser.objects.create(user=user, plan=plan, expDate=exp_date)
            return JsonResponse(
                {
                    "message": "Administrator user created",
                    "user_id": user.id,
                    "tipus": user.tipus,
                    "plan": plan,
                },
                status=201,
            )
        except IntegrityError:
            return JsonResponse(
                {"error": "Username or email already exists"},
                status=400,
            )
        except (ValidationError, ValueError) as e:
            error = e.message_dict if hasattr(e, 'message_dict') else str(e)
            return JsonResponse({"error": error}, status=400)
