<div align="center">

# 📚 ERP Biblioteca 🏢✨

**Sistema de Gestão Empresarial (ERP) moderno, completo e reativo para administração de acervos, empréstimos, estoque, clientes e circulação literária construído com Next.js 16, React 19 e Prisma.**

[![Versão](https://img.shields.io/badge/versão-1.0.0-3b82f6?style=for-the-badge&logo=nextdotjs&logoColor=white)](https://github.com/carlosguedes-dev/erp-biblioteca)
[![Licença](https://img.shields.io/badge/licença-MIT-00ff88?style=for-the-badge)](LICENSE)
[![Next.js](https://img.shields.io/badge/Next.js_16-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)](https://nextjs.org/)
[![React](https://img.shields.io/badge/React_19-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://react.dev/)
[![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_v4-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![Prisma ORM](https://img.shields.io/badge/Prisma_ORM-2D3748?style=for-the-badge&logo=prisma&logoColor=white)](https://www.prisma.io/)
[![Feito com Amor](https://img.shields.io/badge/Feito_com-MUITO_AMOR_❤️-ff0055?style=for-the-badge)](https://github.com/carlosguedes-dev)

🔗 **[Acessar o Repositório no GitHub](https://github.com/carlosguedes-dev/erp-biblioteca)**

---

<p align="center">
  <img src="https://images.unsplash.com/photo-1507842229356-51c6150fe957?q=80&w=1200&auto=format&fit=crop" alt="ERP Biblioteca Banner" width="80%" style="border-radius: 20px; box-shadow: 0 10px 30px rgba(59, 130, 246, 0.4);">
</p>

</div>

---

## 📖 Sobre o Projeto

O **ERP Biblioteca** é uma plataforma de gestão empresarial *Fullstack* de última geração desenvolvida para redefinir e modernizar o controle administrativo, logístico e financeiro de bibliotecas públicas, universitárias e centros literários privados. No cenário tradicional, o gerenciamento de acervos de livros, controle de devoluções, cadastro de leitores e monitoramento de circulação é realizado por sistemas corporativos arcaicos, lentos e com interfaces de usuário ultrapassadas que dificultam a produtividade da equipe e geram erros operacionais.

Para superar as limitações de softwares antigos, o **ERP Biblioteca** foi projetado com uma arquitetura *state-of-the-art* baseada no ecossistema do **Next.js 16 (App Router)** em conjunto com os recursos mais avançados do **React 19**, proporcionando uma experiência web incrivelmente rápida, dinâmica e fluida (*Single Page Application experience com Server Side Rendering*). Através de uma interface limpa, com suporte nativo à estética corporativa moderna e ao **Tailwind CSS v4**, o operador tem controle em tempo real de todo o fluxo operacional da instituição sem atrasos no carregamento de telas.

O sistema integra nativamente módulos fundamentais para o funcionamento de uma biblioteca moderna: controle minucioso e inventário de **Estoque e Acervo**, gestão e histórico completo de **Clientes e Leitores**, e um módulo dinâmico de **PDV (Ponto de Venda e Circulação)** planejado para registrar empréstimos, devoluções e consultas de disponibilidade em tempo recorde. A segurança e modelagem relacional dos dados são asseguradas pelo poder e confiabilidade do **Prisma ORM**, garantindo integridade referencial, consultas de alta performance e escalabilidade para acervos de qualquer dimensão.

---

## ✨ Principais Funcionalidades

- 📦 **Gestão Integrada de Acervo & Estoque**: Controle completo de livros, exemplares, autores, categorias e quantidade de inventário em tempo real com busca instantânea e filtros por estado de conservação.
- 👥 **Cadastro & CRM de Leitores**: Módulo dedicado à administração de clientes e usuários, histórico individual de empréstimos, pendências de devolução e consulta rápida por CPF ou código de matrícula.
- 🛒 **PDV Ágil (Ponto de Circulação & Empréstimos)**: Interface otimizada e pensada na produtividade do atendente no balcão, permitindo registrar saídas, empréstimos, renovações e devoluções de livros em pouquíssimos cliques.
- 📊 **Dashboard Corporativo & Métricas**: Tela inicial visual com indicadores centrais da biblioteca, alertando sobre volumes de circulação, livros mais requisitados e devoluções em atraso.
- ⚡ **Arquitetura Reativa com Next.js 16 & React 19**: Navegação instantânea e pré-carregamento inteligente de rotas através do moderno *App Router*, unindo o melhor da renderização no servidor (*SSR*) e interatividade no cliente.
- 🎨 **Interface Premium com Tailwind CSS v4**: Design system padronizado de alto nível corporativo com tipografia refinada, espaçamentos consistentes e ícones visuais limpos providos pela biblioteca **Lucide React**.
- 🔒 **Integração Robusta de Banco de Dados (Prisma ORM)**: Mapeamento objeto-relacional seguro com tipagem rigorosa de ponta a ponta através de TypeScript 5, prevenindo falhas em tempo de execução.

---

## 💻 Tecnologias Utilizadas

O **ERP Biblioteca** utiliza uma *stack* tecnológica poderosa e na vanguarda do desenvolvimento web moderno:

- **Next.js 16 (App Router)**: Framework Fullstack React de referência no mercado, oferecendo rotas otimizadas, Server Components e APIs internas altamente performáticas.
- **React 19**: Versão mais recente e avançada da principal biblioteca de interfaces do mundo, trazendo melhorias de performance e gerenciamento de estado assíncrono.
- **TypeScript 5**: Linguagem de tipagem estática que confere máxima segurança na comunicação entre os módulos de frontend, rotas de API e banco de dados.
- **Prisma ORM (v5)**: Mapeador objeto-relacional moderno que simplifica consultas complexas de banco de dados com autocompletar inteligente de esquemas no código.
- **Tailwind CSS v4**: Ferramenta de estilização utilitária de última geração para criação de layouts responsivos, elegantes e com tempo de carregamento otimizado.
- **Lucide React**: Biblioteca de ícones SVG modernos, consistentes e otimizados para aplicações de nível empresarial.
- **Axios**: Cliente HTTP baseado em *Promises* utilizado para requisições externas e comunicação de dados estruturados.

---

## 📁 Estrutura de Arquivos

```text
erp-biblioteca/
│
├── app/                   # Núcleo da aplicação em Next.js (App Router e API Routes)
│   ├── api/               # Endpoints RESTful internos para comunicação e lógica de negócios
│   ├── clientes/          # Módulo de cadastro, consulta e gerenciamento de clientes/leitores
│   ├── componentes/       # Componentes React reativos, modulares e reutilizáveis de interface
│   ├── estoque/           # Módulo de controle de livros, acervo, exemplares e inventário
│   ├── pdv/               # Ponto de Venda (PDV) e balcão para circulação e empréstimos
│   ├── layout.tsx         # Layout raiz corporativo com barra de navegação e menu lateral
│   └── page.tsx           # Dashboard principal com métricas, resumo e acesso rápido
├── prisma/                # Esquemas relacionais (schema.prisma), migrations e modelos do ORM
├── public/                # Ativos estáticos, favicon, ícones e recursos visuais
├── CONTRIBUTING.md        # Diretrizes e boas práticas para contribuições da comunidade
├── LICENSE                # Licença MIT de código aberto e software livre
├── package.json           # Manifesto do projeto, scripts executáveis e dependências
└── README.md              # Documentação oficial do sistema ERP (este arquivo)
```

---

## 🚀 Como Instalar e Executar o Projeto

Siga as etapas abaixo para configurar, compilar e executar o servidor de desenvolvimento do **ERP Biblioteca** em sua máquina local.

### 1. Pré-requisitos do Sistema
Certifique-se de ter instalado em seu computador:
- [Node.js](https://nodejs.org/) (Versão 20 ou superior recomendada)
- [NPM](https://www.npmjs.com/), [Yarn](https://yarnpkg.com/) ou [PNPM](https://pnpm.io/)
- Servidor de Banco de Dados compatível com Prisma (PostgreSQL, MySQL, SQLite ou SQL Server)

### 2. Instalação de Dependências
Clone o repositório em sua máquina e instale os pacotes necessários:

```bash
git clone https://github.com/carlosguedes-dev/erp-biblioteca.git
cd erp-biblioteca
npm install
```

### 3. Configuração de Variáveis de Ambiente
Crie ou edite o arquivo `.env` na raiz do projeto e configure a variável de conexão com seu banco de dados de desenvolvimento:

```env
DATABASE_URL="postgresql://usuario:senha@localhost:5432/erp_biblioteca?schema=public"
# Ou, se estiver utilizando SQLite para teste local rápido:
# DATABASE_URL="file:./dev.db"
```

### 4. Geração do Cliente ORM & Sincronização
Gere os tipos do cliente Prisma com base no seu esquema e sincronize as tabelas com o banco de dados:

```bash
npx prisma generate
npx prisma db push
# (Opcional) Para preencher o banco com dados iniciais de teste caso possua um seed configurado:
# npx prisma db seed
```

### 5. Iniciar o Servidor de Desenvolvimento
Execute o comando de inicialização local:

```bash
npm run dev
```

Acesse **[http://localhost:3000](http://localhost:3000)** no seu navegador para explorar e interagir com o sistema ERP em funcionamento!

---

## 🤝 Como Contribuir

O **ERP Biblioteca** é um projeto open-source que busca democratizar o acesso a ferramentas de gestão educacional e literária de alto padrão! Seja para adicionar relatórios financeiros, implementar integrações com leitor de código de barras para o PDV ou aprimorar a acessibilidade das telas, toda ajuda é super bem-vinda.

Consulte o arquivo [CONTRIBUTING.md](CONTRIBUTING.md) para saber mais sobre como configurar o ambiente de desenvolvimento, criar *branches* de funcionalidades e submeter o seu *Pull Request*.

---

## 📄 Licença

Este software é disponibilizado sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes sobre os termos de uso, cópia e distribuição livre.

---

<div align="center">
  <p>Feito com todo o carinho e dedicação por <b>Carlos Guedes</b> ❤️</p>
  <p><b>Transformando código em excelência e inovação! ✨</b></p>
</div>
