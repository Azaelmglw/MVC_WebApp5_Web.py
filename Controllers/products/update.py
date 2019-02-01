import web
import Controllers.config as config

class Update:
    def __init__(self):
        pass

    def GET(self, p_id):
        selected_product = config.model_products.select_product(p_id)
        return config.render2.update(selected_product)

    def POST(self, p_id):
        input_field = web.input()
        name = input_field['name']
        description = input_field['description']
        brand = input_field['brand']
        origin = input_field['origin']
        config.model_products.update_product(p_id, name, description, brand, origin)
        raise web.seeother('/')