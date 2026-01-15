from django.urls import path

from .views import  CategoryList, CategoryDetails # category_list, category_detail,

urlpatterns = [
    #for class based:
    path('category/', CategoryList.as_view()),
    path('category/<id>/', CategoryDetails.as_view())
    
    # path('category/', category_list),
    # path('category/<id>/', category_detail)
]