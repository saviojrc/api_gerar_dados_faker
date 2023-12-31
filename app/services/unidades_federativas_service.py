from app.model.enums.path_payload import PathPayload
from app.util.file_util import FileUtil


file_util = FileUtil()
payload = file_util.get_payload(PathPayload.UF)

unidades_federativas = payload['unidades_federativas']


class UnidadesFederativasServices:

    def obter_listagem_uf(self):
        try:
            response = payload
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
                "Mensagem": "Erro ao consultar a listagem de uf's",
                "error": str(e)
            }

            return paylad_error

    def obter_unidade_federativa_por_sigla(self, sigla):
        try:

            if sigla is not None and len(sigla) == 2:
                response = next((uf for uf in unidades_federativas if uf['uf'] == sigla), None)
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
                            "mensagem_erro": f"Nenhum resultado encontrado com o parâmetro {sigla} informado"
                        }
                    }
            else:
                return {
                    "level": "Erro",
                    "codigo": 400,
                    "mensagem": {
                        "mensagem_erro": f"requisição inválida para parâmetro informado: {sigla}"
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

    def obter_unidade_federativa_codigo_ibge(self, codigo_ibge):
        try:

            if codigo_ibge is not None:
                response = next((uf for uf in unidades_federativas if uf['codigo_ibge'] == codigo_ibge), None)
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
                            "mensagem_erro": f"Nenhum resultado encontrado com o parâmetro {codigo_ibge} informado"
                        }
                    }
            else:
                return {
                    "level": "Erro",
                    "codigo": 400,
                    "mensagem": {
                        "mensagem_erro": f"requisição inválida para parâmetro informado: {codigo_ibge}"
                    }

                }
        except Exception as e:
            paylad_error = {
                "Level": "Error",
                "Codigo": 500,
                "Mensagem": "Erro ao consultar a uf pelo código ibge",
                "error": str(e)
            }

            return paylad_error
