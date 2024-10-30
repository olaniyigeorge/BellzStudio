from .paginations import StandardResultsSetPagination
from .serializers import NoteSerializer
from .models import Note
from rest_framework import generics # type: ignore

#    API ---------
class ApiV1Home(generics.ListCreateAPIView):
    queryset = Note.objects.all().order_by("written_at")
    serializer_class = NoteSerializer
    permission_classes = []
    pagination_class = StandardResultsSetPagination
    search_fields = ['title']
