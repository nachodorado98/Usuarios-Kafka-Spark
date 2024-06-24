import pytest
import requests_mock

from src.extraer_data_api import obtenerContenidoAPI, obtenerUsuarioLimpio, obtenerUsuarioAPI

def test_obtener_contenido_api_error(requests_mock):

    requests_mock.get("https://randomuser.me/api/", status_code=404)

    with pytest.raises(Exception, match="Error en la respuesta"):

        obtenerContenidoAPI()

def test_obtener_contenido_api():

    assert isinstance(obtenerContenidoAPI(), dict)

def test_obtener_usuario_limpio():

    contenido=obtenerContenidoAPI()

    usuario=obtenerUsuarioLimpio(contenido)

    assert isinstance(usuario, dict)
    assert len(usuario.keys())==11

def test_obtener_usuario_api_error(requests_mock):

    requests_mock.get("https://randomuser.me/api/", status_code=404)

    with pytest.raises(Exception, match="Error al obtener el usuario de la API"):

        obtenerUsuarioAPI()

def test_obtener_usuario_api():

    assert isinstance(obtenerUsuarioAPI(), dict)