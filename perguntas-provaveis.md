# Perguntas prováveis e sugestões de resposta

Apresentação de Maggauer e Fina (2025), *Monte Carlo simulation-based economic risk assessment in energy communities*. Avaliação Financeira de Projetos, Prof. Cleiton Martins Duarte Silva, 11/11/2026.

## 1. Se o VPL médio é positivo nos quatro casos, por que se preocupar com risco?

Porque a média esconde a dispersão. No investimento direto no local 1, o VPL médio é de 20.800 €, mas em 32,4% dos cenários simulados o projeto dá prejuízo, e nos 10% piores a perda média é de 34.500 € (cVaR 90%). Para uma comunidade de habitação social, que não tem folga de caixa, uma chance em três de perder dinheiro pesa na decisão tanto quanto o retorno médio. É exatamente o ponto do artigo: o cálculo determinístico acerta o centro da distribuição, mas não mostra a cauda.

## 2. A conclusão de que a contratação é melhor é robusta?

Depende de uma premissa que o próprio artigo não consegue sustentar com dados: a margem de 5% do contratado. As autoras mostram que a contratação só continua menos arriscada com margem de até 5,3% no local 2 e de até 6,7% no local 1, pelo critério da probabilidade de prejuízo. A folga no local 2 é de 0,3 ponto percentual. Por isso a recomendação prática delas é negociar a margem, e não simplesmente escolher a contratação. Eu leria a conclusão como condicional: a contratação é melhor se a margem ficar baixa.

## 3. Por que usar distribuição uniforme para o WACC? Isso não infla o risco?

A uniforme foi usada porque a fonte (Coppitters et al., 2020) só dava uma faixa, de 4% a 8%, sem valor mais provável. O problema é que o WACC não é exatamente um risco do projeto: é a taxa que a comunidade escolhe para descontar o fluxo. Pela análise de sensibilidade do próprio artigo, essa faixa sozinha move o VPL do UC 1.1 em cerca de ±55 mil €, quase três vezes a média. Uma alternativa seria rodar o Monte Carlo separadamente para cada taxa (por exemplo, 4%, 6% e 8%) e mostrar o risco dentro de cada cenário, separando a incerteza sobre a taxa da incerteza operacional.

## 4. O que é cVaR e por que ele é melhor que o VaR?

O VaR a 90% é o valor que separa os 10% piores cenários; ele diz onde a cauda começa, mas não quão ruim ela é. O cVaR a 90% é a média desses 10% piores cenários, ou seja, quanto se perde em média quando as coisas dão errado. Além de informar o tamanho da perda, o cVaR tem uma propriedade teórica desejável: é uma medida de risco coerente (Artzner et al., 1999), o que o VaR não é. No artigo, o UC 1.2 tem VaR positivo (30.100 €), mas cVaR negativo (−22.800 €): olhando só o VaR, pareceria não haver perda na cauda.

## 5. O que os resultados dizem para o contexto brasileiro?

O método é diretamente transferível: geração compartilhada e autoconsumo remoto existem no Brasil desde a REN 482/2012 e a Lei 14.300/2022, e condomínios e cooperativas enfrentam a mesma escolha entre comprar a usina ou contratar uma empresa. Os números, não. Tarifas, irradiação, custo de capital e regras de compensação são muito diferentes, e no Brasil a volatilidade de tarifa e de taxa de juros é maior, o que tornaria o risco ainda mais relevante. A lição que transfere é a do método: não decidir o financiamento só pelo VPL médio.

## Se perguntarem algo mais técnico

- **Por que 100 mil rodadas?** As autoras dizem que o modelo é simples e o custo computacional é baixo. Não apresentam teste de convergência, mas com 100 mil sorteios o erro de Monte Carlo da média é pequeno (da ordem do desvio-padrão dividido por 316).
- **Os parâmetros são independentes?** Sim, por suposição. As autoras reconhecem a limitação e sugerem cópulas para trabalhos futuros.
- **Os "68%" do resumo estão certos?** A regra de que 68% dos resultados ficam a um desvio-padrão da média vale para a distribuição normal. Os histogramas do artigo são assimétricos e achatados, então o número é aproximado.
