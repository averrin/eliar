from django.middleware.locale import LocaleMiddleware
from django.utils import translation

class SwitchLocaleMiddleware(LocaleMiddleware):
    def process_request(self, request):
        if 'language' in request.GET:
            request.session['django_language'] = request.GET['language']
        language = translation.get_language_from_request(request)
        translation.activate(language)
        request.LANGUAGE_CODE = language