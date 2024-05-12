from django.urls import path
from . import views

urlpatterns = [
    path('start', views.start_convo, name='start_convo'),
    path('<int:convo_id>', views.get_conversation, name='get_conversation'),
    path('', views.conversations, name='conversations'),
    path('getchats/<int:pk>', views.ChatAPIList.as_view()),
    path('sendmessage', views.ChatAPIList.as_view()),
    path('deletemessage/<int:pk>/<uuid:server_id>', views.delete_message_api)
]