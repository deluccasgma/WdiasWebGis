#!/usr/bin/env python3
"""
Servidor público para expor o site
"""
import http.server
import socketserver
import threading
import time
import requests
from urllib.parse import urlparse

class PublicHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Headers para permitir acesso externo
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def log_message(self, format, *args):
        # Log personalizado
        print(f"🌐 {self.address_string()} - {format % args}")

def get_public_ip():
    """Tenta obter o IP público"""
    try:
        response = requests.get('https://api.ipify.org', timeout=5)
        return response.text
    except:
        return "Não disponível"

def start_public_server(port=8080):
    """Inicia o servidor público"""
    with socketserver.TCPServer(("0.0.0.0", port), PublicHTTPRequestHandler) as httpd:
        print(f"🚀 Servidor público iniciado!")
        print(f"📱 URLs de acesso:")
        print(f"   🌐 Local: http://localhost:{port}")
        print(f"   📱 Rede local: http://172.30.0.2:{port}")
        print(f"   🌍 IP Público: http://{get_public_ip()}:{port}")
        print(f"⏹️  Pressione Ctrl+C para parar")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Servidor parado")

if __name__ == "__main__":
    start_public_server()