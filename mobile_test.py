#!/usr/bin/env python3
"""
Teste de conectividade mobile
"""
import requests
import socket
import subprocess
import time

def test_local_connectivity():
    """Testa conectividade local"""
    print("🔍 Testando conectividade local...")
    
    # Testar localhost
    try:
        response = requests.get('http://localhost:8000', timeout=5)
        print(f"✅ Localhost:8000 - Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Localhost:8000 - Erro: {e}")
    
    # Testar IP local
    try:
        response = requests.get('http://172.30.0.2:8000', timeout=5)
        print(f"✅ IP Local:172.30.0.2:8000 - Status: {response.status_code}")
    except Exception as e:
        print(f"❌ IP Local:172.30.0.2:8000 - Erro: {e}")

def get_network_info():
    """Obtém informações da rede"""
    print("\n🌐 Informações da rede:")
    
    # IPs locais
    try:
        result = subprocess.run(['hostname', '-I'], capture_output=True, text=True)
        ips = result.stdout.strip().split()
        print(f"📱 IPs locais: {', '.join(ips)}")
    except Exception as e:
        print(f"❌ Erro ao obter IPs: {e}")
    
    # IP público
    try:
        response = requests.get('https://api.ipify.org', timeout=5)
        print(f"🌍 IP público: {response.text}")
    except Exception as e:
        print(f"❌ Erro ao obter IP público: {e}")

def test_ports():
    """Testa portas abertas"""
    print("\n🔌 Testando portas:")
    
    ports = [8000, 8501, 8080]
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex(('localhost', port))
            sock.close()
            
            if result == 0:
                print(f"✅ Porta {port}: Aberta")
            else:
                print(f"❌ Porta {port}: Fechada")
        except Exception as e:
            print(f"❌ Porta {port}: Erro - {e}")

def generate_mobile_urls():
    """Gera URLs para acesso mobile"""
    print("\n📱 URLs para acesso mobile:")
    
    try:
        response = requests.get('https://api.ipify.org', timeout=5)
        public_ip = response.text
    except:
        public_ip = "N/A"
    
    urls = [
        ("Local", "http://localhost:8000"),
        ("Rede Local", "http://172.30.0.2:8000"),
        ("IP Público", f"http://{public_ip}:8000"),
        ("WebGIS Direto", "http://localhost:8501"),
        ("WebGIS Rede", "http://172.30.0.2:8501")
    ]
    
    for name, url in urls:
        print(f"   {name}: {url}")

def main():
    """Função principal"""
    print("📱 Diagnóstico de Conectividade Mobile")
    print("=" * 50)
    
    test_local_connectivity()
    get_network_info()
    test_ports()
    generate_mobile_urls()
    
    print("\n💡 Dicas para acesso mobile:")
    print("1. Certifique-se de estar na mesma rede WiFi")
    print("2. Tente usar o IP da rede local")
    print("3. Se não funcionar, use o Streamlit Cloud")
    print("4. Ou use um túnel como ngrok/cloudflared")

if __name__ == "__main__":
    main()