from app.model.enums.path_payload import PathPayload
from app.util.file_util import FileUtil

file_util = FileUtil()
payload = file_util.get_payload(PathPayload.TIPO_DE_PESSOAS)

tipos_de_pessoas = payload['tipos_de_pessoas']


class TipoDePessoasService:
    def obter_os_tipos_de_pessoas(self):
        try:
            response = tipos_de_pessoas
            if response is not None:
                return {
                    "level": "Sucesso",
                    "codigo": 200,
                    "mensagem": response
                }
            else:
                return {
                    "level": "Erro",
                    "codigo": 404,
                    "mensagem": {
                        "mensagem_erro": "Não existem valores a serem consultados"
                    }
                }

        except Exception as e:
            paylad_error = {
                "Level": "Error",
                "Codigo": 500,
                "Mensagem": "Erro ao consultar a listagem de tipos de pessoas",
                "error": str(e)
            }

            return paylad_error

    def obter_tipo_de_pessoa_por_abreviacao(self, abreviacao):
        try:

            if abreviacao is not None and len(abreviacao) == 2:
                response = next((tipo_de_pessoa for tipo_de_pessoa in tipos_de_pessoas if
                                 tipo_de_pessoa['abreviacao'] == abreviacao), None)
                if response is not None:
                    return {
                        "level": "Sucesso",
                        "codigo": 200,
                        "mensagem": response
                    }
                else:
                    return {
                        "level": "Erro",
                        "codigo": 404,
                        "mensagem": {
                            "mensagem_erro": f"Nenhum resultado encontrado com o parâmetro {abreviacao} informado"
                        }
                    }
            else:
                return {
                    "level": "Erro",
                    "codigo": 400,
                    "mensagem": {
                        "mensagem_erro": f"requisição inválida para parâmetro informado: {abreviacao}"
                    }

                }
        except Exception as e:
            paylad_error = {
                "Level": "Error",
                "Codigo": 500,
                "Mensagem": "Erro ao consultar a uf por sigla",
                "error": str(e)
            }

            return paylad_error

    def obter_tipo_de_pessoa_por_tipo_de_documento(self, tipo_de_documento):
        try:

            if tipo_de_documento is not None:
                response = next((tipo_de_pessoa for tipo_de_pessoa in tipos_de_pessoas if
                                 tipo_de_pessoa['tipo_de_documento'] == tipo_de_documento), None)
                if response is not None:
                    return {
                        "level": "Sucesso",
                        "codigo": 200,
                        "mensagem": response
                    }
                else:
                    return {
                        "level": "Erro",
                        "codigo": 404,
                        "mensagem": {
                            "mensagem_erro": f"Nenhum resultado encontrado com o parâmetro {tipo_de_documento} informado"
                        }
                    }
            else:
                return {
                    "level": "Erro",
                    "codigo": 400,
                    "mensagem": {
                        "mensagem_erro": f"requisição inválida para parâmetro informado: {tipo_de_documento}"
                    }

                }
        except Exception as e:
            paylad_error = {
                "Level": "Error",
                "Codigo": 500,
                "Mensagem": "Erro ao consultar a uf por sigla",
                "error": str(e)
            }

            return paylad_error
