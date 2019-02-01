import web
import Controllers.config as config

class Delete:
    def __init__(self):
        pass

    def GET(self, p_id):
        selected_product = config.model_products.select_product(p_id)
        return config.render2.delete(selected_product)

    def POST(self, p_id):
        input_field = web.input()
        p_id = input_field['id']
        config.model_products.delete_product(p_id)
        raise web.seeother('/')
