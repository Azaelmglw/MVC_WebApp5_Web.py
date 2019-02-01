import web
import Controllers.config as config

class Delete:
    def __init__(self):
        pass

    def GET(self, c_id):
        selected_client = config.model_clients.select_client(c_id)
        return config.render1.delete(selected_client)

    def POST(self, c_id):
        input_field = web.input()
        c_id = input_field['id']
        config.model_clients.delete_client(c_id)
        raise web.seeother('/')