from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializer import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, UserChangePasswordSerializer, SendPasswordResetSerializer, UserPasswordResetSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRender
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# ==============================Manual Token Generation=====================================
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
# ============================================================================================

# ====================================User Registration view==================================
class UserRegistrationView(APIView):
    renderer_classes = [UserRender]  #(Renderers class)
    
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user) #(Token_generation)
        return Response({'token':token, 'msg':'Registration sucessful'}, status=status.HTTP_201_CREATED)
# ============================================================================================

# ====================================user Login view=========================================   
class UserLoginView(APIView):
    renderer_classes = [UserRender] #Renderers class
    
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = authenticate(email=email, password=password)

        if user is not None:
            token = get_tokens_for_user(user) #(Token_generation)
            return Response({'token':token, 'msg':'Login sucessful'}, status=status.HTTP_200_OK)
        else:
            return Response({'errors':{'non_field_errors':['Email or Password is not valid']}}, status=status.HTTP_404_NOT_FOUND)
# ============================================================================================

# =============================Logged User Data and Profile===================================
class UserProfileView(APIView):
    renderer_classes = [UserRender] #Renderers class
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
# ============================================================================================

# =====================================Change Password========================================
class UserChangePasswordView(APIView):
    renderer_classes = [UserRender] #Renderers class
    permission_classes = [IsAuthenticated]
    
    def post(self, request, format=None):
        serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password Changed Sucessfully'}, status=status.HTTP_200_OK)
# =============================================================================================

# =================================Password Reset Email========================================
class SendPasswordResetView(APIView):
    renderer_classes = [UserRender] #Renderers class
    
    def post(self, request, format=None):
        serializer = SendPasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password reset link send.Please check your email.'}, status=status.HTTP_200_OK)       
# =============================================================================================

# ================================After Reset Password View====================================
class UserPasswordResetView(APIView):
    renderer_classes = [UserRender] #Renderers class

    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
        serializer.is_valid(raise_exception=True)
        return Response({'msg': 'Password Reset Sucessfully'}, status=status.HTTP_200_OK)
# =============================================================================================