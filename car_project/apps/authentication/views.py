from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from  rest_framework.response import Response
from .renderers import UserJsonRenderer


from .serializers import RegistrationSerializer

class RegistrationView(APIView):

    permission_classes =(AllowAny,)
    renderer_classes = (UserJsonRenderer,)
    serializer_class = RegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


