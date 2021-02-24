from django.http import JsonResponse

class Response:

    def base(self, values=None, message="", status=200, success=True):
        if values is None:
            values = []

        return JsonResponse({
            'values': values,
            'message': message,
            'success' : success
        }, status=status)

    @staticmethod
    def ok(values=None, message=""):
        return Response().base(values=values, message=message, status=200, success=True)

    @staticmethod
    def badRequest(values=None, message=""):
        return Response().base(values=values, message=message, status=400, success=False)
    
    @staticmethod
    def unauthorized(values=None, message="Unauthorized"):
        return Response().base(values=values, message=message, status=401, success=False)