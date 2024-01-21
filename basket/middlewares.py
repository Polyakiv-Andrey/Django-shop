import uuid


class UserCookiesIdMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_id = request.COOKIES.get('user_id')

        if not user_id:
            response = self.get_response(request)
            user_id = uuid.uuid4()
            response.set_cookie('user_id', user_id)
        else:
            response = self.get_response(request)

        return response
