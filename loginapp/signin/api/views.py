from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from signin.api.serializers import RegistarationSerializer

@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistarationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        # print(request.user)
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)