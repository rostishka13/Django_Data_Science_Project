from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sales
from .forms import SalesSearchForm
import pandas as pd
# Create your views here.
def home_view(request):
    form = SalesSearchForm(request.POST or None)
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        qs = Sales.objects.filter(created__date=date_from)
        df1 = pd.DataFrame(qs.values())
        df2 = pd.DataFrame(qs.values_list())
        print(df1)
        print('#######')
        # print(df2)

    context = {

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

