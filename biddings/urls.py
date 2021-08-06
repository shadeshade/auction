from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    BiddingItemListView,
    BiddingItemDetailView,
    BiddingItemCreateView,
    # BiddingItemUpdateView,
    BiddingItemDeleteView,
    BiddingItemView,
)

app_name = 'biddings'

urlpatterns = [
    path('', BiddingItemListView.as_view(), name='bidding_item_list'),
    path('<int:pk>', BiddingItemView.as_view(), name='bidding_item'),
    path('create/', BiddingItemCreateView.as_view(), name='bidding_item_create'),
    # path('update/<int:pk>/', BiddingItemUpdateView.as_view(), name='bidding_item_update'),
    path('delete/<int:pk>/', BiddingItemDeleteView.as_view(), name='bidding_item_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
