# Site da Cortex Dev (cortexdev.io)

Site estático em HTML, CSS e JavaScript puros. Sem build, sem framework. Usa apenas Google Fonts.

## Publicar no Cloudflare Pages

1. Conecte este repositório ao Cloudflare Pages.
2. Comando de build: vazio.
3. Diretório de saída: a raiz do repositório (`/`).

## Demo

Tudo é controlado por `config.js`:

- `demoPronta`: `true` quando `demo/resultado/index.html` estiver no repositório. Com `true`: selo "No ar", botões "Abrir a demo" e "Ver a demo". Com `false`: "Em desenvolvimento" e "Conceito de interface".
- `demoImagem`: `true` quando `assets/img/demo-hero.png` (captura da demo) estiver no repositório. Com `true`, a seção Demo da home mostra a captura. Com `false`, mostra a tabela antes/depois em CSS.
- `urlDemo`: endereço da demo (padrão `/demo/resultado/`).

## Vídeo e links opcionais

O player de vídeo não existe hoje (URL vazia). Para exibir, adicione um `<iframe>` na seção Demo de `index.html` e em `demo/index.html`. Links de LinkedIn, GitHub e código do site só existem se houver URL.

## Checklist antes de publicar

- [ ] Variáveis vazias revisadas (vídeo, repositório da demo)
- [ ] Afirmações do site confirmadas (prazo, preços, segurança, FAQ)
- [ ] Páginas legais revisadas por profissional jurídico
- [ ] Snapshot em `demo/resultado/index.html`
- [ ] `sitemap.xml` conferido
- [ ] E-mail testado depois de qualquer mudança de DNS
