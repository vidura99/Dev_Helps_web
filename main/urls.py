from django.urls import path
from . import views

urlpatterns=[
    #path('admin/', admin.site.urls),
    #path('',include('main.urls')),
    #path('account',include('django.contrib.auth')),
    path('',views.home,name='home'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('save-comment',views.save_comment,name='save-comment'),
    path('save-upvote',views.save_upvote,name='save-upvote'),
    path('save-downvote',views.save_downvote,name='save-downvote'),
    # User Register
    path('accounts/register/',views.register,name='register'),
    # Ask Question
    path('ask-question',views.ask_form,name='ask-question'),
    # Tag Page
    path('tag/<str:tag>',views.tag,name='tag'),
    # Profile
    path('accounts/profile/',views.profile,name='profile'),
    # Tag Page
    path('tags',views.tags,name='tags'),
    
]