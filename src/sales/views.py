from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sales
from .forms import SalesSearchForm
# Create your views here.
def home_view(request):
    form = SalesSearchForm(request.POST or None)
    hello = 'hello from the view'
    context = {
        'hello': hello,
        'form': form,
    }
    return render(request, 'sales/home.html',context )


class SaleListView(ListView):
    model = Sales
    template_name = 'sales/main.html'
    # context_object_name = 'qs'

class SaleDetailView(DetailView):
    model = Sales
    template_name = 'sales/detail.html'

