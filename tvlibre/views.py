from django.views.generic import TemplateView

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from apps.userProfile.serializers import UserAuthenticationSerializer


class IndexView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            context['user_data'] = UserAuthenticationSerializer(instance=self.request.user).data
        else:
            context['user_data'] = {}
        return context




class CustomPagination(PageNumberPagination):
    """
        Custom pagination
            return only page number in next and previous pages.
    """
    def get_paginated_response(self, data):
        resp = {}
        resp['count'] = self.page.paginator.count
        if self.page.has_next():
            resp['next']  = self.page.next_page_number()
        else:
            resp['next']  = None

        if self.page.has_previous():
            resp['previous'] = self.page.previous_page_number()
        else:
            resp['previous'] = None

        resp['results'] = data
        return Response(resp)