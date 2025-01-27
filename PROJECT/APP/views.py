from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person
from .serializers import ItemSerializer
from rest_framework import status


class PersonView(APIView):

    def get(self, request, pk=None):
        if pk:  
            person = Person.objects.filter(pk=pk).first()
            if person:                
                serializer = ItemSerializer(person)
                return Response(serializer.data)
           
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # If no pk, return all items
        person = Person.objects.all()
        serializer = ItemSerializer(person, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        person = Person.objects.filter(pk=pk).first()
        if person:
            serializer = ItemSerializer(person, data=request.data)  # Changed `item` to `person`
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            # If validation fails, return errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # If person doesn't exist, return error
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, pk):
        person = Person.objects.filter(pk=pk).first()
        if person:
            person.delete()  # Delete the item
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        # If item doesn't exist, return error
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

