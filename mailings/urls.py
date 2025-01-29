from django.urls import path

from mailings.views import MessageListView, HomeView, MessageDeleteView, MessageDetailView, MessageUpdateView, MessageCreateView
app_name = 'mailings'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('message/list', MessageListView.as_view(), name='message_list'),
    path('message/detail/<int:pk>', MessageDetailView.as_view(), name='message_detail'),
    path('message/delete/<int:pk>', MessageDeleteView.as_view(), name='message_delete'),
    path('message/create', MessageCreateView.as_view(), name='message_create'),
    path('message/update/<int:pk>', MessageUpdateView.as_view(), name='message_update'),
]