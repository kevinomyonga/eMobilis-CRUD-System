from django.urls import path

from emobilis_crud.apps.users.views import user_list_view, user_input_view, user_update_view

app_name = "users"
urlpatterns = [
    path("list/", view=user_list_view, name="list"),
    path("input/", view=user_input_view, name="input"),
    path("update/", view=user_update_view, name="update"),
]
