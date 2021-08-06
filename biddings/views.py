from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
    FormView
)
from django.views.generic.detail import SingleObjectMixin

from .forms import BiddingItemCreateViewForm, BiddingItemForm
from .models import BiddingItem
from .tools import place_bit


class BiddingItemListView(ListView):
    model = BiddingItem
    template_name = 'bidding_item_list.html'
    paginate_by = 15
    ordering = ['-created_at']


class BiddingItemCreateView(LoginRequiredMixin, CreateView):
    model = BiddingItem
    template_name = 'bidding_item_create.html'
    form_class = BiddingItemCreateViewForm
    success_url = reverse_lazy('biddings:bidding_item_list')

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


class BiddingItemDetailView(DetailView):
    model = BiddingItem
    template_name = 'bidding_item_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BiddingItemForm()
        return context


class BiddingItemFormView(SingleObjectMixin, FormView):
    template_name = 'bidding_item_detail.html'
    form_class = BiddingItemForm
    model = BiddingItem

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        new_bid = request.POST['bid']
        place_bit(self.object, new_bid)

        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('biddings:bidding_item', kwargs={'pk': self.object.pk})


class BiddingItemView(View):

    def get(self, request, *args, **kwargs):
        view = BiddingItemDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = BiddingItemFormView.as_view()
        return view(request, *args, **kwargs)



# class BiddingItemUpdateView(UserPassesTestMixin, UpdateView):
#     model = BiddingItem
#     template_name = 'bidding_item_update.html'
#     fields = ['item_name',
#               'image',
#               'description',
#               'starting_bid',
#               'auction_starts_at',
#               'auction_ends_at', ]
#
#     def test_func(self):
#         item = self.get_object()
#         user = self.request.user
#         return item.created_by == user or user.is_staff
#
#     def get_success_url(self):
#         """Return the URL to redirect to after processing a valid form."""
#         return reverse('biddings:bidding_item', kwargs={'pk': self.object.pk})


class BiddingItemDeleteView(UserPassesTestMixin, DeleteView):
    model = BiddingItem
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('biddings:bidding_item_list.html')

    def test_func(self):
        item = self.get_object()
        user = self.request.user
        return item.created_by == user or user.is_staff
