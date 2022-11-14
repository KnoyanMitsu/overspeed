from django.urls import path
from .views import OverspeedDetail, OverspeedInfo

urlpatterns =[
    path("ovs/", OverspeedDetail.as_view(), name="ovs"),
    path("ovs/<int:id>/", OverspeedInfo.as_view())
]