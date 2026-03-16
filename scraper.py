"""
Script de Web Scraping para buscar matérias de editais de concursos.
Uso: python scraper.py --concurso "Polícia Federal" --url "https://..."
"""
import requests
from bs4 import BeautifulSoup
import json
import argparse
import re

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

PALAVRAS_MATERIA = [
    'português', 'matemática', 'raciocínio lógico', 'direito constitucional',
    'direito administrativo', 'direito penal', 'informática', 'inglês',
    'conhecimentos gerais', 'atualidades', 'estatística', 'contabilidade',
    'economia', 'administração', 'legislação', 'ética'
]

def scrape_materias(url):
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        texto = soup.get_text(separator=' ').lower()
        encontradas = []
        for mat in PALAVRAS_MATERIA:
            if mat in texto:
                encontradas.append(mat.title())
        return encontradas
    except Exception as e:
        print(f"Erro ao acessar {url}: {e}")
        return []

def scrape_cebraspe(concurso_nome):
    """Busca editais no site do Cebraspe."""
    url = f"https://www.cebraspe.org.br/concursos"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(resp.text, 'html.parser')
        links = soup.find_all('a', href=True)
        resultados = []
        for link in links:
            if concurso_nome.lower() in link.text.lower():
                resultados.append({'titulo': link.text.strip(), 'url': link['href']})
        return resultados
    except Exception as e:
        print(f"Erro Cebraspe: {e}")
        return []

def gerar_json_materias(concurso, orgao, banca, materias):
    estrutura = {
        "concurso": concurso,
        "orgao": orgao,
        "banca": banca,
        "materias": [{"nome": m, "questoes": []} for m in materias]
    }
    nome_arquivo = f"data/{concurso.replace(' ', '_').lower()}.json"
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(estrutura, f, ensure_ascii=False, indent=2)
    print(f"Arquivo gerado: {nome_arquivo}")
    return estrutura

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scraper de editais de concursos')
    parser.add_argument('--url', help='URL do edital')
    parser.add_argument('--concurso', default='Concurso', help='Nome do concurso')
    parser.add_argument('--orgao', default='Órgão', help='Nome do órgão')
    parser.add_argument('--banca', default='Banca', help='Nome da banca')
    args = parser.parse_args()

    if args.url:
        print(f"Buscando matérias em: {args.url}")
        materias = scrape_materias(args.url)
        if materias:
            print(f"Matérias encontradas: {materias}")
            gerar_json_materias(args.concurso, args.orgao, args.banca, materias)
        else:
            print("Nenhuma matéria identificada.")
    else:
        print("Informe --url para buscar matérias de um edital.")
        print("Exemplo: python scraper.py --url https://site.com/edital.pdf --concurso 'PF 2024'")
