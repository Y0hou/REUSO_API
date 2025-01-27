import requests

BASE_URL = "http://127.0.0.1:8000"

def listar_cursos():
    response = requests.get(f"{BASE_URL}/cursos")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao listar cursos: {response.status_code} - {response.text}")
        return []

def obter_curso(id):
    response = requests.get(f"{BASE_URL}/cursos/{id}")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao obter curso com ID {id}: {response.status_code} - {response.text}")
        return None

def criar_curso(titulo, descricao, carga_horaria):
    novo_curso = {
        "titulo": titulo,
        "descricao": descricao,
        "carga_horaria": carga_horaria
    }
    response = requests.post(f"{BASE_URL}/cursos", json=novo_curso)
    if response.status_code == 201:
        return response.json()
    else:
        print(f"Erro ao criar curso: {response.status_code} - {response.text}")
        return None

def atualizar_curso(id, titulo, descricao, carga_horaria):
    curso_atualizado = {
        "titulo": titulo,
        "descricao": descricao,
        "carga_horaria": carga_horaria
    }
    response = requests.put(f"{BASE_URL}/cursos/{id}", json=curso_atualizado)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao atualizar curso com ID {id}: {response.status_code} - {response.text}")
        return None

def excluir_curso(id):
    response = requests.delete(f"{BASE_URL}/cursos/{id}")
    if response.status_code == 204:
        return True
    else:
        print(f"Erro ao excluir curso com ID {id}: {response.status_code} - {response.text}")
        return False

if __name__ == "__main__":
    print("Listando cursos:")
    cursos = listar_cursos()
    for curso in cursos:
        print(curso)

    print("\nCriando um novo curso:")
    novo_curso = criar_curso("Python Avançado", "Curso avançado de Python", 40)
    if novo_curso:
        print("Curso criado com sucesso:", novo_curso)
    else:
        print("Falha ao criar curso.")

    print("\nAtualizando um curso:")
    curso_atualizado = atualizar_curso(1, "Python Avançado", "Curso avançado de Python com FastAPI", 50)
    if curso_atualizado:
        print("Curso atualizado com sucesso:", curso_atualizado)
    else:
        print("Falha ao atualizar curso.")

    print("\nObtendo detalhes de um curso:")
    curso = obter_curso(1)
    if curso:
        print("Detalhes do curso:", curso)
    else:
        print("Falha ao obter detalhes do curso.")

    print("\nExcluindo um curso:")
    if excluir_curso(1):
        print("Curso excluído com sucesso.")
    else:
        print("Falha ao excluir curso.")