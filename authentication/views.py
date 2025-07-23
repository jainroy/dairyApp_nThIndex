from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import User
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework import generics, status
from rest_framework.response import Response
import jwt
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

# Create your views here.


class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        # token = RefreshToken.for_user(user).access_token
        
        # current_site = get_current_site(request)
        # relative_link = reverse('email-verify')
        # absurl = 'http://' + str(current_site.domain) + relative_link + "?token=" + str(token)
        # email_body = 'Hi ' + user.username + ' Use the link below to verify your email \n' + absurl
        # data = {
        #     'email_body': email_body,
        #     'email_subject': "Verify yoyur email",
        #     'token': str(token),
        #     'to_email': user.email
        # }
        # Util.send_email(data)


        return Response(user_data, status=status.HTTP_201_CREATED)
    


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        # print(data)
        # breakpoint()
        return Response(data, status=status.HTTP_200_OK)
    


class LogoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Logout by blacklisting refresh token",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=["refresh"],
            properties={
                'refresh': openapi.Schema(type=openapi.TYPE_STRING)
            }
        )
    )
    def post(self, request):
        refresh_token = request.data.get("refresh", None)
        if not refresh_token:
            return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"msg": "Logout successful"}, status=status.HTTP_200_OK)
        except TokenError:
            return Response({"error": "Invalid or expired token"}, status=status.HTTP_400_BAD_REQUEST)