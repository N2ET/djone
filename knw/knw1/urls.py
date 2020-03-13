from django.urls import path

from . import views

app_name = 'knw1'
urlpatterns = [
    path('', views.index, name='index'),

    # /knw1/5 会被重定向到 /knw1/5/
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('new/', views.IndexView.as_view(), name='new_index'),
    path('new/<int:pk>/', views.DetailView.as_view(), name='new_detail')
]