import web
import Controllers.config as config


class Insert:
    def __init__(self):
        pass
    
    def GET(self):
        return config.render2.insert()

    def POST(self):
        input_field = web.input()
        name = input_field['name']
        description = input_field['description']
        brand = input_field['brand']
        origin = input_field['origin']
        config.model_products.insert_product(name, description, brand, origin)
        raise web.seeother('/')