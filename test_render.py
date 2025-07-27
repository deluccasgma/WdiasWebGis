#!/usr/bin/env python3
"""
Script de teste para Render
"""
import sys
import os

def test_imports():
    """Testa se as dependências estão funcionando"""
    print("🔍 Testando imports...")
    
    try:
        import streamlit
        print(f"✅ Streamlit: {streamlit.__version__}")
    except Exception as e:
        print(f"❌ Streamlit: {e}")
        return False
    
    try:
        import folium
        print(f"✅ Folium: {folium.__version__}")
    except Exception as e:
        print(f"❌ Folium: {e}")
        return False
    
    try:
        import streamlit_folium
        print("✅ Streamlit-folium: OK")
    except Exception as e:
        print(f"❌ Streamlit-folium: {e}")
        return False
    
    return True

def test_app():
    """Testa se o app pode ser importado"""
    print("\n🔍 Testando app...")
    
    try:
        import app_minimal
        print("✅ App pode ser importado")
        return True
    except Exception as e:
        print(f"❌ Erro ao importar app: {e}")
        return False

def main():
    """Função principal"""
    print("🚀 Teste de compatibilidade para Render")
    print("=" * 40)
    
    # Testar imports
    if not test_imports():
        print("\n❌ Falha nos imports")
        sys.exit(1)
    
    # Testar app
    if not test_app():
        print("\n❌ Falha no app")
        sys.exit(1)
    
    print("\n✅ Todos os testes passaram!")
    print("🎉 App pronto para deploy no Render")

if __name__ == "__main__":
    main()