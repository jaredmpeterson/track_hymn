import track_hymn.infrastructure.static_cache as static_cache
from track_hymn.infrastructure.suppressor import suppress
import pyramid.httpexceptions as exc
import track_hymn.infrastructure.cookie_auth as cookie_auth

# import pyramid.renderers
from track_hymn.services.account_service import AccountService


class BaseController:
    def __init__(self, request):
        self.request = request
        self.build_cache_id = static_cache.build_cache_id

        # layout_render = pyramid.renderers.get_renderer('track_hymn:templates/layout.pt')
        # impl = layout_render.implementation()
        # self.layout = impl.macros['layout']

    @property
    def is_logged_in(self):
        return cookie_auth.get_user_id_via_cookie(self.request) is not None

    def redirect(self, to_url, permanent=False):
        if permanent:
            raise exc.HTTPMovedPermanently(to_url)
        raise exc.HTTPFound(to_url)

    @property
    def auth_user_id(self):
        return cookie_auth.get_user_id_via_cookie(self.request)

    @property
    def current_user(self):
        uid = cookie_auth.get_user_id_via_cookie(self.request)
        if not uid:
            return None

        user = AccountService.find_userid(uid)
        return user
