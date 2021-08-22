from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ReservationSerializer, CateringSerializer, RoomSerializer, UserSerializer
from .models import Reservation, Catering, Room
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .permissions import IsSameUser, ReadOnly, StaffAllOrUserRead
from django.http import HttpResponse
from datetime import datetime


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by('id')
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated, StaffAllOrUserRead]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser, StaffAllOrUserRead]


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all().order_by('created_at')
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        serializer_context = {
            'request': request,
        }

        if not pk:
            queryset = self.get_queryset()
        else:
            if len(str(pk)) == 36:  # Check if the PK is an uuid
                queryset = Reservation.objects.filter(id=pk)
            else:  # if not is uuid, it's an user_id
                user = request.user.id
                if pk == "me":
                    queryset = Reservation.objects.filter(user_id=user)
                elif user == int(pk):
                    queryset = Reservation.objects.filter(user_id=pk)
                else:
                    return Response("Not your user", status=403)
        serializer = ReservationSerializer(
            queryset, many=True, context=serializer_context)
        return Response(serializer.data)

    def create(self, request):
        post = request.data
        if 'room_id' in post and 'starts_at' in post and 'ends_at' in post:
            user = User.objects.filter(id=request.user.id).first()

            room_id = post['room_id']
            starts_at = post['starts_at']
            ends_at = post['ends_at']

            queryset = Reservation.objects.create(
                room_id=room_id, user=user, starts_at=starts_at, ends_at=ends_at)
            # context=serializer_context)
            serializer = ReservationSerializer(queryset)
            return Response(serializer.data)
        else:
            return Response("All fields are mandatory.", status=400)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass


class CateringViewSet(viewsets.ModelViewSet):
    queryset = Catering.objects.all().order_by('created_at')
    serializer_class = CateringSerializer
    permission_classes = [IsAuthenticated]
