from fastapi import FastAPI
from models import RespuestaGeneTexto, PedirGeneTexto
from database import create_db, guardar_respuesta, ver_historial
from transformers import AutoTokenizer, AutoModelForCausalLM

app = FastAPI(title="Generador de Texto-Roams")

tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")




@app.post("/generar")
async def generar_texto(respuesta: RespuestaGeneTexto):
    """

    """
    try:
        result = model.generate(
            tokenizer.encode(respuesta.prompt),
            max_length = respuesta.longitud,
            temperature = respuesta.temperatura,
            top_p = respuesta.top_p,
            pad_token_id=tokenizer.eos_token_id
        )

        txt_generado = result[0]["generated_text"]
        guardar_respuesta(respuesta.prompt, txt_generado)

        return {"prompt":respuesta.prompt, "texto_generado":txt_generado}
    except:
        print("Error al ejecutar el modelo IA")


@app.get("/historial")
async def get_historial():
    return ver_historial()
    
