from rest_framework import viewsets
from .models import Asignacion
from .serializers import AsignacionSerializer, UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect


# importamos los decoradores y clases necesarias para la autenticacion
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication




@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
# clase que se encarga de manejar las asignaciones de los usuarios con los detalles de entrada
class AsignacionViewSet(viewsets.ModelViewSet):
    queryset = Asignacion.objects.all()
    serializer_class = AsignacionSerializer


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    def post(self, request):
        user = get_object_or_404(User, username=request.data['username'])

        if not user.check_password(request.data['password']):
            return Response({'error': 'Credenciales invalidas'}, status=status.HTTP_400_BAD_REQUEST)

        token, created = Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(instance=user)

        return Response({'token': token.key, 'user': user_serializer.data}, status=status.HTTP_200_OK)


# debido a la simplicidad de el logout, no es necesario crear una vista, se puede hacer en una sola linea  
def salir(request):
    logout(request)
    return redirect('/')


class RegisterView(APIView):
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            user = User.objects.get(username=user_serializer.data['username'])
            user.set_password(user_serializer.data['password'])
            user.save()

            token = Token.objects.create(user=user)

            return Response({'token': token.key, 'user': user_serializer.data}, status=status.HTTP_201_CREATED)

        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class ProfileView(APIView):
    def post(self, request):
        print(request.user)

        return Response({'user': UserSerializer(instance=request.user).data}, status=status.HTTP_200_OK)
