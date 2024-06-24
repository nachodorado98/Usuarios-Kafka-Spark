import requests
from typing import Dict, Optional

def obtenerContenidoAPI()->Optional[Dict]:

	respuesta=requests.get("https://randomuser.me/api/")

	if respuesta.status_code!=200:

		raise Exception("Error en la respuesta")

	return respuesta.json()

def obtenerUsuarioLimpio(contenido:Dict)->Dict:

	usuario_limpio={}

	usuario=contenido["results"][0]

	localizacion=usuario["location"]

	usuario_limpio["nombre"]=usuario["name"]["first"]

	usuario_limpio["apellido"]=usuario["name"]["last"]

	usuario_limpio["genero"]=usuario["gender"]

	calle=f"{str(localizacion['street']['number'])} {localizacion['street']['name']},"

	ciudad=f"{localizacion['city']}, {localizacion['state']}, {localizacion['country']}"

	usuario_limpio["direccion"]=f"{calle} {ciudad}"

	usuario_limpio["codigo_postal"]=localizacion["postcode"]
								
	usuario_limpio["correo"]=usuario["email"]

	usuario_limpio["usuario"]=usuario["login"]["username"]

	usuario_limpio["fecha_nacimiento"]=usuario["dob"]["date"].split("T")[0]

	usuario_limpio["fecha_registro"]=usuario["registered"]["date"].split("T")[0]

	usuario_limpio["telefono"]=usuario["phone"]

	usuario_limpio["imagen"]=usuario["picture"]["medium"]

	return usuario_limpio

def obtenerUsuarioAPI()->Optional[Dict]:

	try:

	    contenido=obtenerContenidoAPI()

	    return obtenerUsuarioLimpio(contenido)

	except Exception:

		raise Exception("Error al obtener el usuario de la API")