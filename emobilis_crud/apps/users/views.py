from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView, UpdateView

from emobilis_crud.apps.users.models import User


class UserListView(ListView):
    model = User
    queryset = User.objects.all()


user_list_view = UserListView.as_view()


class UserInputView(CreateView):
    model = User
    fields = [
        "username",
        "email",
        "password",
    ]
    success_message = _("Information successfully saved")
    success_url = reverse_lazy('users:list')


user_input_view = UserInputView.as_view()


class UserUpdateView(UpdateView):
    model = User
    fields = [
        "username",
        "email",
        "password",
    ]
    success_message = _("Information successfully saved")
    success_url = reverse_lazy('users:list')


user_update_view = UserUpdateView.as_view()
