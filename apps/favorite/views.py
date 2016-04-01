from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.program.models import Program

from .models import Favorite
from .serializers import FavoriteSerializer


class FavoriteModelViewSet(viewsets.ModelViewSet):
    serializer_class= FavoriteSerializer
    paginate_by = 100
    queryset = Favorite.objects.all()

    def get_queryset(self):
        return Favorite.objects.for_user(self.request.user, model=Program)

    def create(self, request, *args, **kwargs):
        if request.data.get('target_object_id'):
            program_id = request.data.get('target_object_id')
            try:
                program = Program.objects.get(pk= program_id)

                fav = Favorite.objects.get_favorite(request.user, program, Program)

                if fav is None:
                    Favorite.objects.create(request.user, program, Program)
                    action = 'added'
                else:
                    fav.delete()
                    action = 'deleted'

                message = "Success " + action + " favorite"
                return Response({"message": message}, status=status.HTTP_200_OK)
            except Program.DoesNotExist:
                return Response({"message": "Error, the program dont exists"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

