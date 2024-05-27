from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import User
from core.serializers import UserSerializer

from firebase_admin.messaging import Message
from fcm_django.models import FCMDevice


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=["post"])
    def send(self, request):
        # You can still use .filter() or any methods that return QuerySet (from the chain)
        device = FCMDevice.objects.all().first()
        # send_message parameters include: message, dry_run, app
        device.send_message(Message(data={...}))
        return Response({"message": "Hello, World!"})

    # @action(detail=False, methods=["post"])
    # def register(self, request):
