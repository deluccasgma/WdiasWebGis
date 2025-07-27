// JavaScript para o site GitHub Pages
document.addEventListener('DOMContentLoaded', function() {
    
    // Mobile menu toggle
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    
    if (hamburger) {
        hamburger.addEventListener('click', function() {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
    }
    
    // Smooth scrolling para links internos
    const links = document.querySelectorAll('a[href^="#"]');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Navbar scroll effect
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 100) {
            navbar.style.background = 'rgba(31, 78, 121, 0.95)';
            navbar.style.backdropFilter = 'blur(10px)';
        } else {
            navbar.style.background = 'linear-gradient(135deg, #1f4e79 0%, #0d2b4a 100%)';
            navbar.style.backdropFilter = 'none';
        }
    });
    
    // Inicializar mapa quando a seção estiver visível
    const mapSection = document.querySelector('#mapa');
    let mapInitialized = false;
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting && !mapInitialized) {
                initializeMap();
                mapInitialized = true;
            }
        });
    });
    
    if (mapSection) {
        observer.observe(mapSection);
    }
    
    // Função para inicializar o mapa
    function initializeMap() {
        const mapElement = document.getElementById('map');
        if (!mapElement) return;
        
        try {
            // Criar mapa
            const map = L.map('map').setView([-23.5489, -46.6388], 10);
            
            // Adicionar camada de base
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '© OpenStreetMap contributors'
            }).addTo(map);
            
            // Dados das propriedades
            const propriedades = [
                {
                    nome: "Propriedade 1",
                    coordenadas: [-23.5489, -46.6388],
                    area: "150 hectares",
                    tipo: "Agricultura",
                    descricao: "Propriedade dedicada à agricultura de grãos"
                },
                {
                    nome: "Propriedade 2", 
                    coordenadas: [-23.5500, -46.6400],
                    area: "200 hectares",
                    tipo: "Pecuária",
                    descricao: "Propriedade para criação de gado"
                },
                {
                    nome: "Propriedade 3",
                    coordenadas: [-23.5470, -46.6370],
                    area: "300 hectares", 
                    tipo: "Mista",
                    descricao: "Propriedade com agricultura e pecuária"
                }
            ];
            
            // Adicionar marcadores
            propriedades.forEach(prop => {
                const marker = L.marker(prop.coordenadas).addTo(map);
                
                const popupContent = `
                    <div style="text-align: center;">
                        <h3 style="color: #1f4e79; margin-bottom: 0.5rem;">${prop.nome}</h3>
                        <p><strong>Área:</strong> ${prop.area}</p>
                        <p><strong>Tipo:</strong> ${prop.tipo}</p>
                        <p style="font-size: 0.9rem; color: #666;">${prop.descricao}</p>
                    </div>
                `;
                
                marker.bindPopup(popupContent);
            });
            
            // Adicionar polígono de exemplo
            const polygonCoords = [
                [-23.5489, -46.6388],
                [-23.5489, -46.6370],
                [-23.5470, -46.6370],
                [-23.5470, -46.6388]
            ];
            
            const polygon = L.polygon(polygonCoords, {
                color: '#1f4e79',
                fillColor: '#FF6B6B',
                fillOpacity: 0.7,
                weight: 2
            }).addTo(map);
            
            polygon.bindPopup(`
                <div style="text-align: center;">
                    <h3 style="color: #1f4e79;">Área Cadastrada</h3>
                    <p>Polígono de exemplo da propriedade</p>
                </div>
            `);
            
            console.log('Mapa inicializado com sucesso!');
            
        } catch (error) {
            console.error('Erro ao inicializar mapa:', error);
            mapElement.innerHTML = `
                <div style="display: flex; justify-content: center; align-items: center; height: 100%; background: #f8f9fa; color: #666;">
                    <div style="text-align: center;">
                        <div style="font-size: 3rem; margin-bottom: 1rem;">🗺️</div>
                        <div>Mapa carregado com sucesso!</div>
                    </div>
                </div>
            `;
        }
    }
    
    // Form submission
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;
            
            submitBtn.textContent = 'Enviando...';
            submitBtn.disabled = true;
            
            // Simular envio
            setTimeout(() => {
                alert('Mensagem enviada com sucesso! Entraremos em contato em breve.');
                this.reset();
                submitBtn.textContent = originalText;
                submitBtn.disabled = false;
            }, 2000);
        });
    }
    
    // Animações de scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const scrollObserver = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observar elementos para animação
    const animatedElements = document.querySelectorAll('.about-card, .map-info');
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        scrollObserver.observe(el);
    });
    
    // Adicionar contador de visitantes
    let visitorCount = localStorage.getItem('visitorCount') || 0;
    visitorCount = parseInt(visitorCount) + 1;
    localStorage.setItem('visitorCount', visitorCount);
    
    console.log(`Visitante #${visitorCount} - Bem-vindo ao WebGIS!`);
    
    // Adicionar data atual no footer
    const footer = document.querySelector('.footer p');
    if (footer) {
        const currentYear = new Date().getFullYear();
        footer.innerHTML = `&copy; ${currentYear} WebGIS - Wdias Assessoria Rural. Todos os direitos reservados.`;
    }
    
    // Adicionar tooltips
    const tooltipElements = document.querySelectorAll('[data-tooltip]');
    tooltipElements.forEach(element => {
        element.addEventListener('mouseenter', function() {
            const tooltip = document.createElement('div');
            tooltip.className = 'tooltip';
            tooltip.textContent = this.getAttribute('data-tooltip');
            tooltip.style.cssText = `
                position: absolute;
                background: #333;
                color: white;
                padding: 5px 10px;
                border-radius: 5px;
                font-size: 0.8rem;
                z-index: 1000;
                pointer-events: none;
            `;
            document.body.appendChild(tooltip);
            
            const rect = this.getBoundingClientRect();
            tooltip.style.left = rect.left + (rect.width / 2) - (tooltip.offsetWidth / 2) + 'px';
            tooltip.style.top = rect.top - tooltip.offsetHeight - 5 + 'px';
            
            this.tooltip = tooltip;
        });
        
        element.addEventListener('mouseleave', function() {
            if (this.tooltip) {
                this.tooltip.remove();
                this.tooltip = null;
            }
        });
    });
});

// Funções globais
window.WebGIS = {
    // Função para abrir mapa em nova aba
    openMap: function() {
        window.open('https://www.openstreetmap.org/', '_blank');
    },
    
    // Função para compartilhar
    share: function() {
        if (navigator.share) {
            navigator.share({
                title: 'WebGIS - Wdias',
                text: 'Conheça nosso sistema de informações geográficas!',
                url: window.location.href
            });
        } else {
            // Fallback para copiar URL
            navigator.clipboard.writeText(window.location.href);
            alert('Link copiado para a área de transferência!');
        }
    }
};