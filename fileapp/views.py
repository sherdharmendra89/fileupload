from rest_framework.views import APIView
from rest_framework.response import Response
# from .serializers import UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CustomUserSerializer

# class UserRegistrationView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)


class SuperuserCreateView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            
            if request.path == '/api/superusers/':
              user = serializer.save(is_superuser=True)
              user.set_password(request.data.get('password'))
              user.is_staff = request.data.get('is_staff', True)  # Set is_staff value
            else:
                user = serializer.save(is_superuser=False)
                user.set_password(request.data.get('password'))
                user.is_staff = request.data.get('is_staff', False)  # Set is_staff value

            user.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .serializers import FileSerializer
from .permissions import IsSuperUser

class FileUploadAPI(APIView):
    parser_classes = (MultiPartParser,)
    permission_classes = (IsAuthenticated, IsSuperUser)

    def post(self, request, format=None):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)  # Save the file with the authenticated user
            return Response({'message': 'File uploaded successfully.'}, status=201)
        return Response(serializer.errors, status=400)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import File
from .serializers import FileSerializer

class FileListAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data)

from django.urls import reverse

class FileDownloadAPI(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            file = File.objects.get(pk=pk)
            download_url = request.build_absolute_uri(reverse('file-download', kwargs={'pk': file.pk}))
            return Response({'download_url': download_url})
        except File.DoesNotExist:
           return Response({'message': 'File not found.'}, status=404)
