from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import RegisterUser, LoginUser, BlogListView, logout_user, search
from account import views as user_views


urlpatterns = [
    path('', BlogListView.as_view(), name = 'home'),
    path('register/', RegisterUser.as_view(), name = 'register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('blog/', include('blog.urls')),
    path('search/', search, name = 'search'),
    path('password-reset/', auth_views.PasswordResetView.as_view( template_name = 'main/password_reset.html'), name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view( template_name = 'main/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view( template_name = 'main/password_reset_confirm.html'), name='password_reset_confirm'),
    path('profile/', user_views.profile, name='profile'),
]