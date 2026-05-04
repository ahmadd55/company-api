from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet,EmployeeViewSet,RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router=DefaultRouter()

router.register(r'companies', CompanyViewSet)
router.register(r'employee', EmployeeViewSet)

urlpatterns = [

    path('', include(router.urls)),
    path('register/',RegisterView.as_view()),
    path('login/',TokenObtainPairView.as_view()),
    path('token/refresh',TokenRefreshView.as_view()),


]