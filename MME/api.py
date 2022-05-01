from wagtail.api.v2.views import PagesAPIViewSet
from wagtail.api.v2.router import WagtailAPIRouter
from wagtail.documents.api.v2.views import DocumentsAPIViewSet


api_router = WagtailAPIRouter('mmeapi')


api_router.register_endpoint('pages', PagesAPIViewSet)
api_router.register_endpoint('documents', DocumentsAPIViewSet)
