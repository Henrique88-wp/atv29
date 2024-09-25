# Crie um programa que receba uma lista com os nomes dos alunos presentes em uma aula e exiba quantos alunos estão presentes e a lista dos nomes. Se o total de alunos presentes for menor que 5, exiba uma mensagem sugerindo uma revisão da lista de chamada.

# Exemplo de entrada:
# Alunos presentes: ['Ana', 'Bruno', 'Carlos', 'Daniela']

# Exemplo de saída:
# Alunos presentes: 4
# Lista de alunos presentes: Ana, Bruno, Carlos, Daniela
# Aviso: Poucos alunos presentes. Revisar lista de chamada.

lista_presentes = []

while True:
    aluno = input("Digite o nome do aluno (ou 0 para terminar): ")
    if aluno == "0":
        break
    lista_presentes.append(aluno)

print(f"Alunos presentes: {len(lista_presentes)}")
print(lista_presentes)
print("Revise a lista de chamada" if len(lista_presentes) < 5 else "Só sucesso, bons estudos.")
