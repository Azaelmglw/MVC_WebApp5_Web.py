import web
import Controllers.config as config

class Update:
    def __init__(self):
        pass

    def GET(self, c_id):
        selected_client = config.model_clients.select_client(c_id)
        return config.render1.update(selected_client)

    def POST(self, c_id):
        input_field = web.input()
        name = input_field['name']
        gender = input_field['gender']
        phone_number = input_field['phone_number']
        occupation = input_field['occupation']
        config.model_clients.update_client(c_id, name, gender, phone_number, occupation)
        raise web.seeother('/')