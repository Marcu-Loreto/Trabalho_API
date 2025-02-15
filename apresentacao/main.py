
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests #cnpj
#import json
import httpx
import logging


app = FastAPI(
    title='Capiva das Empresas',
    version='1.01',
    description='Projeto API - Prof. Rogério',
    summary='API para buscar informações de empresas direto da Receita Federal',
    terms_of_service="https://expertatech.com.br/termos//",
    contact={
        "name da equipe": "LL-Leandro Lima, RK -Ricardo Kerr, ML - Marcu Loreto",
        "url": "https://github.com/Marcu-Loreto/Projeto_API",
        "emails": "Leandrowaglima@gmail.com , ricardo.kerr@gmail.com , mlbonfim@gmail.com",      
    },
)


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

logger = logging.getLogger("Eu nas API")

logger.info("Mensagem informativa")
logger.warning("Mensagem de alerta")
logger.error("Mensagem de erro")
logger.critical("Mensagem crítica")
  
@app.post("/")
def hello_mundo():
        return {"message": "Hello, World!"} 




API_URL= f"https://minhareceita.org/" #URL da busca do CNPJ
@app.post ("/cnpj")
 
async def Busca_dados_da_empresa(cnpj: str):
    cnpj = re.sub(r'\D', '', cnpj) #recuperar apenas os numeros
    if not cnpj.isdigit() or len(cnpj) != 14:
        raise HTTPException(status_code=400, detail="CNPJ deve ter 14 dígitos numéricos.")
    
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_URL}{cnpj}")
        
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Erro ao buscar os dados.")
        
        return response.json()
    


