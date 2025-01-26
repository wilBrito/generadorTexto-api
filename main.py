from fastapi import FastAPI, HTTPException, Depends
from models import RespuestaGeneTexto, PedirGeneTexto
from database import guardar_respuesta, ver_historial
from transformers import AutoTokenizer, AutoModelForCausalLM
import logging
from security import verificar_token
from fastapi.security import  HTTPAuthorizationCredentials

# Configuración del logger
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("Logger")

app = FastAPI(title="Generador de Texto-Roams")

#Herramientas para la utilización del modelo IA
tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2")
model = AutoModelForCausalLM.from_pretrained("openai-community/gpt2")



#Método POST, envio del prompt y estructura-modelo para generarar texto
@app.post("/generar")
async def generar_texto(request: PedirGeneTexto, credenciales: HTTPAuthorizationCredentials = Depends(verificar_token)):
    """
    OBJ: Conseguir texto generado a partir de los datos proporcionados, siguiendo el modelo de models.py
    PRE: prompt no tiene que estar vacío
    """
    if not request.prompt.strip():
        logger.error("El prompt está vacío Error!!!!")
        return {"prompt":request.prompt, "texto_generado": "El prompt está vacío Error!!!!"}
    
    #Logger Solicitud
    logger.info(f"Solicitud: {request.prompt}")

    try:
        result = model.generate(
            tokenizer.encode(request.prompt, return_tensors='pt'),
            max_length = request.longitud,
            temperature = request.temperatura,
            do_sample=True,
            top_p = request.top_p,
            pad_token_id=tokenizer.eos_token_id
        )

        txt_generado = tokenizer.decode(result[0], skip_special_tokens=True)
        
        #Guardar en la base de datos
        guardar_respuesta(request.prompt, txt_generado)

        #Logger Respuesta
        logger.info(f"Respuesta: {txt_generado}")

        return {"prompt":request.prompt, "texto_generado":txt_generado}
    except:
        logger.error("Error al ejecutar el modelo IA")
        #print("Error al ejecutar el modelo IA")

#Método GET, extraer las consultas realizadas de la database
@app.get("/historial")
async def get_historial():
    return ver_historial()

