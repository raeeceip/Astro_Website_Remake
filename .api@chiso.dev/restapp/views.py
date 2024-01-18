from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def post_test(request):
    return Response({'message': 'Hello, world!'})




