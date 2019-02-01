import web
import config as config


class Index:
    def __init__(self):
        pass

    def GET(self):
        clients_data = config.model_clients.select_clients().list()
        products_data = config.model_products.select_products().list()
        return config.render.index(clients_data, products_data)