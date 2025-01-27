from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    carga_horaria: int

cursos_db = []
current_id = 1

@app.get("/cursos", response_model=List[Curso])
def listar_cursos():
    return cursos_db

@app.get("/cursos/{id}", response_model=Curso)
def obter_curso(id: int):
    curso = next((curso for curso in cursos_db if curso.id == id), None)
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return curso

@app.post("/cursos", response_model=Curso, status_code=201)
def criar_curso(curso: Curso):
    global current_id
    curso.id = current_id
    current_id += 1
    cursos_db.append(curso)
    return curso

@app.put("/cursos/{id}", response_model=Curso)
def atualizar_curso(id: int, curso_atualizado: Curso):
    curso = next((curso for curso in cursos_db if curso.id == id), None)
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    curso.titulo = curso_atualizado.titulo
    curso.descricao = curso_atualizado.descricao
    curso.carga_horaria = curso_atualizado.carga_horaria
    return curso

@app.delete("/cursos/{id}", status_code=204)
def excluir_curso(id: int):
    curso = next((curso for curso in cursos_db if curso.id == id), None)
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    cursos_db.remove(curso)
    return None

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)