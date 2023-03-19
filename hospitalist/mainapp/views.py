from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import HospitalDetail
from .serializers import HospitalDetailSerializer
from knox.auth import TokenAuthentication


@api_view(["POST"])
def hospital_detail(request):
    token = request.META.get("HTTP_AUTHORIZATION", False)
    if token:
        token = str(token).split()[1].encode("utf-8")
        knoxAuth = TokenAuthentication()
        user, auth_token = knoxAuth.authenticate_credentials(token)
        request.user = user
        if request.method == "POST":
            serializer = HospitalDetailSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_hospital_detail(request):
    token = request.META.get("HTTP_AUTHORIZATION", False)
    if token:
        token = str(token).split()[1].encode("utf-8")
        knoxAuth = TokenAuthentication()
        user, auth_token = knoxAuth.authenticate_credentials(token)
        request.user = user

        details = HospitalDetail.objects.filter(user=request.user)
        serializer = HospitalDetailSerializer(details, many=True)
        return Response(serializer.data)

    return Response({})


@api_view(["PUT"])
def edit_hospital_detail(request, pk):
    token = request.META.get("HTTP_AUTHORIZATION", False)
    if token:
        token = str(token).split()[1].encode("utf-8")
        knoxAuth = TokenAuthentication()
        user, auth_token = knoxAuth.authenticate_credentials(token)
        request.user = user
        details = HospitalDetail.objects.get(pk=pk)
        serializer = HospitalDetailSerializer(details, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response({})


@api_view(["GET"])
def getAll_hospital_detail(self):
    details = HospitalDetail.objects.all()
    serializer = HospitalDetailSerializer(details, many=True)
    return Response(serializer.data)
