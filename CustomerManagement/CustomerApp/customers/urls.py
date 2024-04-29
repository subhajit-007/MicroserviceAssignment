from django.urls import path

from .views import CustomerDetailsViewSet

urlpatterns = [
    path('customerdetails', CustomerDetailsViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('customerdetails/<str:pk>', CustomerDetailsViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    # path('user', UserAPIView.as_view())
]