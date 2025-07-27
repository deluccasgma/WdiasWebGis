#!/usr/bin/env python3
"""
Servidor HTTP simples para o site de desenvolvimento
"""
import http.server
import socketserver
import os
import webbrowser
from urllib.parse import urlparse

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Adicionar headers CORS para permitir iframe
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def do_GET(self):
        # Roteamento personalizado
        if self.path == '/':
            self.path = '/index.html'
        elif self.path == '/mapa':
            self.path = '/index.html#mapa'
        elif self.path == '/sobre':
            self.path = '/index.html#sobre'
        elif self.path == '/contato':
            self.path = '/index.html#contato'
        
        return super().do_GET()

def start_server(port=8000):
    """Inicia o servidor HTTP"""
    with socketserver.TCPServer(("0.0.0.0", port), CustomHTTPRequestHandler) as httpd:
        print(f"🚀 Servidor iniciado na porta {port}")
        print(f"📱 Acesse: http://localhost:{port}")
        print(f"🌐 IP Local: http://172.30.0.2:{port}")
        print("⏹️  Pressione Ctrl+C para parar")
        
        try:
            # Abrir navegador automaticamente
            webbrowser.open(f'http://localhost:{port}')
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Servidor parado")

if __name__ == "__main__":
    start_server()