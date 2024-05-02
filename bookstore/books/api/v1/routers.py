from rest_framework.routers import DefaultRouter

from books.api.v1.views import BookViewSet, AuthorViewSet, PublisherViewSet


router = DefaultRouter()
router.register('books', BookViewSet)
router.register('authors', AuthorViewSet)
router.register('publishers', PublisherViewSet)
