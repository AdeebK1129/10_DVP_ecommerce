from django.views.generic import TemplateView

class ProductDetailView(TemplateView):
    template_name = 'shop/product_show.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_id'] = self.kwargs['pk']
        return context
