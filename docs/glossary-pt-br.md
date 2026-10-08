# Glossário pt-BR

Termos usados no produto, na documentação e nas mensagens da API.

| Termo | Significado neste produto | Observação |
|---|---|---|
| Posição | Quantidade de um ativo mantida em uma conta, em uma data de referência. | No mercado também pode significar exposição líquida; aqui é só o que consta no extrato. |
| Custódia | Guarda dos ativos por uma instituição em nome do investidor. | Não é o mesmo que a corretora que executa ordens. |
| Custo de aquisição | Valor pago pelo ativo (quantidade × preço médio). | É o valor das linhas dos extratos da demonstração. Não é valor de mercado. |
| Valor de mercado | Quantidade × cotação em uma data. | Não é calculado nesta fatia. Nunca se soma com custo de aquisição. |
| Quantidade | Número de unidades do ativo; pode ser fracionária. | |
| Preço médio | Custo de aquisição dividido pela quantidade. | Pode vir arredondado no extrato; a conferência tolera R$ 0,01. |
| Ativo | Instrumento identificado por ticker (e, quando houver, ISIN). | O ticker sozinho pode ser ambíguo. |
| Conta | Conta de um cliente em uma instituição. | Nos dados fictícios, "Cliente Demo 001". |
| Data de referência | Data a que os valores do extrato se referem. | Dois extratos da mesma conta e data não se somam. |
| Divergência | Diferença entre dois valores que deveriam coincidir, calculada por código. | Ex.: total declarado R$ 43.220,00 contra soma R$ 42.620,00 (R$ 600,00). |
| Conciliação | Comparação dos extratos entre si e com os totais declarados, gerando exceções. | Exceção não resolvida fica visível; o dado de origem não é alterado. |
| Corretora | Instituição que intermedeia a compra e venda de ativos. | |
| Custodiante | Instituição que guarda os ativos. | Pode ser a mesma corretora ou outra. |