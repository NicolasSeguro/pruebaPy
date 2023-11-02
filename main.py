import openai
import ast 
from datetime import datetime

# Define tu clave de API de OpenAI
api_key = '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'

# Configura la clave de API
openai.api_key = api_key

# Función para generar una tarea pendiente en formato de cadena
def generar_tarea_para_reunion(reunion, hora):
    # Define el prompt que solicita la tarea pendiente
    prompt = f"Genera una tarea pendiente para la reunión de {reunion} a las {hora}:"
    
    # Llama a la API de OpenAI para generar texto basado en el prompt
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=100
    )
    
    # Obtiene la respuesta generada por OpenAI y la formatea
    tarea_generada = f"[Pendiente] {response.choices[0].text.strip()}"
    
    return tarea_generada  # Devolvemos la tarea generada

# Función para definir el horario de la reunión utilizando ast.literal_eval()
def definir_horario_reunion():
    reunion = input("Ingrese el nombre de la reunión: ")
    hora = input("Ingrese la hora de la reunión (formato HH:MM): ")
    
    # Verificar si la hora ingresada es válida utilizando ast.literal_eval()
    try:
        ast.literal_eval(f"'{hora}'")
    except (SyntaxError, ValueError):
        print("La hora ingresada no es válida (debe estar en formato HH:MM).")
        return
    
    tarea_generada = generar_tarea_para_reunion(reunion, hora)
    
    # Imprime la tarea pendiente generada junto con el nombre de la reunión y la hora
    print(f"Tarea pendiente para la {reunion} a las {hora}: {tarea_generada}")
    
    # Crear un diccionario con la tarea pendiente, el nombre de la reunión y la hora
    tarea_dict = {
        "reunion": reunion,
        "hora": hora,
        "tarea_pendiente": tarea_generada
    }
    
    # Guardar el diccionario en un archivo JSON
    with open("tareas_pendientes.json", "a") as json_file:
        json.dump(tarea_dict, json_file)
    
if __name__ == "__main__":
    definir_horario_reunion()
