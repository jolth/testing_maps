import web

urls = (
    '/', 'index',
    '/simple_map', 'simple_map',
    '/fullscreen_map', 'fullscreen_map',
    '/mobile_map', 'mobile_map',
    '/interaction_map', 'interaction_map',
    '/base_maps', 'base_maps',
    '/styled_maps', 'styled_maps',
    '/tile_base_maps', 'tile_base_maps',
    '/tile_overlays', 'tile_overlays',
    '/toggle_overlay', 'toggle_overlay',
    '/image_overlays', 'image_overlays'
)
render = web.template.render('templates/')


class index(object):
    def GET(self):
        ch1_links = (['simple_map',
                      'Creating a simple map in a custom DIV element'],
                     ['fullscreen_map', 'Creating a simple fullscreen map'],
                     ['mobile_map', 'Moving from the Web to mobile devices'],
                     ['interaction_map',
                      'Changing map properties programmatically'],
                     ['base_maps', 'Changing base maps'])

        ch2_links = (['styled_maps', 'Styling of Google base maps'],
                     ['tile_base_maps',
                      'Using differentt tile sources as base mapas'],
                     ['tile_overlays', 'Adding tile overlays to maps'],
                     ['toggle_overlay', 'Toggle the overlay layers'],
                     ['image_overlays', 'Adding image overlays to maps'])

        return render.index(ch1_links, ch2_links)


class simple_map(object):
    def GET(self):
        return render.simple_map()


class fullscreen_map(object):
    def GET(self):
        return render.fullscreen_map()


class mobile_map(object):
    def GET(self):
        return render.mobile_map()


class interaction_map(object):
    def GET(self):
        return render.interaction_map()


class base_maps(object):
    def GET(self):
        return render.base_maps()


class styled_maps(object):
    def GET(self):
        return render.styled_maps()


class tile_base_maps(object):
    def GET(self):
        return render.tile_base_maps()


class tile_overlays(object):
    def GET(self):
        return render.tile_overlays()


class toggle_overlay(object):
    def GET(self):
        return render.toggle_overlay()


class image_overlays(object):
    def GET(self):
        return render.image_overlays()


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
