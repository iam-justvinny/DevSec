import pdfplumber

# Função para imprimir o texto extraído de cada página
def extrair_texto_pdf(caminho_pdf):
    try:
        with pdfplumber.open(caminho_pdf) as pdf:
            # Iterar por todas as páginas e exibir o texto de cada uma
            for i, pagina in enumerate(pdf.pages):
                texto = pagina.extract_text()
                if texto:
                    print(f"Texto da página {i+1}:\n{texto}\n{'-'*40}")
                else:
                    print(f"Não foi possível extrair texto da página {i+1}")
    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")

# Caminho do PDF da nota fiscal
caminho_pdf = r"C:\Users\LEANDRO\Desktop\Nova pasta (6)\download(2).pdf"

# Extrair e exibir o texto do PDF
extrair_texto_pdf(caminho_pdf)

import re

def extrair_informacoes_pdf(caminho_pdf):
    try:
        with pdfplumber.open(caminho_pdf) as pdf:
            texto = ""
            for pagina in pdf.pages:
                texto_pagina = pagina.extract_text()
                if texto_pagina:
                    texto += texto_pagina
        
        # Exibir o texto extraído para análise
        print("Texto completo extraído do PDF:\n", texto)

        # Ajustando a lógica de extração de CNPJ e Número da Nota com expressões regulares (regex)
        cnpj_pattern = r"\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}"  # Padrão do CNPJ
        numero_nota_pattern = r"\d{6,}"  # Número da Nota com 6 ou mais dígitos

        cnpj = re.search(cnpj_pattern, texto)
        numero_nota = re.search(numero_nota_pattern, texto)

        # Verificando se as informações foram encontradas
        cnpj = cnpj.group(0) if cnpj else "CNPJ não encontrado"
        numero_nota = numero_nota.group(0) if numero_nota else "Número da Nota não encontrado"

        print(f"CNPJ: {cnpj}")
        print(f"Número da Nota: {numero_nota}")

        # Retornar as informações extraídas
        return {
            "CNPJ": cnpj,
            "Número da Nota": numero_nota
        }
    except Exception as e:
        print(f"Erro ao processar o PDF: {e}")
        return None