from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from core import views


def google_verify(request):
    return HttpResponse("google-site-verification: googlecd5090acaf63a595.html")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('post-job/', views.post_job, name='post_job'),
    path('profile/', views.profile_view, name='profile'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('job/<int:job_id>/bid/', views.add_bid, name='add_bid'),
    path('googlecd5090acaf63a595.html', google_verify),
]
