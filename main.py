from fastapi import FastAPI, HTTPException
from models import RespuestaGeneTexto, PedirGeneTexto
from database import guardar_respuesta, ver_historial
from transformers import AutoTokenizer, AutoModelForCausalLM

app = FastAPI(title="Generador de Texto-Roams")

#Herramientas para la utilización del modelo IA
tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2")
model = AutoModelForCausalLM.from_pretrained("openai-community/gpt2")



#Método POST, envio del prompt y estructura-modelo para generarar texto
@app.post("/generar")
async def generar_texto(request: PedirGeneTexto):
    """
    OBJ: Conseguir texto generado a partir de los datos proporcionados, siguiendo el modelo de models.py
    PRE: prompt no tiene que estar vacío
    """
    if not request.prompt.strip():
        return {"prompt":request.prompt, "texto_generado": "El prompt está vacío Error!!!!"}

    try:
        result = model.generate(
            tokenizer.encode(request.prompt, return_tensors='pt'),
            max_length = request.longitud,
            temperature = request.temperatura,
            do_sample=True,
            top_p = request.top_p,
            pad_token_id=tokenizer.eos_token_id
        )

        #print(result)
        txt_generado = tokenizer.decode(result[0], skip_special_tokens=True)
        #print(txt_generado)

        #Guardar en la base de datos
        guardar_respuesta(request.prompt, txt_generado)

        return {"prompt":request.prompt, "texto_generado":txt_generado}
    except:
        print("Error al ejecutar el modelo IA")

#Método GET, extraer las consultas realizadas de la database
@app.get("/historial")
async def get_historial():
    return ver_historial()

