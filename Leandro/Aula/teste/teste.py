from turtle import pd
import pdfplumber
import pandas as ad

from DevSec.Leandro.Aula.teste.teste1 import extrair_informacoes_pdf

def extrair_informações_pdf (caminho_pdf):
    with pdfplumber.open(caminho_pdf) as pdf:
        texto = ""
        for pagina in pdf.pages:
            texto+= pagina.extract_text()


    codigo_produto = ""
    descricao_produto = ""

    if "codigo" or "cod. prod" in texto:
        codigo_produto = texto.split("codigo")[1].split()[0]
    if "descrição" or "descrição do prod/serv." in texto:
        descricao_produto = texto.split("descrição" or "descrição do prod/serv.")[1].split()[0]
    
    return {
        "codigo" or "cod. prod": codigo_produto,
        "descrição" or "descrição do prod/serv.": descricao_produto
    }

# Função para salvar os dados no Excel
def salvar_no_excel(dados, caminho_excel):
    df = pd.DataFrame([dados])  # Converte os dados em DataFrame
    df.to_excel(caminho_excel, index=False)  # Salva no Excel

# Caminho do PDF da nota fiscal e o caminho onde salvar o arquivo Excel
caminho_pdf = "nota_fiscal.pdf"
caminho_excel = "informacoes_nota_fiscal.xlsx"

# Extrair informações e salvar no Excel
dados_nota = extrair_informacoes_pdf(caminho_pdf)
salvar_no_excel(dados_nota, caminho_excel)

print("Informações extraídas e salvas no arquivo Excel.")