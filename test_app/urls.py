from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from test_app import views
urlpatterns = [
    path('api/v1/login/', views.UserLoginView.as_view()),
    path('api/v1/logout/', views.UserLogoutView.as_view()),
    path('api/v1/users/<int:id>/', views.UserDetailView.as_view()),
    path('api/v1/countries/', views.CountryDetailView.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
