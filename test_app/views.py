from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from test_app.models import *
from test_app.serializers import *
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.db.models import Subquery, OuterRef


# Create your views here.


class UserLoginView(APIView):
    """
    user login API view user need to post email and password to login
    """
    def post(self, request, *args, **kwargs):
        email = request.data['email']
        password = request.data['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            token = Token.objects.get_or_create(user=user)
            return Response({'response':{'token':token[0].key, 'user_id':token[0].user_id}})
        else:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
        
class UserLogoutView(APIView):
    """
    user logout API view
    """
    def post(self, request):
        import pdb;pdb.set_trace()
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)


class UserDetailView(APIView):
    """
    get and update user's details API view 
    """
    # permission_classes = [IsAuthenticated]

    def get(self, request, id):
        queryset = CustomUser.objects.filter(id=id)
        if queryset is not None:
                serializer = UserLoginSerializer(queryset, many=True)
                return Response(serializer.data)
        else:
                return Response({'error': 'Invalid user_id'}, status=status.HTTP_401_UNAUTHORIZED)
            
    def patch(self, request, id):
        queryset =get_object_or_404(CustomUser, id = id)
        serializer = UserLoginSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"result" : "User's details updated!"}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors) 


class CountryDetailView(APIView):
    '''
    get country's datials API view
    '''
    # permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        queryset = Country.objects.all()
        annotated_queryset = queryset.annotate(
            cities=Subquery(
                City.objects.filter(country=OuterRef('pk')).values_list('name', flat=True)
            )
        )

        serializer = CountrySerializer(annotated_queryset, many=True)
        
        return Response(serializer.data)
