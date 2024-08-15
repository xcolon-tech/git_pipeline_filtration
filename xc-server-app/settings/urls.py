from django.urls import path
from .views import UserProfileView, AccountSettingsView, DefaultBranchView, DeleteAccountView

urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('account-settings/', AccountSettingsView.as_view(), name='account-settings'),
    path('default-branch/', DefaultBranchView.as_view(), name='default-branch'),
    path('delete-account/', DeleteAccountView.as_view(), name='delete-account'),
]