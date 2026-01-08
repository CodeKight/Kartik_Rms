from django.urls import path

from .views import  CategoryAPIView, CategoryDetailAPIView #CategoryList, CategoryDetail #category_list, category_detail,

urlpatterns = [
    # path('/category/', category_list),
    # path('/category/<id>/',category_detail)
    # path('/category/', CategoryList.as_view()),
    # path('/category/<id>/',CategoryDetail.as_view())
    
    path('/category/', CategoryAPIView.as_view()),
    path('/category/<pk>/',CategoryDetailAPIView.as_view())
]   

