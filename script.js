// JavaScript para interatividade do site

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
    
    // Form submission
    const contactForm = document.querySelector('.contact-form form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Simular envio do formulário
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;
            
            submitBtn.textContent = 'Enviando...';
            submitBtn.disabled = true;
            
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
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observar elementos para animação
    const animatedElements = document.querySelectorAll('.about-card, .map-info, .contact-info');
    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
    
    // Verificar se o Streamlit está rodando
    function checkStreamlitStatus() {
        const iframe = document.querySelector('iframe[src*="localhost:8501"]');
        if (iframe) {
            iframe.onload = function() {
                console.log('Streamlit carregado com sucesso!');
            };
            
            iframe.onerror = function() {
                console.log('Streamlit não está rodando. Iniciando...');
                // Aqui você pode adicionar lógica para iniciar o Streamlit
            };
        }
    }
    
    // Verificar status do Streamlit após 2 segundos
    setTimeout(checkStreamlitStatus, 2000);
    
    // Adicionar loading state para o iframe
    const mapFrame = document.querySelector('.map-frame');
    if (mapFrame) {
        const loadingDiv = document.createElement('div');
        loadingDiv.innerHTML = `
            <div style="
                display: flex;
                justify-content: center;
                align-items: center;
                height: 600px;
                background: #f8f9fa;
                color: #1f4e79;
                font-size: 1.2rem;
            ">
                <div style="text-align: center;">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">🗺️</div>
                    <div>Carregando mapa...</div>
                    <div style="margin-top: 1rem; font-size: 0.9rem; opacity: 0.7;">
                        Se o mapa não carregar, verifique se o Streamlit está rodando
                    </div>
                </div>
            </div>
        `;
        
        const iframe = mapFrame.querySelector('iframe');
        if (iframe) {
            iframe.style.display = 'none';
            mapFrame.appendChild(loadingDiv);
            
            iframe.onload = function() {
                loadingDiv.remove();
                iframe.style.display = 'block';
            };
            
            iframe.onerror = function() {
                loadingDiv.innerHTML = `
                    <div style="
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 600px;
                        background: #f8f9fa;
                        color: #e74c3c;
                        font-size: 1.2rem;
                    ">
                        <div style="text-align: center;">
                            <div style="font-size: 3rem; margin-bottom: 1rem;">⚠️</div>
                            <div>Erro ao carregar o mapa</div>
                            <div style="margin-top: 1rem; font-size: 0.9rem; opacity: 0.7;">
                                Verifique se o Streamlit está rodando em localhost:8501
                            </div>
                            <button onclick="location.reload()" style="
                                margin-top: 1rem;
                                padding: 10px 20px;
                                background: #1f4e79;
                                color: white;
                                border: none;
                                border-radius: 5px;
                                cursor: pointer;
                            ">Tentar Novamente</button>
                        </div>
                    </div>
                `;
            };
        }
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
    
    // Adicionar contador de visitantes (simulado)
    let visitorCount = localStorage.getItem('visitorCount') || 0;
    visitorCount = parseInt(visitorCount) + 1;
    localStorage.setItem('visitorCount', visitorCount);
    
    // Mostrar contador no console (para desenvolvimento)
    console.log(`Visitante #${visitorCount} - Bem-vindo ao WebGIS!`);
    
    // Adicionar data atual no footer
    const footer = document.querySelector('.footer p');
    if (footer) {
        const currentYear = new Date().getFullYear();
        footer.innerHTML = `&copy; ${currentYear} WebGIS - Wdias Assessoria Rural. Todos os direitos reservados.`;
    }
});

// Função para iniciar o Streamlit (se necessário)
function startStreamlit() {
    console.log('Iniciando Streamlit...');
    // Aqui você pode adicionar lógica para iniciar o Streamlit via API
}

// Função para verificar se o Streamlit está rodando
function isStreamlitRunning() {
    return fetch('http://localhost:8501')
        .then(response => response.ok)
        .catch(() => false);
}

// Exportar funções para uso global
window.WebGIS = {
    startStreamlit,
    isStreamlitRunning
};