from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from api.models import Translation
from api.serializers import TranslationSerializer

# Create your views here.
class TranslationViewSet(viewsets.ReadOnlyModelViewSet):
	serializer_class = TranslationSerializer
	permission_classes = [permissions.IsAuthenticated]

	def get_queryset(self):
		queryset = Translation.objects.all()

		if 'query' in self.request.query_params:
			query = self.request.query_params.get('query')
			queryset = queryset.filter(polish__icontains=query) | queryset.filter(english__icontains=query)

		return queryset	
