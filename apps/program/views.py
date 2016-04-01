from django.shortcuts import render

from rest_framework import viewsets

from .models import Program, Episode, Category

from .serializers import EpisodeSerializer, ProgramSerializer, CategorySerializer
from rest_framework import filters
import django_filters


from rest_framework.generics import ListAPIView
#from haystack.inputs import AutoQuery


class EpisodeFilter(django_filters.FilterSet):
    q = django_filters.MethodFilter(action='filter_by_q', distinct=True)
    category = django_filters.MethodFilter(action='filter_by_category', distinct=True)

    def filter_by_q(self, queryset, value):
        return queryset.filter(title__icontains=value)

    def filter_by_category(self, queryset, value):
        return queryset.filter(program__category__slug=value)

    class Meta:
        model = Episode
        fields = {
            'id': ('exact',),
            'program__slug': ('exact',),
            'program': ('exact',),
            'created': ('lt', 'gt'),
            'title': ('icontains',),
            'description': ('icontains',),
        }


# class EpisodeFilter(django_filters.FilterSet):
#
#     class Meta:
#         model = Episode
#         fields = ['program__slug', 'program']


class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = EpisodeFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

class CategoryListAPIView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
