from django .urls import path
from .views import CollectionDelete, CollectionUpdate, Dashboard, CollectionCreate, CollectionDetail, CollectionDetailList
from .views import CollectionUpdate, CollectionDelete, CustomLoginView, RegisterPage, DashboardList
from .views import TaskList, TaskCreate, TaskUpdate, TaskDelete, CollectionPostDb, CollectionPostNamechange
from .views import DeleteQuestionFromCollection, ResourcePage
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('resources/', ResourcePage.as_view(), name='resources'),
    path('delete-question-from-collection/', DeleteQuestionFromCollection.as_view(), name='delete-question-from-collection'),
    path('collection-post-db/', CollectionPostDb.as_view(), name='collection-post-db'),
    path('collection-post-namechange/', CollectionPostNamechange.as_view(), name='collection-post-namechange'),
    path('tasklist/', TaskList.as_view(), name='tasklist'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('collection-create/', CollectionCreate.as_view(), name="collection-create"),
    path('collection-update/<str:pk>/', CollectionUpdate.as_view(), name="collection-update"),
    path('collection-delete/<str:pk>/', CollectionDelete.as_view(), name='collection-delete'),
    path('list/collection-create/', CollectionCreate.as_view(), name="collection-create-list"),
    path('list/collection-update/<str:pk>/', CollectionUpdate.as_view(), name="collection-update-list"),
    path('list/collection-delete/<str:pk>/', CollectionDelete.as_view(), name='collection-delete-list'),
    path('', Dashboard.as_view(), name="dashboard"),
    path('collection-detail/<str:col>/', CollectionDetail.as_view(), name="collection-detail"),
    path('collection-detail-list/<str:col>/<str:order>/', CollectionDetailList.as_view(), name="collection-detail-list"),
    path('collection-detail-list/<str:col>/<str:que>/<str:order>/', CollectionDetailList.as_view(), name="collection-detail-list-post"),
    path('collection-detail/<str:col>/<str:que>/', CollectionDetail.as_view(), name="collection-detail-post"),
    path('task-complete/<str:pk>/', TaskList.as_view(), name='task-complete'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<str:pk>/', TaskUpdate.as_view(), name='task-update'), 
    path('task-delete/<str:pk>/', TaskDelete.as_view(), name='task-delete'), 

    

    
    
]