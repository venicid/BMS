from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, reverse
from BMS import settings


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        white_list = settings.WHITE_LIST
        if request.path in white_list:
            return None
        if not request.user.is_authenticated:
            next_url = reverse('login_reg:index')
            return redirect(next_url)
