#!/usr/bin/env python3
"""
Gerador de QR Code para acesso mobile
"""
import qrcode
import requests
import os

def get_public_ip():
    """Obtém o IP público"""
    try:
        response = requests.get('https://api.ipify.org', timeout=5)
        return response.text
    except:
        return "localhost"

def generate_qr_code(url, filename="site_qr.png"):
    """Gera um QR Code para a URL"""
    try:
        # Criar QR Code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)

        # Criar imagem
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(filename)
        
        print(f"📱 QR Code gerado: {filename}")
        print(f"🔗 URL: {url}")
        return True
    except Exception as e:
        print(f"❌ Erro ao gerar QR Code: {e}")
        return False

def main():
    """Função principal"""
    print("📱 Gerador de QR Code para acesso mobile")
    print("=" * 40)
    
    # URLs para gerar QR Codes
    urls = [
        ("http://localhost:8000", "site_local_qr.png"),
        ("http://172.30.0.2:8000", "site_rede_qr.png"),
        (f"http://{get_public_ip()}:8000", "site_public_qr.png")
    ]
    
    for url, filename in urls:
        print(f"\n🔗 Gerando QR Code para: {url}")
        if generate_qr_code(url, filename):
            print(f"✅ QR Code salvo como: {filename}")
        else:
            print(f"❌ Falha ao gerar QR Code para: {url}")
    
    print("\n📱 Como usar:")
    print("1. Abra a câmera do seu celular")
    print("2. Aponte para o QR Code")
    print("3. Clique no link que aparecer")
    print("4. Acesse o site no navegador do celular")

if __name__ == "__main__":
    main()