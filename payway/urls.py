from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.contrib.sitemaps.views import sitemap

from core import views
from core.sitemaps import StaticViewSitemap


def google_verify(request):
    return HttpResponse("google-site-verification: googlecd5090acaf63a595.html")


sitemaps = {
    'static': StaticViewSitemap,
}


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

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
]
