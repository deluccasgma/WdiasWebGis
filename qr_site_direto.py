#!/usr/bin/env python3
"""
QR Code para o site direto
"""
import qrcode

def generate_qr_code(url, filename="site_direto_qr.png"):
    """Gera um QR Code para a URL"""
    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
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
    print("📱 QR Code para o site direto")
    print("=" * 40)
    
    # URL do site direto
    site_url = "https://github.com/deluccasgma/WdiasWebGis/blob/main/site_direto.html"
    
    print(f"🔗 Gerando QR Code para: {site_url}")
    if generate_qr_code(site_url, "site_direto_qr.png"):
        print("✅ QR Code salvo como: site_direto_qr.png")
    else:
        print("❌ Falha ao gerar QR Code")
    
    print("\n📱 Como usar:")
    print("1. Abra a câmera do seu celular")
    print("2. Aponte para o QR Code")
    print("3. Clique no link que aparecer")
    print("4. O site abrirá automaticamente!")

if __name__ == "__main__":
    main()