from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import overspeed
from .serailizer import OverspeedSerializer
# Create your views here.


class OverspeedDetail(APIView):
    def get(self,request):
        obj = overspeed.objects.all()
        serializer = OverspeedSerializer(obj,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self,request):
        serializer = OverspeedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

class OverspeedInfo(APIView):
    def get(self,request,id):
        try:
            obj = overspeed.objects.get(id=id)

        except overspeed.DoesNotExist:
            msg = {"msg":"Tidak Ada"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = OverspeedSerializer(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,id):
        try:
            obj = overspeed.objects.get(id=id)

        except overspeed.DoesNotExist:
            msg = {"msg":"Tidak Ada"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = OverspeedSerializer(obj,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id):
        try:
            obj = overspeed.objects.get(id=id)

        except overspeed.DoesNotExist:
            msg = {"msg":"Tidak Ada"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = OverspeedSerializer(obj,data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        try:
            obj = overspeed.objects.get(id=id)

        except overspeed.DoesNotExist:
            msg = {"msg":"Tidak Ada"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        obj.delete()
        return Response({"msg":"Terhapus"}, status=status.HTTP_204_NO_CONTENT)