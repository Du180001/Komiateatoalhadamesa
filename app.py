import requests
from bs4 import BeautifulSoup

session = requests.Session()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

URL = "http://200.133.203.133/home"

def send_form(pt_id):
    try:
        response = session.get(URL, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        csrf_element = soup.find("input", {'name': 'csrfmiddlewaretoken'})

        if not csrf_element or not csrf_element.get('value'):
            print("[!] Não foi possível localizar o csrfmiddlewaretoken na página.")
            return False
        
        csrf_token = csrf_element["value"]
        print(f"[-] Token CSRF obtido: {csrf_token[:10]}...")

        form_data = {
            "csrfmiddlewaretoken": csrf_token,
            "prontuario": pt_id,
            "tipo": "1"
        }

        headers_post = headers.copy()
        headers_post["Referer"] = URL

        response_post = session.post(URL, data=form_data, headers=headers_post, timeout=10)
        print(f"[-] Status do envio: {response_post.status_code}")

        if response_post.status_code == 200:
            print("[+] Formulário submetido com sucesso!")

    except requests.exceptions.RequestException as e:
        print(f"[!] Erro durante a comunicação: {e}")

if __name__ == "__main__":
    send_form("PT304775X")