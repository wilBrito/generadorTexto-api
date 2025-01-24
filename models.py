from pydantic import BaseModel, Field
"""
Empleamos la librería pydantic para la validación y estandarización de datos 
"""

class PedirGeneTexto(BaseModel):
    """
    OBJ: Dotar de una estructura determinada al texto que se va a pedir, generado por el modelo IA
    PRE: Configurar parámetros opcionales del modelo, como longitud máxima del texto generado, temperatura, y top-p.
    """
    prompt: str = Field(..., min_length=1 , description="Texto inicial")
    longitud: int = Field(50,ge=1, le=300, description="Rango (número) de las palabras generadas")
    temperatura: float = Field(1.0,ge=0.0, le=1.0, description="Aleatoriedad de la respuesta")
    top_p: float = Field(1.0,ge=0.0, le=1.0, description="Alternativa a temperatura")


class RespuestaGeneTexto(BaseModel):
    """
    OBJ: Recibir la respuesta generada por el modelo IA
    """
    prompt : str
    texto_generado : str