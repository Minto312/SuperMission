from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
import re

class AuthMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        permit_urls = [
            '/account/register/',
            '/account/sign_in/',
            '/account/sign_out/',
            '/account/sign_in/query_email',
            '/account/sign_in/password_reset'
        ]
        
        if re.match(r'^/account/sign_in/query_email.*$', request.path_info) or re.match(r'^/account/sign_in/password_reset.*$', request.path_info):
            return response
        
        if request.path_info not in permit_urls and not request.user.is_authenticated:
            current_url = request.path
            return redirect('/account/sign_in/?next=' + current_url)
        return response