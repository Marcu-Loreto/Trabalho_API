# Trabalho_API
Repositório dos trabalhos da materia API - Pos graduação "Agentes inteligentes" UFG

 Este reposotório é destinado a guardar os trabalhos realizados durante a aula sobre desenvolvimento de APIs do Professor Rogerio Rodrigues Carvalho

Aqui está um texto explicativo sobre como instalar e configurar um ambiente virtual no Python para rodar uma API localmente:

---

# Configurando um Ambiente Virtual no Python para Rodar uma API Localmente

Para garantir que sua API rode em um ambiente isolado, sem conflitos com outras bibliotecas do sistema, é recomendável criar um ambiente virtual no Python. Siga os passos abaixo:

### 1. Verifique se o Python está instalado
Antes de começar, certifique-se de que o Python está instalado em sua máquina. Para verificar, execute o seguinte comando no terminal:

```bash
python --version
```
ou, dependendo do sistema:
```bash
python3 --version
```

Se não estiver instalado, baixe e instale o Python a partir de [python.org](https://www.python.org/).

### 2. Crie um Ambiente Virtual
Agora, no diretório onde deseja configurar seu projeto, execute o seguinte comando para criar um ambiente virtual:

No Windows:
```bash
python -m venv venv
```

No macOS/Linux:
```bash
python3 -m venv venv
```

Isso criará uma pasta chamada `venv`, que conterá todos os pacotes isolados do projeto.

### 3. Ative o Ambiente Virtual
Após a criação, ative o ambiente virtual com um dos comandos abaixo:

- **Windows (CMD/Powershell):**
  ```bash
  venv\Scripts\activate
  ```
  
- **Windows (Git Bash):**
  ```bash
  source venv/Scripts/activate
  ```

- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

Se a ativação for bem-sucedida, o terminal exibirá um prefixo `(venv)`, indicando que o ambiente virtual está ativo.

### 4. Instale as Dependências
Agora, instale as bibliotecas necessárias para rodar a API. Se você tiver um arquivo `requirements.txt`, use:

```bash
pip install -r requirements.txt
```

Se precisar instalar manualmente, use `pip install`:

```bash
pip install fastapi uvicorn
```

### 5. Rodando a API
Se estiver usando o **FastAPI**, crie um arquivo `main.py` com o seguinte código:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API funcionando!"}
```

Para iniciar a API localmente, execute:

```bash
uvicorn main:app --reload
```

Agora, a API estará rodando em `http://127.0.0.1:8000`.

### 6. Desativando o Ambiente Virtual
Quando terminar de trabalhar no projeto, desative o ambiente virtual com:

```bash
deactivate
```

Isso encerrará o uso do ambiente virtual e restaurará o ambiente padrão do sistema.

### Conclusão
Seguindo esses passos, você terá um ambiente virtual configurado para rodar sua API localmente, garantindo um ambiente de desenvolvimento organizado e livre de conflitos. 🚀
