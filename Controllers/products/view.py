import web
import Controllers.config as config

class View:
    def __init__(self):
        pass
    
    def GET(self, p_id):
        selected_product = config.model_products.select_product(p_id)
        return config.render2.view(selected_product)