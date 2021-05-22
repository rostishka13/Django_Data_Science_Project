from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sales
# Create your views here.
def home_view(request):
    hello = 'hello from the view'
    return render(request, 'sales/home.html', {'hello':hello})


class SaleListView(ListView):
    model = Sales
    template_name = 'sales/main.html'
    # context_object_name = 'qs'

class SaleDetailView(DetailView):
    model = Sales
    template_name = 'sales/detail.html'

