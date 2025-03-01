from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

class ContentSecurityPolicyMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response["Content-Security-Policy"] = "default-src 'self'; script-src 'self' cdnjs.cloudflare.com; style-src 'self' fonts.googleapis.com"
        return response
