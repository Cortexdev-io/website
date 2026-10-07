# Demo: extratos em posição consolidada (dados fictícios)

Demonstração da Cortex Dev. Três extratos de corretoras fictícias, em formatos diferentes (CSV, planilha e e-mail), são lidos pelo Claude e convertidos em um formato único. O código confere os totais e consolida a posição.

**Todos os dados são fictícios.** Os tickers, as corretoras, os clientes e os preços são inventados. Não são cotações de mercado e não são recomendação de investimento.

## O que tem aqui

- `exemplos/01_corretora_alfa.csv`: extrato em CSV, com vírgula decimal e datas dd/mm/aaaa.
- `exemplos/02_beta_invest.xlsx`: planilha com cabeçalhos em inglês e datas ISO.
- `exemplos/03_gama_email.txt`: extrato em texto de e-mail. Um total declarado diverge da soma das posições, de propósito, para o código sinalizar.
- `prompt_extracao.txt`: o prompt enviado ao Claude para a leitura.
- `gabarito.json`: os valores esperados, para conferir o resultado. Não envie este arquivo ao Claude.

## Como a demo funciona

1. **Leitura (Claude):** o Claude recebe os três arquivos e devolve um JSON no formato único definido em `prompt_extracao.txt`.
2. **Conferência (código):** o código compara o total declarado com a soma das posições e refaz quantidade × preço médio de cada linha.
3. **Consolidação (código):** posição por ativo, por corretora e por setor fictício, com custo total.
4. **Resumo e perguntas (Claude):** o Claude recebe apenas os números já calculados e escreve o resumo. Ele não faz contas.

Valores esperados (para conferência):
- Custo total: R$ 149.025,00
- Divergência esperada: Gama Capital, R$ 600,00 (total declarado R$ 43.220,00; soma das posições R$ 42.620,00)

## Como executar

A leitura roda dentro do claude.ai, na página da demonstração. Não há servidor nem chave de API neste repositório.

1. Abra a página da demonstração no claude.ai.
2. Clique em **Usar os 3 arquivos de exemplo** e depois em **Ler com o Claude**.
3. Confira o resultado com os valores acima.
4. Exporte o snapshot em HTML, se quiser.

A leitura usa o limite de uso do Claude do seu plano.

## Sobre o resultado publicado

O snapshot publicado no site é um registro estático de uma execução real, com os mesmos dados fictícios. Ele não chama o Claude de novo. Se a demonstração for alterada, o snapshot precisa ser gerado novamente.

## Limitações

- A leitura é feita pelo Claude e pode errar. Por isso há conferência por código e campos de dúvida sinalizados.
- Não há integração com corretoras reais, nem armazenamento de dados.
- Não use dados reais de clientes com esta demonstração.

## Licença

Uso livre para leitura e estudo. Os arquivos de exemplo são fictícios e podem ser reutilizados sem restrição.
