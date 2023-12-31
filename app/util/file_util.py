import os
import json
from app.model.enums.path_payload import PathPayload

here = os.path.dirname(os.path.abspath(__file__))


class FileUtil:

    ## Metodo que carrega o aquivo data.json da pasta payload
    ## para o formato json e com o encoding utf-8
    def get_payload(self, path: PathPayload):
        path = os.path.join(here, path.value)
        with open(path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data
