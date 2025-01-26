from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()
API_TOKEN = "ROAMS"

def verificar_token(credenciales: HTTPAuthorizationCredentials = Depends(security)):
    if credenciales.credentials != API_TOKEN:
        raise HTTPException(
            status_code=401, 
            detail="Token de autenticación inválido."
        )