<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Moussa Sow - Étudiant en Systèmes d'Information & Développeur FullStack">
    <title>Moussa Sow | Portfolio</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="{{ asset('css/style.css') }}">
</head>
<body>
    <!-- Navigation -->
    <nav class="nav">
        <div class="nav-container">
            <a href="#" class="nav-logo">MS</a>
            <div class="nav-links">
                <a href="#about">À propos</a>
                <a href="#skills">Compétences</a>
                <a href="#projects">Projets</a>
                <a href="#certifications">Certifications</a>
                <a href="#contact">Contact</a>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero">
        <div class="hero-container">
            <p class="hero-badge animate">Développeur FullStack</p>
            <h1 class="hero-title animate animate-delay-1">Moussa Sow</h1>
            <p class="hero-slogan animate animate-delay-2">Learning Earning Returning</p>
            <p class="hero-subtitle animate animate-delay-3">
                Étudiant en Systèmes d'Information, passionné par le développement web et la modélisation orientée objet.
            </p>
            <div class="hero-cta animate animate-delay-4">
                <a href="#projects" class="btn btn-primary">
                    <i class="fas fa-code"></i>
                    Découvrir mes projets
                </a>
                <a href="#contact" class="btn btn-secondary">
                    <i class="fas fa-envelope"></i>
                    Me contacter
                </a>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="section">
        <div class="container">
            <div class="about-grid">
                <div class="about-image">
                    <img src="{{ asset('photoPro.jpg') }}" alt="Moussa Sow">
                </div>
                <div class="about-content">
                    <h3>Développeur FullStack & Administrateur Systèmes</h3>
                    <p>
                        Étudiant en fin de cycle de Licence 3 en Développement et Administration d'Applications (Systèmes d'Information), avec une solide expérience en développement fullstack, administration des systèmes et recherche appliquée.
                    </p>
                    <p>
                        Candidat à un Master aux États-Unis, avec un fort intérêt pour les systèmes d'information et les technologies orientées données. Capacité démontrée à concevoir des applications évolutives et gérer des infrastructures informatiques.
                    </p>
                    <div class="stats">
                        <div class="stat">
                            <div class="stat-number">7+</div>
                            <div class="stat-label">Projets réalisés</div>
                        </div>
                        <div class="stat">
                            <div class="stat-number">4</div>
                            <div class="stat-label">Certifications</div>
                        </div>
                        <div class="stat">
                            <div class="stat-number">3+</div>
                            <div class="stat-label">Années d'expérience</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Skills Section -->
    <section id="skills" class="section section-dark">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">Compétences</h2>
                <p class="section-subtitle">Une expertise pluridisciplinaire dans le développement et l'administration système</p>
            </div>
            <div class="skills-grid">
                <div class="skill-card">
                    <div class="skill-header">
                        <div class="skill-icon"><i class="fas fa-code"></i></div>
                        <h4 class="skill-title">Programmation & Web</h4>
                    </div>
                    <div class="skill-tags">
                        <span class="skill-tag">JavaScript</span>
                        <span class="skill-tag">PHP</span>
                        <span class="skill-tag">TypeScript</span>
                        <span class="skill-tag">React</span>
                        <span class="skill-tag">Laravel</span>
                        <span class="skill-tag">HTML/CSS</span>
                    </div>
                </div>
                <div class="skill-card">
                    <div class="skill-header">
                        <div class="skill-icon"><i class="fas fa-database"></i></div>
                        <h4 class="skill-title">Bases de données</h4>
                    </div>
                    <div class="skill-tags">
                        <span class="skill-tag">MySQL</span>
                        <span class="skill-tag">PostgreSQL</span>
                        <span class="skill-tag">SQL</span>
                    </div>
                </div>
                <div class="skill-card">
                    <div class="skill-header">
                        <div class="skill-icon"><i class="fas fa-server"></i></div>
                        <h4 class="skill-title">Systèmes & Réseaux</h4>
                    </div>
                    <div class="skill-tags">
                        <span class="skill-tag">Windows Server</span>
                        <span class="skill-tag">Active Directory</span>
                        <span class="skill-tag">PowerShell</span>
                        <span class="skill-tag">DNS/DHCP</span>
                    </div>
                </div>
                <div class="skill-card">
                    <div class="skill-header">
                        <div class="skill-icon"><i class="fas fa-pencil-ruler"></i></div>
                        <h4 class="skill-title">Design & Data</h4>
                    </div>
                    <div class="skill-tags">
                        <span class="skill-tag">UX/UI</span>
                        <span class="skill-tag">UML</span>
                        <span class="skill-tag">Visualisation</span>
                        <span class="skill-tag">Modélisation</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="section">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">Projets</h2>
                <p class="section-subtitle">Des réalisations concrètes qui démontrent mon expertise</p>
            </div>
            <div class="projects-grid">
                <div class="project-card">
                    <div class="project-meta">
                        <span class="project-date">Mai 2024 - Fév 2025</span>
                    </div>
                    <div class="project-tech">
                        <span>HTML/CSS</span>
                        <span>JavaScript</span>
                        <span>SQL</span>
                    </div>
                    <h3 class="project-title">ReachData</h3>
                    <p class="project-desc">Plateforme de collecte et visualisation de données scientifiques avec interfaces interactives.</p>
                    <a href="#" class="project-link"><i class="fab fa-github"></i> Code source</a>
                </div>
                <div class="project-card">
                    <div class="project-meta">
                        <span class="project-date">Janv 2025 - Fév 2025</span>
                    </div>
                    <div class="project-tech">
                        <span>PHP</span>
                        <span>MySQL</span>
                    </div>
                    <h3 class="project-title">StockPlus</h3>
                    <p class="project-desc">Système de gestion des stocks, ventes et commandes avec tableaux de bord décisionnels.</p>
                    <a href="#" class="project-link"><i class="fab fa-github"></i> Code source</a>
                </div>
                <div class="project-card">
                    <div class="project-meta">
                        <span class="project-date">Oct - Déc 2024</span>
                    </div>
                    <div class="project-tech">
                        <span>HTML5</span>
                        <span>Bootstrap</span>
                    </div>
                    <h3 class="project-title">Gestion Stocks</h3>
                    <p class="project-desc">Application web de suivi des stocks et ventes avec interfaces claires.</p>
                    <a href="#" class="project-link"><i class="fab fa-github"></i> Code source</a>
                </div>
                <div class="project-card">
                    <div class="project-meta">
                        <span class="project-date">Nov 2024 - Juin 2025</span>
                    </div>
                    <div class="project-tech">
                        <span>POO</span>
                        <span>NetLogo</span>
                    </div>
                    <h3 class="project-title">CIRAD</h3>
                    <p class="project-desc">Modélisation orientée objet des feux de brousse et parefeu en contexte silvopastoral.</p>
                    <a href="#" class="project-link"><i class="fas fa-flask"></i> Recherche</a>
                </div>
                <div class="project-card">
                    <div class="project-meta">
                        <span class="project-date">Mai - Juin 2025</span>
                    </div>
                    <div class="project-tech">
                        <span>Windows Server</span>
                        <span>PowerShell</span>
                    </div>
                    <h3 class="project-title">Infrastructure</h3>
                    <p class="project-desc">Conception d'infrastructure réseau complète avec Active Directory, DNS, DHCP.</p>
                    <a href="#" class="project-link"><i class="fas fa-server"></i> Documentation</a>
                </div>
                <div class="project-card">
                    <div class="project-meta">
                        <span class="project-date">Août 2025</span>
                    </div>
                    <div class="project-tech">
                        <span>React</span>
                        <span>TypeScript</span>
                    </div>
                    <h3 class="project-title">Gestion Financière</h3>
                    <p class="project-desc">Plateforme financière avec prévisions, alertes intelligentes et tableaux de bord.</p>
                    <a href="#" class="project-link"><i class="fab fa-github"></i> Code source</a>
                </div>
                <div class="project-card">
                    <div class="project-meta">
                        <span class="project-date">Mai - Juillet 2025</span>
                    </div>
                    <div class="project-tech">
                        <span>PostgreSQL</span>
                        <span>UX Design</span>
                    </div>
                    <h3 class="project-title">Ferlo Impact Hub</h3>
                    <p class="project-desc">Vitrine web officielle avec portail de présentation et suivi des initiatives.</p>
                    <a href="#" class="project-link"><i class="fas fa-external-link-alt"></i> Voir le site</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Certifications Section -->
    <section id="certifications" class="section section-dark">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">Certifications</h2>
                <p class="section-subtitle">Des qualifications reconnues internationalement</p>
            </div>
            <div class="certs-grid">
                <div class="cert-card">
                    <div class="cert-icon"><i class="fas fa-brain"></i></div>
                    <div class="cert-info">
                        <h4>Fondamentaux de l'IA</h4>
                        <p>Cambridge International Qualifications</p>
                        <span class="cert-year">Septembre 2025</span>
                    </div>
                </div>
                <div class="cert-card">
                    <div class="cert-icon"><i class="fas fa-bullhorn"></i></div>
                    <div class="cert-info">
                        <h4>Marketing Digital</h4>
                        <p>Cambridge International Qualifications</p>
                        <span class="cert-year">Septembre 2025</span>
                    </div>
                </div>
                <div class="cert-card">
                    <div class="cert-icon"><i class="fas fa-project-diagram"></i></div>
                    <div class="cert-info">
                        <h4>MODEV 2</h4>
                        <p>Agence Française de Développement</p>
                        <span class="cert-year">Septembre 2025</span>
                    </div>
                </div>
                <div class="cert-card">
                    <div class="cert-icon"><i class="fas fa-heartbeat"></i></div>
                    <div class="cert-info">
                        <h4>IA au service de la santé</h4>
                        <p>Certification de préincubation</p>
                        <span class="cert-year">Septembre 2025</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">Contact</h2>
                <p class="section-subtitle">Une opportunité de collaboration ? N'hésitez pas à me contacter.</p>
            </div>
            <div class="contact-grid">
                <div class="contact-info">
                    <div class="contact-item">
                        <div class="contact-icon"><i class="fas fa-envelope"></i></div>
                        <div>
                            <h4>Email</h4>
                            <p>moussa3.sow@uadb.edu.sn</p>
                        </div>
                    </div>
                    <div class="contact-item">
                        <div class="contact-icon"><i class="fas fa-phone"></i></div>
                        <div>
                            <h4>Téléphone</h4>
                            <p>+221 78 162 08 88</p>
                        </div>
                    </div>
                    <div class="contact-item">
                        <div class="contact-icon"><i class="fas fa-map-marker-alt"></i></div>
                        <div>
                            <h4>Localisation</h4>
                            <p>Dakar, Sénégal</p>
                        </div>
                    </div>
                    <div class="social">
                        <a href="https://linkedin.com/in/ms-officiel" class="social-link" target="_blank">
                            <i class="fab fa-linkedin-in"></i>
                        </a>
                        <a href="#" class="social-link" target="_blank">
                            <i class="fab fa-github"></i>
                        </a>
                    </div>
                </div>
                <div class="contact-message">
                    <h4>Envie de collaborer ?</h4>
                    <p>Je suis toujours ouvert aux nouvelles opportunités et aux projets intéressants.</p>
                    <p style="margin-top: var(--space-3);"><strong>Langues :</strong> Français (courant), Anglais (intermédiaire)</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-logo">MS</div>
            <p>&copy; 2025 Moussa Sow. Tous droits réservés.</p>
            <p class="footer-slogan">Learning Earning Returning</p>
        </div>
    </footer>

    <script src="{{ asset('js/main.js') }}"></script>
</body>
</html>

