from rest_framework import routers
from projects.api import ProjectViewSet

router = routers.DefaultRouter() # Allow to create all the crud

''' My Routes '''
router.register('api/projects', ProjectViewSet, 'projects')

''' Route's export '''
urlpatterns = router.urls