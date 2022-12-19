from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework.response import Response


class RegisterView(APIView):

    def post(self, requests):
        data = requests.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            message = 'вы успешно зарегистривалис'
            return Response(message, status=201)


