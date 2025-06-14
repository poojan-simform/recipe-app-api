"""
Views for the user API.
"""

from rest_framework import authentication, generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken

from user.serializers import AuthTokenSerializer, UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Create a new user."""

    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""

    serializer_class = AuthTokenSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""

    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return authenticated user."""
        return self.request.user
