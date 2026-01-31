from django.urls import path

#from .views import  CategoryList, CategoryDetails # category_list, category_detail,
#from .views import CategoryAPIView, CategoryDetailAPIView
#from .views import CategoryViewSet, CategoryDetailViewset, CategoryModelViewSet
from .views import CategoryViewset, FoodViewset
from rest_framework import routers

#for routers
router = routers.DefaultRouter() #you  can use SimpleRouter() also instead of DefaultRouter()
#router = routers.DefaultRouter() #shows the links of routes
router.register('category', CategoryViewset, basename='mycategory')
router.register('food', FoodViewset, basename = 'myfood')

urlpatterns = [
    
    #for model view sets: 
    #   path('category/', CategoryModelViewSet.as_view({'get':'list', 'post':'create'})),
    #   path('category/<pk>/', CategoryModelViewSet.as_view({'get':'retrieve', 'put':'update', 'delete':'destroy' }))
    
    
    
    
    
    
    
    
    #for viewsets:
    # path('category/', CategoryViewSet.as_view({'get':'list', 'post':'create'})),
    # path('category/<pk>/', CategoryDetailViewset.as_view({'get':'retrieve'}))
    
    
    
    
    
    
    # for generics api: 
    # path('category/', CategoryAPIView.as_view()),
    # path('category/<pk>/', CategoryDetailAPIView.as_view()) # OR,
    #path('category/<str:name>/', CategoryDetailAPIView.as_view())  #need to add lookup field in class to use identifier other than pk like id, name
    
    
    
    
    

    
    # # for class based:
    # path('category/', CategoryList.as_view()),
    # path('category/<id>/', CategoryDetails.as_view())
    
    # # normal path: 
    # path('category/', category_list),
    # path('category/<id>/', category_detail)
] + router.urls