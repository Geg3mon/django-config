from rest_framework import status, views
from rest_framework.response import Response

from django.conf import settings


class Hello(views.APIView):

    @staticmethod
    def get(request):
        return Response({"enjoy": "coding"}, status=status.HTTP_200_OK)
