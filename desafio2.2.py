
import tkinter as tk
from tkinter import ttk

# Classe Atleta e funções principais
class Atleta:
    def __init__(self, nome, notas, manobras_selecionadas):
        self.nome = nome
        self.notas = notas
        self.media = self.calcular_media()
        self.manobras_selecionadas = manobras_selecionadas

    def calcular_media(self):
        # Remove a menor e a maior nota para calcular a média
        notas_validas = sorted(self.notas)[1:-1]
        return sum(notas_validas) / len(notas_validas) if notas_validas else 0

    def __repr__(self):
        return f'{self.nome}: {self.media:.2f}'

def registrar_notas(manobras_disponiveis):
    atletas = []
    num_atletas = int(input("Quantos atletas estão competindo? "))
    for i in range(num_atletas):
        nome = input(f"Nome do atleta {i + 1}: ")
        # Seleção de manobras
        print("Selecione as manobras que o atleta executou (digite os números separados por vírgula): ")
        for idx, manobra in enumerate(manobras_disponiveis, start=1):
            print(f"{idx}: {manobra}")
        selecao = input("Selecione as manobras: ")
        manobras_selecionadas = [manobras_disponiveis[int(num) - 1] for num in selecao.split(",")]

        notas = [float(input(f"Digite a nota {j + 1} para {nome}: ")) for j in range(5)]
        atletas.append(Atleta(nome, notas, manobras_selecionadas))
    return atletas

def pontuar_competicao(atletas):
    atletas_ordenados = sorted(atletas, key=lambda atleta: atleta.media, reverse=True)
    for i in range(len(atletas_ordenados) - 1):
        if atletas_ordenados[i].media == atletas_ordenados[i + 1].media:
            notas1 = sorted(atletas_ordenados[i].notas, reverse=True)
            notas2 = sorted(atletas_ordenados[i + 1].notas, reverse=True)
            if notas2 > notas1:
                atletas_ordenados[i], atletas_ordenados[i + 1] = atletas_ordenados[i + 1], atletas_ordenados[i]
    return atletas_ordenados

# Função para exibir o ranking e manobras em uma interface gráfica
def mostrar_interface_grafica(atletas, manobras_disponiveis):
    # Configuração da janela principal
    root = tk.Tk()
    root.title("Competição de Skate")
    root.geometry("500x400")

    # Criação do Notebook (conjunto de abas)
    notebook = ttk.Notebook(root)
    notebook.pack(pady=10, expand=True)

    # Aba de Manobras
    tab_manobras = ttk.Frame(notebook)
    notebook.add(tab_manobras, text="Manobras")

    # Exibir as manobras na aba "Manobras"
    label_titulo = tk.Label(tab_manobras, text="Manobras Disponíveis:", font=("Arial", 14, "bold"))
    label_titulo.pack(pady=10)

    for manobra in manobras_disponiveis:
        label = tk.Label(tab_manobras, text=manobra, font=("Arial", 12))
        label.pack(anchor="w", padx=10, pady=2)

    # Aba de Relatório
    tab_relatorio = ttk.Frame(notebook)
    notebook.add(tab_relatorio, text="Relatório")

    # Exibir o ranking dos atletas na aba "Relatório"
    label_titulo_relatorio = tk.Label(tab_relatorio, text="Ranking dos Atletas:", font=("Arial", 14, "bold"))
    label_titulo_relatorio.pack(pady=10)

    for pos, atleta in enumerate(atletas, start=1):
        label = tk.Label(
            tab_relatorio,
            text=f"{pos}º lugar - {atleta.nome}: Média {atleta.media:.2f} | Manobras: {', '.join(atleta.manobras_selecionadas)}",
            font=("Arial", 12)
        )
        label.pack(anchor="w", padx=10, pady=5)

        # Separação entre atletas
        separador = tk.Label(tab_relatorio, text="-" * 75)
        separador.pack(anchor="w", padx=10)

    # Iniciar o loop principal da interface
    root.mainloop()

# Execução do programa
manobras_disponiveis = [
    "Nollie Flip Backside Tail Slide",
    "Switch Kickflip Frontside Nosegrind",
    "360 Flip Crooked Grind",
    "Hardflip Backside 5-0",
    "Bigspin Flip Frontside Boardslide"
]

atletas = registrar_notas(manobras_disponiveis)
ranking = pontuar_competicao(atletas)

# Exibir o ranking final no terminal
print("\n====================================== Ranking Final ========================================")
for pos, atleta in enumerate(ranking, start=1):
    print(f"\n{pos}º lugar:")
    print(f"Nome: {atleta.nome}")
    print(f"Média: {atleta.media:.2f}")
    print(f"Manobras Selecionadas: {', '.join(atleta.manobras_selecionadas)}")
    print("-" * 100)  # Linha de separação entre cada atleta

# Mostrar o ranking e manobras na interface gráfica
mostrar_interface_grafica(ranking, manobras_disponiveis)

#atividade feita pela equipe TEMPESTADE DE IDEIAS:
#Tiago, Vinicius, Leandro, Lauany, Ana Caroline