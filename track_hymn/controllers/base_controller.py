import track_hymn.infrastructure.static_cache as static_cache
from track_hymn.infrastructure.suppressor import suppress
import pyramid.httpexceptions as exc


# import pyramid.renderers


class BaseController:
    def __init__(self, request):
        self.request = request
        self.build_cache_id = static_cache.build_cache_id

        # layout_render = pyramid.renderers.get_renderer('track_hymn:templates/layout.pt')
        # impl = layout_render.implementation()
        # self.layout = impl.macros['layout']

    @property
    def is_logged_in(self):
        return False

    @suppress
    def testing_base(self):
        print("testing base controller")

    def redirect(self, to_url, permanent=False):
        if permanent:
            raise exc.HTTPMovedPermanently(to_url)
        raise exc.HTTPFound(to_url)
