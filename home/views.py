from django.shortcuts import render
from .serializers import UserSeralaizer, BlogSeralaizer
from .models import User, Blog
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login , logout 
from django.views.decorators.csrf import csrf_exempt

@api_view(["POST"])
def signup(request):
    serializer = UserSeralaizer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": 201 })
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def userlist(request):
    db = User.objects.all()
    serialazier = UserSeralaizer(db, many = True)
    return Response(serialazier.data)

@api_view(['PUT'])
def update_user(request, pk):
    try:
        blog = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = UserSeralaizer(blog, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Blog
@api_view(['GET'])
def list_blogs(request):
    blogs = Blog.objects.all().order_by('-date')
    serializer = BlogSeralaizer(blogs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_blog(request):
    serializer = BlogSeralaizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def retrieve_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = BlogSeralaizer(blog)
    return Response(serializer.data)

@api_view(['PUT'])
def update_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = BlogSeralaizer(blog, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_blog(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    blog.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# search

@api_view(['GET'])
def search(request):
    search_query = request.GET.get('search', None)
    
    if search_query:
        # Qidiruv so'roviga mos keladigan bloglarni topish
        blogs = Blog.objects.filter(
            name__icontains=search_query
        ) | Blog.objects.filter(
            info__icontains=search_query
        )
    else:
        # Qidiruv so'rovi bo'lmasa, barcha bloglarni qaytarish
        blogs = Blog.objects.all().order_by('-date')
    
    # Serializer yordamida bloglarni JSON formatida qaytarish
    serializer = BlogSeralaizer(blogs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Login, Logout

@csrf_exempt
@api_view(['POST'])
def loginUser(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({"detail": "Successfully logged in."}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['POST'])
def logoutUser(request):
    logout(request)
    return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
