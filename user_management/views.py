from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from user_management import models

# Create your views here.


class UserLogin(APIView):

    def post(self, request):
        user = models.UserProfile()
        user.username = 'Varun'
        user.save()
        return Response({"data" : "Success."}, status=status.HTTP_200_OK)



class UserLogout(APIView):

    def post(self, request):
        users = models.UserProfile.objects.all()
        print(users)
        for user in users:
            print(user.username)
        return Response({"data" : "Success"}, status=status.HTTP_200_OK)



class CreateUser(APIView):

    def post(self, request):
        return Response({"data" : "Success"}, status=status.HTTP_200_OK)