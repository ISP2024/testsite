"""Views that return various status codes."""
import django.http as http
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def index(request: HttpRequest):
    """Return index page of all available pages."""
    return render(request, 'index.html')

def forbidden(request: HttpRequest):
    """Return a 403 response."""
    return http.HttpResponseForbidden("Not allowed here!")

def unauthorized(request: HttpRequest):
    """Return a 401 Unauthorizaed response."""
    return http.HttpResponse("Unauthorized", status=401)

def payment_required(request: HttpRequest):
    return http.HttpResponse("Payment Required, just like NY Times", status=402)

def unacceptable(request: HttpRequest):
    """Return a 406 Not Acceptable response."""
    return http.HttpResponse("Not Acceptable", status=406)

def not_allowed(request: HttpRequest):
    """Return a 405 Method not Allowed response."""
    return http.HttpResponseNotAllowed("Not Allowed")

def any_status(request: HttpRequest, status_code: int):
    """Return any requested status code."""
    if status_code < 100 or status_code > 599:
        return http.HttpResponseBadRequest(f"Status value must be an integer 100 - 599")
    return HttpResponse(f"Status code {status_code}", status=status_code)
