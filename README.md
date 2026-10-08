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

## Publicação (Cloudflare Workers com assets estáticos)
O site é publicado como um Worker chamado `cortexdev`, com `wrangler.jsonc` (`assets.directory` = `./`). Tudo na raiz é público, exceto o que está em `.assetsignore`. Toda pasta ou arquivo novo que não seja público deve entrar em `.assetsignore` no mesmo commit (`tests/test_repo_exposure.py` verifica isso).

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

## Cortex Financial Engine (motor de conferência, fatia mínima)
Estado: **em desenvolvimento, só local, só dados fictícios**. Não está publicado nem recebe arquivos de clientes.

| Item | Estado |
|---|---|
| Leitura de CSV e XLSX no formato brasileiro (vírgula decimal, ponto de milhar, R$) | Feito, com testes |
| Totais em `Decimal` e conciliação (divergência de R$ 600,00; consolidado R$ 149.025,00) | Feito, com testes |
| Exportação CSV com proteção contra injeção de fórmulas | Feito, com testes |
| Provedor de IA | Só simulado (`mock`); nenhuma chamada à API do Claude |
| PDF, API web, login, banco de dados, avaliação com conjunto de referência | Não iniciado |

Pastas: `engine/` (código), `fixtures/` (arquivos sintéticos), `tests/`, `scripts/`, `docs/`.
As fixtures foram reconstruídas a partir da página `/demo/` (a pasta `demo_dados` não estava no repositório).

### Rodar localmente (PowerShell)
```powershell
uv sync
uv run pytest -q
uv run python -m engine.cli demo
```
Não é preciso chave nem `.env`. Variáveis de limite estão em `.env.example` (padrões conservadores: gasto diário US$ 0, chave de bloqueio ligada).
