from fastapi import FastAPI
from models import RespuestaGeneTexto, PedirGeneTexto
from database import guardar_respuesta, ver_historial
from transformers import AutoTokenizer, AutoModelForCausalLM

app = FastAPI(title="Generador de Texto-Roams")

tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")




@app.post("/generar")
async def generar_texto(request: PedirGeneTexto):
    """

    """
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

        #guardar_respuesta(request.prompt, txt_generado)

        return {"prompt":request.prompt, "texto_generado":txt_generado}
    except:
        print("Error al ejecutar el modelo IA")


@app.get("/historial")
async def get_historial():
    return ver_historial()

#uvicorn main:app --reload
