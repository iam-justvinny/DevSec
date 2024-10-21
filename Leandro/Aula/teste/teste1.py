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

        # Aqui você pode ajustar a extração conforme necessário
        # Exemplo de extração do CNPJ e número da nota fiscal
        cnpj = ""
        numero_nota = ""

        # Buscar CNPJ e número da nota
        if "CNPJ" in texto:
            cnpj = texto.split("CNPJ")[1].split()[0]  # Pega a primeira palavra após "CNPJ"
        if "Número" in texto:
            numero_nota = texto.split("Número")[1].split()[0]  # Pega a primeira palavra após "Número"

        # Exibir as informações extraídas
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

# Função para salvar os dados no Excel
def salvar_no_excel(dados, caminho_excel):
    try:
        # Converter as informações extraídas em DataFrame
        df = pd.DataFrame([dados])
        # Salvar no Excel
        df.to_excel(caminho_excel, index=False)
        print(f"Informações salvas no arquivo {caminho_excel}.")
    except Exception as e:
        print(f"Erro ao salvar no Excel: {e}")

# Caminho do PDF da nota fiscal e o caminho onde salvar o arquivo Excel
caminho_pdf = r"C:\Users\LEANDRO\Desktop\Nova pasta (6)\download(2).pdf"  # Substitua pelo caminho real do seu PDF
caminho_excel = r"C:\Users\LEANDRO\Desktop\Nova pasta (6)\Pasta1.xlsx"  # Substitua pelo caminho onde deseja salvar o Excel

# Extrair informações e salvar no Excel
dados_nota = extrair_informacoes_pdf(caminho_pdf)

if dados_nota:
    salvar_no_excel(dados_nota, caminho_excel)
else:
    print("Não foi possível extrair as informações da nota fiscal.")
