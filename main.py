from app.services.unidades_federativas_service import UnidadesFederativasServices
from app.services.tipo_de_pessoas_service import TipoDePessoasService
from flask import Flask, jsonify, request
from app.util.file_util import FileUtil
from model.enums.path_payload import PathPayload

app = Flask(__name__)
uf_service = UnidadesFederativasServices()
tipo_de_pessoas_service = TipoDePessoasService()
file_util = FileUtil()
payload = file_util.get_payload(PathPayload.UF)


@app.route('/api/v1/uf/listar_todas_as_ufs', methods=['GET'])
def listar_todas_as_ufs():
    response = uf_service.obter_listagem_uf()
    return jsonify(response['mensagem']), response['codigo']


@app.route('/api/v1/uf/listar_uf_por_sigla', methods=['GET'])
def listar_uf_por_sigla():
    sigla = request.args.get("sigla")
    response = uf_service.obter_unidade_federativa_por_sigla(sigla=sigla)
    return jsonify(response['mensagem']), response['codigo']


@app.route('/api/v1/uf/listar_uf_por_codigo_ibge', methods=['GET'])
def listar_uf_por_codigo_ibge():
    codigo_ibge = request.args.get("codigo_ibge")
    response = uf_service.obter_unidade_federativa_codigo_ibge(codigo_ibge=codigo_ibge)
    return jsonify(response['mensagem']), response['codigo']


@app.route('/api/v1/tipo_de_pessoas/listar_os_tipos_de_pessoas', methods=['GET'])
def listar_os_tipos_de_pessoas():
    response = tipo_de_pessoas_service.obter_os_tipos_de_pessoas()
    return jsonify(response['mensagem']), response['codigo']


@app.route('/api/v1/tipo_de_pessoas/listar_tipo_de_pessoa_por_abreviacao', methods=['GET'])
def listar_tipo_de_pessoa_por_abreviacao():
    abreviacao = request.args.get("abreviacao")
    response = tipo_de_pessoas_service.obter_tipo_de_pessoa_por_abreviacao(abreviacao=abreviacao)
    return jsonify(response['mensagem']), response['codigo']


@app.route('/api/v1/tipo_de_pessoas/listar_tipo_de_pessoa_por_tipo_documento', methods=['GET'])
def listar_tipo_de_pessoa_por_tipo_de_documento():
    tipo_de_documento = request.args.get("tipo_de_documento")
    response = tipo_de_pessoas_service.obter_tipo_de_pessoa_por_tipo_de_documento(tipo_de_documento=tipo_de_documento)
    return jsonify(response['mensagem']), response['codigo']


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(port=5000, debug=True, host='localhost')
