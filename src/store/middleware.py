import time
import logging
from django.http import HttpResponse

# Настройка логирования
logger = logging.getLogger('request_logger')
handler = logging.FileHandler('requests.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Логируем входящий запрос
        logger.info(f"Incoming request: {request.method} {request.get_full_path()}")

        response = self.get_response(request)
        return response

class RequestTimeMiddleware:
   def __init__(self, get_response):
       self.get_response = get_response

   def __call__(self, request):
       timestamp = time.monotonic()

       response = self.get_response(request)

       print(
           f'Продолжительность запроса {request.path} - '
           f'{time.monotonic() - timestamp:.5f} сек.'
       )

       return response


class ExceptionLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Exception as e:
            # Логируем исключение
            logger.exception(
                f"Exception occurred while processing request {request.method} {request.get_full_path()}: {e}")
            raise

        return response
