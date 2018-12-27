# notes/router.py
from rest_framework import routers
from .views import NoteViewSet

# Создаем router
router = routers.DefaultRouter()
# регистрируем наш ViewSet
router.register('notes', NoteViewSet)

# URLs настраиваются автоматически роутером
api_urls = router.urls
