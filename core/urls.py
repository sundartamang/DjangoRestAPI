from django.urls import path
from .views import (
    # employeeView,
    # update,
    # delete,
    # PostView,
    PostCreateListView,
    destroyupdateView
)


urlpatterns = [
    path('list-create', PostCreateListView.as_view(),name='list-create'),
    path('destroy-update/<str:pk>/', destroyupdateView.as_view(),name='destroy-update'),
    # path('', PostView.as_view(),name='employee'),
    # path('update/<str:pk>/', update,name='update'),
    # path('delete/<str:pk>/', delete,name='delete'),
    # path('', employeeView.as_view(),name='employee'),
]