from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from account.models import CustomUser, Profile
from rest_framework.authtoken.models import Token
from .serializers import CustomUserSerializer, ProfileSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication






class CustomUserListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            # return Response(serializer.errors, status=status.HTTP_201_CREATED)
            #  token created
             
            user = serializer.save()
            token_obj, created = Token.objects.get_or_create(user=user)
            if created:
                # return Response({'payload': serializer.data, 'token': str(token_obj),'status': 200, 'message': 'token created'}, )
                    return Response({'user': serializer.data, 'token': token_obj.key}, status=status.HTTP_201_CREATED)
            else:
                # Handle case where token cannot be created
                return Response({'error': 'Token creation failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                # return Response({'status': 403,'error': 'Token creation failed', 'token': str(token_obj), 'message': 'token can not created'}, )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomUserRetrieveUpdateDestroyAPIView(APIView):
    # permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    # def put(self, request, pk):
    #     user = self.get_object(pk)
    #     serializer = CustomUserSerializer(user, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         user = self.get_object(pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class ProfileListCreateAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         profiles = Profile.objects.all()
#         serializer = ProfileSerializer(profiles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProfileRetrieveUpdateDestroyAPIView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get_object(self, pk):
#         try:
#             return Profile.objects.get(pk=pk)
#         except Profile.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)

#     def get(self, request, pk):
#         profile = self.get_object(pk)
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         profile = self.get_object(pk)
#         serializer = ProfileSerializer(profile, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         profile = self.get_object(pk)
#         profile.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
