from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from .models import Notification
from .serializers import NotificationSerializer

class ResponsePagination(PageNumberPagination):
    page_query_param = 'p'
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10

@api_view(['GET'])
def get_notfication_list(request):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        notification = Notification.objects.get(user=request.user.id)
        paginator = ResponsePagination()
        results = paginator.paginate_queryset(notification, request)
        serializer = NotificationSerializer(results, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)
