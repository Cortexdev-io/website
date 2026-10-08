# Cortex Dev: site

Site estático da Cortex Dev (cortexdev.io), em HTML, CSS e JavaScript puros. Não há build nem dependências.

## Estrutura
- `index.html`: home
- `demo/index.html`: página que explica a demonstração
- `demo/resultado/index.html`: registro estático da demonstração (dados fictícios)
- `privacidade/` e `termos/`: páginas legais
- `assets/`: CSS, JavaScript e imagens
- `config.js`: chaves da demonstração
- `_headers`, `robots.txt`, `sitemap.xml` e `404.html`

## Publicação (Cloudflare Pages)
1. Conecte este repositório ao Cloudflare Pages.
2. Comando de build: nenhum. Diretório de saída: a raiz do repositório.
3. Teste na URL `*.pages.dev` antes de ligar o domínio.

## config.js
- `demoPronta`: com `true`, a home mostra o selo "No ar" e o botão da demonstração; com `false`, mostra "Em desenvolvimento".
- `demoImagem`: com `true`, usa `assets/img/demo-hero.png`; com `false`, usa a tabela de exemplo em CSS.
- `urlDemo`: endereço da demonstração.

## Antes de publicar
- [ ] `demo/resultado/index.html` presente, com custo total de R$ 149.025,00 e divergência de R$ 600,00 na Gama.
- [ ] `assets/img/og-image.png` é um PNG de verdade.
- [ ] Todos os links do menu, do rodapé e do WhatsApp funcionam.
- [ ] Páginas legais revisadas por profissional jurídico.
- [ ] E-mail testado depois de qualquer mudança de DNS.

## Dados
Todos os dados da demonstração são fictícios. Nada aqui é recomendação de investimento.