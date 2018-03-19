import os
from pyramid.config import Configurator

import track_hymn
import track_hymn.controllers.home_controller as home
import track_hymn.controllers.hymn_controller as hymn
import track_hymn.controllers.account_controller as acct
from track_hymn.data.dbsession import DBSessionFactory


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    init_includes(config)
    init_routing(config)
    init_database(config)
    return config.make_wsgi_app()


def init_routing(config):
    config.add_static_view('static', 'static', cache_max_age=3600)

    # config.add_route('home', '/')

    config.add_handler('root', '/', handler=home.HomeController, action='index')
    add_controller_routes(config, home.HomeController, 'home')
    add_controller_routes(config, hymn.HymnController, 'hymn')
    add_controller_routes(config, acct.AccountController, 'account')
    config.scan()


def add_controller_routes(config, ctrl, prefix):
    config.add_handler(prefix + 'ctrl_index', '/' + prefix, handler=ctrl, action='index')
    config.add_handler(prefix + 'ctrl_index/', '/' + prefix + '/', handler=ctrl, action='index')
    config.add_handler(prefix + 'ctrl', '/' + prefix + '/{action}', handler=ctrl)
    config.add_handler(prefix + 'ctrl/', '/' + prefix + '/{action}/', handler=ctrl)
    config.add_handler(prefix + 'ctrl_id', '/' + prefix + '/{action}/{id}', handler=ctrl)


def init_includes(config):
    config.include('pyramid_chameleon')
    config.include('pyramid_handlers')


def init_database(config):
    top_folder = os.path.dirname(track_hymn.__file__)
    rel_folder = os.path.join('db', 'track_hymn.sqlite')
    db_file = os.path.join(top_folder, rel_folder)
    DBSessionFactory.global_init(db_file)
