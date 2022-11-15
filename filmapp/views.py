from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import *
from rest_framework.views import APIView
from .serializers import *

# class KinolarAPIView(APIView):
#     def get(self, request):
#         kinolar = Kino.objects.all()
#         serializer = KinoSerializer(kinolar, many=True)
#         return Response(serializer.data)
#
# class AktyorlarAPIView(APIView):
#     def get(self, request):
#         aktyorlar = Aktyor.objects.all()
#         serializer = AktyorSerializer(aktyorlar, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         aktyor = request.data
#         serializer = AktyorSerializer(data=aktyor)
#         if serializer.is_valid():
#             serializer.save()
#             natija = {"Xabar":"Saqlandi",
#                       "Yangi aktyor":serializer.data}
#             return Response(natija)
#         return Response({"Ma'lumotda xatolik bor"})
#
# class AktyorAPIView(APIView):
#     def get(self, request, pk):
#         aktyor = Aktyor.objects.get(id=pk)
#         serializer = AktyorSerializer(aktyor)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         aktyor = Aktyor.objects.get(id=pk)
#         serializer = AktyorSerializer(aktyor, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             natija = {"Xabar":"Saqlandi",
#                       "O'zgartirilgan aktyor":serializer.data}
#             return Response(natija)
#         return Response({"Xabar":"Ma'lumotda xatolik bor", "Detail":serializer.errors})
#
#     def delete(self, request, pk):
#         aktyor = Aktyor.objects.get(id=pk)
#         aktyor.delete()
#         return Response({"Successfully deleted"})

class CommentsAPIView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        comment = request.data
        serializer = CommentSerializer(data=comment)
        if serializer.is_valid():
            serializer.save(user=user)
            natija = {"Success":"True",
                      "New comment":serializer.data}
            return Response(natija)
        return Response({"detail":serializer.errors})

class KinoViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Kino.objects.all()
    serializer_class =KinoSerializer

    @action(methods=['GET'], detail=True)
    def commentlar(self, request, pk):
        comment = Comment.objects.filter(kino__id=pk)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)

class AktyorViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Aktyor.objects.all()
    serializer_class =AktyorSerializer

# class CommentViewSet(ModelViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Comment.objects.all()
#     serializer_class =CommentSerializer