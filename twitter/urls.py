from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='twitter/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='twitter/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('editar/', views.editar, name='editar'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('follow/<str:username>/', views.follow, name='follow'),
    path('unfollow/<str:username>/', views.unfollow, name='unfollow'),
    


    # path('profile/', views.profile, name='profile'),
	# path('post/', views.post, name='post'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #añadimos la ruta media_root a la "urls" de las imagenes
