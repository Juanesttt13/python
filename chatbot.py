import unidecode
respuestas = {
    "hola":"Hola, espero que este teniendo un excelente día",
    "bien y tu": "¡Me alegro!, yo estoy excelente",
    "¿sabes donde puedo encontrar curso de progamación gratis": "Claro, hay muchas opciones, pero te recomiendo el curso de TalentoTech",
    "en donde se ubican ellos?": "TalentoTech se ubica en la ciudad de Bucaramanga, Sanatander",


}


def obtener_respuesta(mensaje):
    mensaje = unidecode.unidecode(mensaje.lower())
    mensaje= mensaje.lower()
    for clave in respuestas:
        if unidecode.unidecode(clave.lower()) == mensaje:
            return respuestas[clave]
    if mensaje in respuestas:
        return respuestas[mensaje]
    else:
        return "no se que me tratas de decir, ¿puedes explicarte mejor?"

print("¡Hola! Soy quien podrá resolver algunas de las dudas que tengas")
while True:
    pregunta = input("¿En qué puedo ayudarte hoy? ")
    if pregunta == "salir":
        break
    print(obtener_respuesta(pregunta)) 