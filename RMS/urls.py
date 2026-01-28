from django.urls import path

#from .views import  CategoryList, CategoryDetails # category_list, category_detail,
from .views import CategoryAPIView, CategoryDetailAPIView

urlpatterns = [
    # for generics api: 
    path('category/', CategoryAPIView.as_view()),
    path('category/<pk>/', CategoryDetailAPIView.as_view()) # OR,
    #path('category/<str:name>/', CategoryDetailAPIView.as_view())  #need to add lookup field in class to use identifier other than pk like id, name
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # # for class based:
    # path('category/', CategoryList.as_view()),
    # path('category/<id>/', CategoryDetails.as_view())
    
    # # normal path: 
    # path('category/', category_list),
    # path('category/<id>/', category_detail)
]