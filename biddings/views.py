from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView
)

from .forms import BiddingItemCreateViewForm, BiddingItemForm
from .models import BiddingItem


def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })


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


# class BiddingItemFormView(SingleObjectMixin, FormView):
#     template_name = 'bidding_item_detail.html'
#     form_class = BiddingItemForm
#     model = BiddingItem
#
#     def get_success_url(self):
#         return reverse('biddings:bidding_item', kwargs={'pk': self.object.pk})
#
#
# class BiddingItemView(View):
#
#     def get(self, request, *args, **kwargs):
#         view = BiddingItemDetailView.as_view()
#         return view(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         view = BiddingItemFormView.as_view()
#         return view(request, *args, **kwargs)


class BiddingItemDeleteView(UserPassesTestMixin, DeleteView):
    model = BiddingItem
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('biddings:bidding_item_list.html')

    def test_func(self):
        item = self.get_object()
        user = self.request.user
        return item.created_by == user or user.is_staff
