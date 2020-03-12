from user.models import User
from rest_framework import viewsets,permissions
from user.serializers import UserSerializer

#User view set, helps us create CRUD without explicit routes
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny    
        ]
    serializer_class = UserSerializer