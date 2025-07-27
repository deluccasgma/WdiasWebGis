#!/usr/bin/env python3
"""
Túnel HTTP simples para expor o WebGIS
"""
import socket
import threading
import http.server
import socketserver
import requests
from urllib.parse import urlparse

class TunnelHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            # Redirecionar para o Streamlit
            response = requests.get(f"http://localhost:8501{self.path}", timeout=10)
            self.send_response(response.status_code)
            
            # Copiar headers
            for header, value in response.headers.items():
                if header.lower() not in ['transfer-encoding', 'connection']:
                    self.send_header(header, value)
            
            self.end_headers()
            self.wfile.write(response.content)
            
        except Exception as e:
            self.send_error(500, f"Erro no túnel: {str(e)}")
    
    def do_POST(self):
        try:
            # Ler dados do POST
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            
            # Redirecionar para o Streamlit
            response = requests.post(
                f"http://localhost:8501{self.path}",
                data=post_data,
                headers=dict(self.headers),
                timeout=10
            )
            
            self.send_response(response.status_code)
            for header, value in response.headers.items():
                if header.lower() not in ['transfer-encoding', 'connection']:
                    self.send_header(header, value)
            
            self.end_headers()
            self.wfile.write(response.content)
            
        except Exception as e:
            self.send_error(500, f"Erro no túnel: {str(e)}")

def start_tunnel(port=8080):
    """Inicia o túnel na porta especificada"""
    with socketserver.TCPServer(("0.0.0.0", port), TunnelHandler) as httpd:
        print(f"🚀 Túnel iniciado na porta {port}")
        print(f"📱 Acesse: http://54.188.159.183:{port}")
        print(f"🌐 Ou use: http://localhost:{port}")
        print("⏹️  Pressione Ctrl+C para parar")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Túnel parado")

if __name__ == "__main__":
    start_tunnel()