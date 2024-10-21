import pdfplumber
import pandas as pd

# Função para extrair informações específicas de uma nota fiscal
def extrair_informacoes_pdf(caminho_pdf):
    try:
        with pdfplumber.open(caminho_pdf) as pdf:
            texto = ""
            # Itera por todas as páginas do PDF e extrai o texto
            for pagina in pdf.pages:
                texto_pagina = pagina.extract_text()
                if texto_pagina:
                    texto += texto_pagina
        
        # Exibir o texto extraído para análise
        print("Texto extraído do PDF:\n", texto)

        # Ajustando a extração de CNPJ e número da nota (exemplo simples)
        cnpj = ""
        numero_nota = ""

        if "CNPJ" in texto:
            cnpj = texto.split("CNPJ")[1].split()[0]  # Pega a primeira palavra após "CNPJ"
        if "Número" in texto:
            numero_nota = texto.split("Número")[1].split()[0]  # Pega a primeira palavra após "Número"

        print(f"CNPJ: {cnpj}")
        print(f"Número da Nota: {numero_nota}")

        # Retornar as informações como dicionário
        return {
            "CNPJ": cnpj,
            "Número da Nota": numero_nota
        }
    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")
        return None

# Função para salvar uma informação em uma célula específica no Excel
def salvar_na_celula(dados, caminho_excel, linha, coluna):
    try:
        # Verificar se o arquivo já existe
        try:
            df = pd.read_excel(caminho_excel)
        except FileNotFoundError:
            # Se não existir, criar um DataFrame vazio
            df = pd.DataFrame()

        # Expandir o DataFrame caso necessário
        max_rows, max_cols = df.shape
        if max_rows < linha + 1:
            for _ in range(linha + 1 - max_rows):
                df = df.append(pd.Series([None]*max_cols), ignore_index=True)
        if max_cols < coluna + 1:
            for col in range(max_cols, coluna + 1):
                df[col] = None

        # Salvar os dados na célula específica
        df.iat[linha, coluna] = dados

        # Salvar o DataFrame no arquivo Excel
        df.to_excel(caminho_excel, index=False)
        print(f"Informação '{dados}' salva na célula [{linha}, {coluna}] do arquivo {caminho_excel}.")
    except Exception as e:
        print(f"Erro ao salvar no Excel: {e}")

# Caminho do PDF da nota fiscal e o caminho onde salvar o arquivo Excel
caminho_pdf = r"C:\Users\LEANDRO\Desktop\Nova pasta (6)\download(2).pdf"  # Substitua pelo caminho real do seu PDF
caminho_excel = r"C:\Users\LEANDRO\Desktop\Nova pasta (6)\Pasta1.xlsx"  # Substitua pelo caminho do Excel

# Extrair informações e salvar no Excel
dados_nota = extrair_informacoes_pdf(caminho_pdf)

if dados_nota:
    # Salvando CNPJ na célula [1, 0] (linha 2, coluna A) e Número da Nota na célula [1, 1] (linha 2, coluna B)
    salvar_na_celula(dados_nota["CNPJ"], caminho_excel, 1, 0)
    salvar_na_celula(dados_nota["Número da Nota"], caminho_excel, 1, 1)
else:
    print("Não foi possível extrair as informações da nota fiscal.")
