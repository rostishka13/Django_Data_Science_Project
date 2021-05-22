from django.urls import path
from .views import home_view, SaleListView, SaleDetailView

app_name = 'sales'

urlpatterns = [
    path('', home_view, name='home'),
    path('sales/', SaleListView.as_view(), name='sale'),
    path('sales/<int:pk>/', SaleDetailView.as_view(), name ='detail')

]