print('\n =================================================Simulador de Investimentos=============================================')

print('\nOlá seja bem-vindo, temos os melhores investimentos para você, confira!')
print("-" * 120)

# Função para determinar o perfil do investidor
def determinar_perfil_investidor():
    print('\nResponda abaixo para descobrir o seu perfil investidor:')
    print("-" * 120) 

    experiencia = input("Qual é o seu nível de experiência em investimentos? (Iniciante, Intermediário, Avançado): ").strip().lower()
    tolerancia_risco = input("Qual é a sua tolerância ao risco? (Baixa, Média, Alta): ").strip().lower()
    objetivo = input("Qual é o seu principal objetivo de investimento? (Preservação de capital, Crescimento moderado, Alto crescimento): ").strip().lower()
    
    # Avaliação para definir o perfil
    pontos = 0
    if experiencia == "iniciante":
        pontos += 1
    elif experiencia == "intermediário":
        pontos += 2
    elif experiencia == "avançado":
        pontos += 3

    if tolerancia_risco == "baixa":
        pontos += 1
    elif tolerancia_risco == "média":
        pontos += 2
    elif tolerancia_risco == "alta":
        pontos += 3

    if objetivo == "preservação de capital":
        pontos += 1
    elif objetivo == "crescimento moderado":
        pontos += 2
    elif objetivo == "alto crescimento":
        pontos += 3

    if pontos <= 4:
        perfil = "conservador"
    elif 5 <= pontos <= 6:                                                                                                                                                                              
        perfil = "moderado"
    else:
        perfil = "arrojado"

    print(f"O seu perfil de investidor é: {perfil.capitalize()}")
    return perfil

# Função para exibir as opções de investimento
def exibir_opcoes_investimento(perfil):
    investimentos = {
        "conservador": {
            "Opções": [
                {
                    "Nome": "Poupança",
                    "Tempo mínimo de resgate": "Imediato",
                    "Taxa de retorno mensal": 0.5,
                    "Taxa de retorno anual": 6.17,
                    "Retorno acumulado em 5 anos": lambda taxa: (1 + taxa/100)**60 - 1
                }
            ],
            "Descrição": "Investimentos de baixo risco para segurança do capital."
        },
        "moderado": {
            "Opções": [
                {
                    "Nome": "Renda Fixa",
                    "Tempo mínimo de resgate": "1 ano",
                    "Taxa de retorno mensal": 1.0,
                    "Taxa de retorno anual": 12.68,
                    "Retorno acumulado em 5 anos": lambda taxa: (1 + taxa/100)**60 - 1
                }
            ],
            "Descrição": "Investimentos de risco moderado, balanceando segurança e retorno."
        },
        "arrojado": {
            "Opções": [
                {
                    "Nome": "Ações ou criptomoedas",
                    "Tempo mínimo de resgate": "5 anos",
                    "Taxa de retorno mensal": 2.5,
                    "Taxa de retorno anual": 34.49,
                    "Retorno acumulado em 5 anos": lambda taxa: (1 + taxa/100)**60 - 1
                }
            ],
            "Descrição": "Investimentos de alto risco, voltados para maior rentabilidade."
        }
    }

    if perfil in investimentos:
        print(f"\nPerfil: {perfil.capitalize()}")
        print(investimentos[perfil]["Descrição"])
        print("Opções de investimento:")
        
        for opcao in investimentos[perfil]["Opções"]:
            retorno_acumulado = opcao["Retorno acumulado em 5 anos"](opcao["Taxa de retorno mensal"])
            print(f"\n  - {opcao['Nome']}")
            print(f"    Tempo mínimo de resgate: {opcao['Tempo mínimo de resgate']}")
            print(f"    Taxa de retorno mensal: {opcao['Taxa de retorno mensal']}%")
            print(f"    Taxa de retorno anual: {opcao['Taxa de retorno anual']}%")
            print(f"    Retorno acumulado em 5 anos: {retorno_acumulado * 100:.2f}%")
    else:
        print("Perfil inválido. Escolha entre conservador, moderado ou arrojado.")

# Função para gerar e imprimir o relatório do investimento
def gerar_relatorio(perfil):
    investimentos = {
        "conservador": {
            "Opções": [
                {
                    "Nome": "Poupança",
                    "Tempo mínimo de resgate": "Imediato",
                    "Taxa de retorno mensal": 0.5,
                    "Taxa de retorno anual": 6.17,
                    "Retorno acumulado em 5 anos": lambda taxa: (1 + taxa/100)**60 - 1
                }
            ],
            "Descrição": "Investimentos de baixo risco para segurança do capital."
        },
        "moderado": {
            "Opções": [
                {
                    "Nome": "Renda Fixa",
                    "Tempo mínimo de resgate": "1 ano",
                    "Taxa de retorno mensal": 1.0,
                    "Taxa de retorno anual": 12.68,
                    "Retorno acumulado em 5 anos": lambda taxa: (1 + taxa/100)**60 - 1
                }
            ],
            "Descrição": "Investimentos de risco moderado, balanceando segurança e retorno."
        },
        "arrojado": {
            "Opções": [
                {
                    "Nome": "Ações ou criptomoedas",
                    "Tempo mínimo de resgate": "5 anos",
                    "Taxa de retorno mensal": 2.5,
                    "Taxa de retorno anual": 34.49,
                    "Retorno acumulado em 5 anos": lambda taxa: (1 + taxa/100)**60 - 1
                }
            ],
            "Descrição": "Investimentos de alto risco, voltados para maior rentabilidade."
        }
    }

    if perfil in investimentos:
        print(f"\nRELATÓRIO DE INVESTIMENTO - Perfil: {perfil.capitalize()}")
        print("=" * 120)
        print(f"Descrição: {investimentos[perfil]['Descrição']}")
        
        for opcao in investimentos[perfil]["Opções"]:
            retorno_acumulado = opcao["Retorno acumulado em 5 anos"](opcao["Taxa de retorno mensal"])
            print("\nOpção de Investimento:")
            print(f"  - Nome: {opcao['Nome']}")
            print(f"  - Tempo mínimo de resgate: {opcao['Tempo mínimo de resgate']}")
            print(f"  - Taxa de retorno mensal: {opcao['Taxa de retorno mensal']}%")
            print(f"  - Taxa de retorno anual: {opcao['Taxa de retorno anual']}%")
            print(f"  - Retorno acumulado em 5 anos: {retorno_acumulado * 100:.2f}%")
        print("=" * 120)

# Execução principal
while True:
    perfil = determinar_perfil_investidor()
    exibir_opcoes_investimento(perfil)

    # Pergunta se o usuário deseja gerar o relatório
    gerar_relatorio_resposta = input("Você deseja gerar um relatório do investimento? (sim/não): ").strip().lower()
    if gerar_relatorio_resposta == "sim":
        gerar_relatorio(perfil)
    
    # Pergunta se o usuário deseja escolher outro perfil
    continuar = input("Você deseja escolher outro perfil de investidor? (sim/não): ").strip().lower()
    if continuar != "sim":
        print("Obrigado por usar o simulador de investimentos! Até logo!")
        break