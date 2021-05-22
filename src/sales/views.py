from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sales
from .forms import SalesSearchForm
import pandas as pd
# Create your views here.
def home_view(request):
    sales_df = None
    position_df = None
    form = SalesSearchForm(request.POST or None)
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        sale_qs = Sales.objects.filter(created__date__lte=date_to, created__date__gte=date_from)
        if len(sale_qs) > 0:
            sales_df = pd.DataFrame(sale_qs.values())
            positions_data = []
            for sale in sale_qs:
                for pos in sale.get_positions():
                    obj = {
                        'position_id': pos.id,
                        'product': pos.product.name,
                        'quantity': pos.quantity,
                        'price': pos.price,
                        }
                    positions_data.append(obj)

            position_df = pd.DataFrame(positions_data)

            print(position_df)
            sales_df = sales_df.to_html()
            position_df = position_df.to_html()
        else:
            print('No data')


    context = {
        'sales_df':sales_df,
        'form': form,
        'position_df': position_df
    }
    return render(request, 'sales/home.html', context)


class SaleListView(ListView):
    model = Sales
    template_name = 'sales/main.html'
    # context_object_name = 'qs'

class SaleDetailView(DetailView):
    model = Sales
    template_name = 'sales/detail.html'

