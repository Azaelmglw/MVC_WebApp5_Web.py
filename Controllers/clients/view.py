import web
import Controllers.config as config

class View:
    def __init__(self):
        pass
    
    def GET(self, c_id):
        selected_client = config.model_clients.select_client(c_id)
        return config.render1.view(selected_client)