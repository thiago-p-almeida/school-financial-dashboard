# Business Requirements Document v1.1

## Parte 1 — Change Summary

### O que mudou

Esta atualização do **BRD v1.0** para **v1.1** preserva o núcleo já consolidado — controle financeiro mensal, estrutura de custos com destaque para aluguel/folha, sustentabilidade da mensalidade, rematrícula/retenção/evasão, impacto de descontos e baixa maturidade digital — e incorpora um incremento analítico e gerencial para permitir enxergar **onde** estão os principais problemas e oportunidades dentro da escola.

O incremento principal é a inclusão explícita de **segmentação** e de dimensões de gestão que afetam diretamente o resultado financeiro e a retenção:

- **Segmentação acadêmica**: segmento (Educação Infantil / Fundamental I / Fundamental II), série/ano (Maternal, Jardim I/II, 1º–9º) e turma.
- **Dimensões gerenciais**: status do aluno, status de rematrícula, faixa de desconto, situação financeira, motivo de saída e ocupação por turma.
- **Bolsistas**: acompanhamento de contagem, percentual e valor concedido, com distinção explícita entre **bolsa** e **desconto comercial**.

### Por que mudou

O **BRD v1.0** já aponta que a escola opera em um mercado sensível a preço, com pressão por descontos, risco de evasão e custo de aluguel como despesa crítica. Nesse contexto, a leitura apenas **consolidada** — por exemplo, “total de alunos” e “receita total” — é útil para visão executiva, mas pode **ocultar concentrações** relevantes, como:

- evasão concentrada em certas séries/turmas (transições de ciclo);
- descontos/bolsas concentrados em determinados grupos (compressão de receita líquida);
- turmas com baixa ocupação (ineficiência estrutural e aumento do custo por aluno).

A literatura de gestão educacional e financeira reforça a importância de monitorar:

1. a relação entre desconto e a **receita líquida de mensalidades**;  
2. capacidade/ocupação para decisões de planejamento e eficiência.

### Seções impactadas

Atualizações cirúrgicas foram aplicadas nas seções:

- **Executive Summary**  
  Incluiu o racional da visão segmentada e o escopo de dimensões gerenciais.

- **Business Context**  
  Estruturou a leitura por segmento/série/turma e registrou necessidade de visibilidade comparativa.

- **Known Business Challenges**  
  Incluiu lacuna de visibilidade por recorte, bolsas e ocupação por turma.

- **Derived Challenges and Secondary Risks**  
  Incluiu riscos de concentração de concessões, baixa ocupação e perdas em transições.

- **Business Strengths and Opportunities**  
  Incluiu oportunidades de gestão por recorte e eficiência de capacidade.

- **Strategic Business Objectives**  
  Incluiu objetivo explícito de visibilidade segmentada.

- **Key Business Questions**  
  Incluiu perguntas por segmento/série/turma e impacto de bolsas/ocupação.

- **Initial Business Requirements**  
  Incluiu requisitos de dados e leitura segmentada, mantendo simplicidade.

- **Critical Validation Gaps**  
  Incluiu lacunas para viabilizar segmentação, bolsas e ocupação.

- **Recommended Next Steps**  
  Incluiu recomendações práticas e notas que impactam SRS/SDD: local-first, cloud-ready e modelo de dados com segmentação.

---

## Parte 2 — BRD v1.1 completo

### Metadados

- **Documento:** Business Requirements Document (BRD)
- **Produto:** @CESOL School Financial and Administrative Dashboard
- **Versão:** v1.1
- **Data:** 12/03/2026 (America/Belém)
- **Natureza da revisão:** incremental (cirúrgica), preservando o núcleo do BRD v1.0 e adicionando segmentação e dimensões gerenciais.

### Legenda de rastreabilidade de fonte

- **Directly stated in BRD v1.0**: informação explicitamente presente no BRD original.
- **Derived from BRD v1.0**: inferência plausível a partir do BRD original, sem introduzir fatos novos.
- **Open question / Needs validation**: item necessário, mas que requer confirmação com a liderança (dados, definições, políticas e disponibilidade).

---

## Executive Summary

A @CESOL opera com uma estrutura escolar enxuta e funcional, mas enfrenta limitações importantes de gestão por ausência de controle financeiro consolidado, baixa digitalização e dificuldade de transformar dados operacionais em decisões estratégicas. O cenário combina pressão competitiva por preço, custo fixo relevante com aluguel, risco de evasão e fragilidade na leitura da saúde financeira.  
**[Directly stated in BRD v1.0]**

O problema central não parece ser apenas a falta de um dashboard, mas a ausência de uma base mínima de gestão orientada por dados, o que limita a capacidade da direção de responder com segurança a perguntas críticas sobre rentabilidade, retenção, impacto de descontos, sustentabilidade da mensalidade e equilíbrio da operação.  
**[Directly stated in BRD v1.0]**

### Incremento v1.1 — visão segmentada e gerencial

Além da visão consolidada (mês a mês), a gestão precisa enxergar **onde** estão receita, risco e pressão: por **segmento**, **série/ano** e **turma**, com leitura conjunta de **desconto, bolsa, ocupação e motivos de saída**. Esse tipo de análise facilita decisões coerentes com o objetivo do BRD: tornar a gestão mais objetiva sem tornar a solução complexa.  
**[Derived from BRD v1.0 + incremento solicitado]**

A distinção entre **desconto** e **bolsa** passa a ser explicitamente necessária no contexto do negócio, pois ambas reduzem o valor efetivamente arrecadado por aluno e podem influenciar a sustentabilidade financeira. Em instituições educacionais, monitorar a relação entre concessões (auxílios/bolsas/descontos) e receita efetiva é prática recomendada para evitar erosão de receita líquida.  
**[Derived from BRD v1.0 + incremento solicitado]**

---

## Business Context

A @CESOL é uma escola privada de pequeno/médio porte com 4 sócios, 1 secretária, 10 professores e pouco mais de 100 alunos. Atua na educação infantil e no ensino fundamental, com operação concentrada no turno da manhã.  
**[Directly stated in BRD v1.0]**

A escola está inserida em um mercado sensível a preço, com concorrentes que praticam mensalidades menores e possuem vantagem estrutural por não carregarem custo de aluguel. Isso pressiona a @CESOL em margem financeira e retenção de alunos.  
**[Directly stated in BRD v1.0]**

### Estrutura analítica recomendada (v1.1)

Para decisões mais precisas, o contexto passa a ser analisado sob a hierarquia:

- **Segmento (mínimo analítico)**: Educação Infantil, Ensino Fundamental I, Ensino Fundamental II.  
  **[Open question / Needs validation: confirmar quais séries existem hoje e se Fundamental II está completo]**

- **Série/Ano (granularidade)**: Maternal, Jardim I, Jardim II, 1º ao 9º ano.  
  **[Open question / Needs validation: confirmar abrangência real]**

- **Turma (operacional)**: ex.: “Jardim II A”, “1º Ano A”, “1º Ano B”.  
  **[Derived from BRD v1.0 + incremento solicitado]**

A demanda central permanece sendo de clareza gerencial: entender melhor a operação, ganhar visibilidade sobre custos e receitas, monitorar retenção e apoiar decisões com mais segurança.  
**[Directly stated in BRD v1.0]**

---

## Known Business Challenges

1. Controle financeiro majoritariamente manual, baseado em papel.  
   **[Directly stated in BRD v1.0]**

2. Baixa digitalização dos processos administrativos e financeiros.  
   **[Directly stated in BRD v1.0]**

3. Quase inexistência de planilhas estruturadas.  
   **[Directly stated in BRD v1.0]**

4. Perda de dados e lentidão para checagem de informações.  
   **[Directly stated in BRD v1.0]**

5. Quase zero controle financeiro consolidado.  
   **[Directly stated in BRD v1.0]**

6. Forte pressão competitiva por concorrentes com mensalidades mais baixas.  
   **[Directly stated in BRD v1.0]**

7. Pressão frequente por descontos por parte das famílias.  
   **[Directly stated in BRD v1.0]**

8. Risco ou ocorrência de evasão para concorrentes.  
   **[Directly stated in BRD v1.0]**

9. Custo de aluguel como despesa crítica e desvantagem competitiva.  
   **[Directly stated in BRD v1.0]**

10. Baixa maturidade digital de parte da gestão.  
    **[Directly stated in BRD v1.0]**

### Desafios adicionados pela necessidade de gestão segmentada (v1.1)

11. Baixa visibilidade de indicadores por **segmento / série / turma** (dificuldade de localizar onde estão pressão e risco).  
    **[Derived from BRD v1.0 + incremento solicitado]**

12. Ausência (ou baixa clareza) de leitura estruturada de **bolsas vs descontos**, e do impacto financeiro total dessas concessões.  
    **[Open question / Needs validation: existência e política de bolsa]**

13. Ausência de leitura estruturada de **ocupação por turma** (capacidade vs matriculados), dificultando avaliar ociosidade e eficiência.  
    **[Directly stated in BRD v1.0 (ocupação como lacuna) + incremento solicitado]**

14. Dificuldade de localizar pontos específicos de pressão por desconto e evasão ao longo da jornada (ex.: séries de transição).  
    **[Derived from BRD v1.0 + incremento solicitado]**

15. Baixa padronização de conceitos (o que é desconto, o que é bolsa, o que é aluno ativo, o que é rematrícula elegível) pode gerar divergências internas e ruído nos indicadores.  
    **[Directly stated in BRD v1.0 (padronização) + incremento solicitado]**

---

## Derived Challenges and Secondary Risks

As inferências do BRD v1.0 permanecem válidas — decisão com baixa confiabilidade informacional, dificuldade de precificar, desconto sem cálculo de impacto, baixa previsibilidade de caixa, invisibilidade de rentabilidade real, dificuldade de agir preventivamente e risco de abandono por complexidade.  
**[Directly stated in BRD v1.0 + Derived from BRD v1.0]**

### Incrementos v1.1 — efeitos de concentração e eficiência

- **Concessões concentradas por turma/série podem “comprimir” a receita efetiva** de forma não visível no consolidado. Monitorar a relação entre taxa de desconto, matrículas e receita líquida é prática recomendada em estudos de desconto educacional.  
  **[Derived from BRD v1.0 + incremento solicitado]**

- **Baixa ocupação por turma pode elevar custo por aluno** e reduzir eficiência operacional. Abordagens de capacidade escolar comparam capacidade e matrícula (“number on roll”) para identificar vagas excedentes e apoiar decisões de alocação de recursos.  
  **[Derived from BRD v1.0 + incremento solicitado]**

- **Evasão concentrada em transições** (entre ciclos/anos) pode exigir ação específica de retenção, e não apenas desconto.  
  **[Derived from BRD v1.0 + incremento solicitado]**

- **Misturar bolsa e desconto comercial** pode distorcer a análise de sustentabilidade: bolsa tende a ter lógica/política distinta e precisa ser rastreável para gestão.  
  **[Derived from BRD v1.0 + incremento solicitado]**

---

## Business Strengths and Opportunities

1. Escola já em operação, com base ativa de alunos.  
   **[Directly stated in BRD v1.0]**

2. Estrutura organizacional enxuta, favorecendo ajustes rápidos.  
   **[Directly stated in BRD v1.0]**

3. Número de alunos administrável para uma primeira virada de gestão com dados.  
   **[Directly stated in BRD v1.0]**

4. Necessidade clara reconhecida pela liderança (possível patrocínio interno).  
   **[Directly stated in BRD v1.0]**

5. Potencial de ganhos rápidos com organização mínima de dados e visão gerencial simples.  
   **[Directly stated in BRD v1.0]**

### Oportunidades ampliadas (v1.1)

- Direcionar ações onde o efeito marginal é maior (retenção e concessões), ao identificar concentração por segmento/série/turma.  
  **[Derived from BRD v1.0 + incremento solicitado]**

- Rebalancear concessões (desconto/bolsa) para preservar sustentabilidade, medindo impacto na receita efetiva.  
  **[Derived from BRD v1.0 + incremento solicitado]**

- Melhorar eficiência de capacidade (ocupação por turma) para reduzir ociosidade e apoiar decisões de organização de vagas/turmas.  
  **[Derived from BRD v1.0 + incremento solicitado]**

---

## Strategic Business Objectives

1. Estabelecer controle financeiro mensal confiável e consolidado.  
   **[Directly stated in BRD v1.0]**

2. Dar visibilidade à estrutura de custos, com destaque para aluguel e folha.  
   **[Directly stated in BRD v1.0]**

3. Avaliar sustentabilidade da mensalidade frente à operação atual.  
   **[Directly stated in BRD v1.0]**

4. Monitorar retenção, rematrícula e perda de alunos com maior clareza.  
   **[Directly stated in BRD v1.0]**

5. Criar base objetiva para decisões sobre desconto.  
   **[Directly stated in BRD v1.0]**

6. Reduzir dependência de controles manuais e da memória operacional.  
   **[Directly stated in BRD v1.0]**

7. Criar cultura inicial de tomada de decisão orientada por dados.  
   **[Directly stated in BRD v1.0]**

### Objetivo adicional (v1.1)

8. Obter visibilidade segmentada (**segmento → série/ano → turma**) para localizar concentração de risco/pressão e orientar ações específicas de sustentabilidade, retenção, política de concessões (desconto/bolsa) e ocupação.  
   **[Derived from BRD v1.0 + incremento solicitado]**

---

## Key Business Questions the Dashboard Must Answer

As perguntas originais permanecem obrigatórias e são preservadas:

- resultado mensal;
- entradas/saídas;
- peso de aluguel/folha;
- custo por aluno;
- sustentabilidade;
- desconto e margem;
- entradas/permanências/saídas;
- taxa de rematrícula;
- taxa de perda;
- motivos;
- impacto da perda;
- ponto de equilíbrio;
- alunos mínimos.

**[Directly stated in BRD v1.0]**

### Perguntas adicionais (v1.1) para localizar “onde” está o problema

- Em quais **segmentos** a margem parece mais pressionada (receita por aluno vs custo por aluno)?  
  **[Derived from BRD v1.0 + incremento solicitado]**

- Em quais **séries/turmas** a taxa de rematrícula e a taxa de perda são mais críticas?  
  **[Derived from BRD v1.0 + incremento solicitado]**

- Onde descontos e bolsas estão mais concentrados por recorte e qual o impacto total dessas concessões sobre a receita efetiva?  
  **[Derived from BRD v1.0 + incremento solicitado]**

- Qual é o percentual de bolsistas e quanto representa, em valor, de renúncia de receita por segmento/turma?  
  **[Open question / Needs validation: existência e política de bolsa]**

- Quais turmas estão com menor taxa de ocupação e qual o impacto potencial no custo por aluno/eficiência?  
  **[Derived from BRD v1.0 + incremento solicitado]**

- Motivos de saída (preço/concorrência/outros) variam por segmento/série?  
  **[Derived from BRD v1.0 + incremento solicitado]**

- Qual recorte concentra maior risco de inadimplência (se houver dados estruturados)?  
  **[Open question / Needs validation: dados de inadimplência]**

---

## Initial Business Requirements

Os requisitos do BRD v1.0 permanecem e são preservados como base do produto:

- consolidar receitas/despesas;
- resultado mensal;
- custos por categoria;
- destaque aluguel/folha;
- custo por aluno;
- mensalidade média e efeito de descontos;
- acompanhar rematrícula/retenção/saídas;
- registrar motivos de saída;
- simplicidade;
- confiabilidade;
- reduzir papel;
- apoiar decisão;
- alertas.

**[Directly stated in BRD v1.0]**

### Requisitos incrementais (v1.1)

- A solução deve permitir **visão consolidada e segmentada** por: segmento, série/ano e turma (com filtros simples e leitura executiva).  
  **[Derived from BRD v1.0 + incremento solicitado]**

- A solução deve permitir leitura por **status do aluno** (ativo/novo/rematriculado/evadido/inativo) e **status de rematrícula** (elegível/rematriculado/não rematriculado/pendente).  
  **[Open question / Needs validation: definições internas]**

- A solução deve permitir análise de **desconto** por recorte (incluindo faixa de desconto), evidenciando impacto sobre receita efetiva.  
  **[Derived from BRD v1.0 + incremento solicitado]**

- A solução deve permitir análise de **bolsas** separadamente de desconto comercial, acompanhando:
  - contagem e percentual de bolsistas;
  - valor concedido (mensal e acumulado no período);
  - distribuição por segmento/série/turma;
  - tipo/faixa de bolsa (mínimo: integral vs parcial).  
  **[Open question / Needs validation: existência e política]**

- A solução deve suportar **ocupação por turma** (capacidade, matriculados, taxa), para identificar ociosidade e apoiar decisões gerenciais.  
  **[Derived from BRD v1.0 + incremento solicitado]**

- A solução deve preservar simplicidade de uso (baixa maturidade digital), mesmo com maior profundidade analítica (camadas de detalhe opcionais).  
  **[Directly stated in BRD v1.0 + Derived from BRD v1.0]**

### Campos mínimos recomendados para cadastro/registro (v1.1)

Estes campos são recomendados para viabilizar a segmentação e as leituras gerenciais sem inflar complexidade.

#### Campos acadêmicos

- `segmento` (Infantil / Fundamental I / Fundamental II)
- `serie_ano` (Maternal, Jardim I, Jardim II, 1º–9º)
- `turma` (ex.: `1º Ano A`)

**[Open question / Needs validation: taxonomia interna]**

#### Campos de status

- `status_aluno` (ativo/novo/rematriculado/evadido/inativo)
- `status_rematricula` (elegível/rematriculado/não rematriculado/pendente)

**[Open question / Needs validation: regras e critérios]**

#### Campos de concessões

- `desconto_valor` e/ou `desconto_percentual`
- `faixa_desconto` (sem / até 5% / 6–10% / acima de 10%)

**[Derived from BRD v1.0 + incremento solicitado]**

#### Campos mínimos de bolsista (para distinguir de desconto)

- `bolsista_flag` (sim/não)
- `bolsa_tipo` (integral/parcial/outro)
- `bolsa_valor` e/ou `bolsa_percentual`
- `bolsa_inicio_periodo` (opcional, se houver sazonalidade/prazo)

**[Open question / Needs validation: política e forma de concessão]**

> **Nota de justificativa:** acompanhar concessões (bolsa/auxílio) separadamente reduz o risco de “misturar” causas de redução de receita e melhora a leitura de receita líquida de mensalidades.

#### Campos de saída e risco

- `data_saida`
- `motivo_saida` (preço/concorrência/mudança/insatisfação/dificuldade financeira/outros)
- `situacao_financeira` (adimplente/atraso leve/atraso crítico/negociação/inadimplente)

**[Directly stated in BRD v1.0 (motivo de saída como necessidade) + incremento solicitado]**

#### Campos de ocupação por turma

- `capacidade_turma`
- `matriculados_turma` (derivado de alunos ativos na turma)
- `taxa_ocupacao` (derivado)

**[Open question / Needs validation: capacidade instalada por turma]**

### KPIs novos recomendados por recorte (v1.1)

KPIs adicionais para permitir gestão comparativa e localizar concentrações, mantendo foco em simplicidade.

#### KPIs por segmento/série/turma (mínimo)

- Alunos ativos por recorte
- Receita recebida por recorte
- Desconto médio por recorte (valor e/ou %)
- Bolsistas (contagem, % e valor concedido) por recorte
- Taxa de rematrícula por recorte
- Taxa de perda por recorte
- Taxa de ocupação por turma

**[Derived from BRD v1.0 + incremento solicitado]**

#### KPIs condicionais (dependem de dados)

- Inadimplência por recorte (valor e taxa)

**[Open question / Needs validation]**

---

## Critical Validation Gaps

As lacunas originais são preservadas:

- receita média mensal;
- custo de aluguel e peso;
- custo de folha;
- inadimplência e seu peso;
- mensalidade média por segmento/turma;
- volume de descontos;
- sazonalidade de entrada/saída;
- motivos reais de evasão;
- capacidade total e taxa de ocupação;
- outras receitas;
- disponibilidade da equipe;
- governança dos dados;
- decisões mensais sem base objetiva.

**[Directly stated in BRD v1.0]**

### Lacunas adicionais necessárias para viabilizar o incremento v1.1

- A escola possui hoje cadastro confiável de **segmento, série/ano e turma** por aluno (histórico e atual)?  
  **[Open question / Needs validation]**

- Existe registro da **capacidade por turma** (não apenas capacidade total) para medir taxa de ocupação e ociosidade?  
  **[Open question / Needs validation]**

- Existe uma política formal de **bolsa** (integral/parcial) e ela é distinta do desconto comercial? Se sim, como medir (valor, percentual, ambos)?  
  **[Open question / Needs validation]**

- Qual definição será adotada para **aluno ativo**, **aluno elegível para rematrícula** e **status de rematrícula** (para evitar distorção de taxas)?  
  **[Open question / Needs validation]**

- A escola deseja registrar **situação financeira** em qual granularidade (por aluno, por mensalidade, por período)?  
  **[Open question / Needs validation]**

---

## Recommended Next Steps

### Validação executiva com direção/sócios (prioridade máxima)

- Confirmar abrangência real de segmentos/séries (principalmente Fundamental II).  
  **[Needs validation]**

- Aprovar taxonomia de:
  - segmento, série/ano e turma;
  - motivos de saída;
  - status do aluno e rematrícula;
  - faixas de desconto;
  - política de bolsa e campos mínimos (se aplicável).  
  **[Needs validation]**

### Padronização mínima de dados (antes de evoluir PRD/SDD)

- Definir um **cadastro mínimo do aluno** com os campos do incremento v1.1 (segmentação + concessões + motivo de saída + status).  
  **[Derived from BRD v1.0 + incremento solicitado]**

- Definir categorias financeiras mínimas (receitas/despesas) e padronizar o que é desconto vs bolsa.  
  **[Derived from BRD v1.0 + incremento solicitado]**

### Desdobramento documental

- Atualizar o **PRD para v1.1** com:
  - filtros por segmento/série/turma;
  - KPIs por recorte;
  - visões específicas de bolsas, descontos e ocupação por turma;
  - critérios de alerta por recorte (ex.: turma com ocupação baixa e alta concessão).  
  **[Derived from BRD v1.0 + incremento solicitado]**

### Nota explícita que impacta SRS/SDD posteriores

- Estratégia de entrega recomendada: **MVP local-first** para adoção rápida e estabilização de rotinas de dados, com arquitetura **cloud-ready** para evolução posterior (migração sem reescrever o modelo).  
  **[Derived from BRD v1.0 (adoção simples) + incremento solicitado]**

- Implicação para SRS/SDD: o modelo de dados deve suportar segmentação (segmento/série/turma) e concessões (desconto e bolsa separados) desde a base, mesmo que algumas análises sejam liberadas por fase.  
  **[Derived from incremento solicitado]**

---

## Matriz de rastreabilidade do incremento

> **Observação:** a coluna “PRD Module/Requirement” referencia os módulos e temas que normalmente serão formalizados no PRD do dashboard (ex.: filtros, alunos, receitas, custos). Caso o PRD v1.0 não esteja anexado neste momento, esta matriz deve ser validada ao atualizar o PRD para v1.1.  
> **[Needs validation]**

| PRD Module/Requirement | BRD Change (v1.1) | Data Dependency | Priority | Source Type |
|---|---|---|---|---|
| Filtros gerais (período + recortes) | Incluir filtros por segmento / série / turma | cadastro de aluno com `segmento`, `serie_ano`, `turma` | MVP | Derived from BRD v1.0 + incremento |
| Resumo executivo financeiro | Manter visão consolidada + permitir “quebrar” por segmento | receitas, despesas, alunos ativos por recorte | MVP | Directly stated + incremento |
| Alunos e Retenção | Analisar rematrícula/perda por segmento/série/turma | status aluno, status rematrícula, entradas/saídas | MVP | Directly stated + incremento |
| Descontos | Adicionar faixa de desconto e análise por recorte | desconto (%/valor), faixa, mensalidade | MVP | Directly stated + incremento |
| Bolsas | Diferenciar bolsa de desconto; analisar total, %, valor e distribuição | `bolsista_flag`, `bolsa_tipo`, bolsa (%/valor) | Fase 1 (se houver política) | Open question / Needs validation |
| Ocupação por turma | Adicionar capacidade por turma e taxa de ocupação | `capacidade_turma`, alunos ativos por turma | Fase 1 | Directly stated (lacuna) + incremento |
| Motivo de saída | Cruzar motivo de saída com segmento/série/turma | `motivo_saida` padronizado | MVP | Directly stated + incremento |
| Situação financeira / inadimplência | Introduzir “situação financeira”; inadimplência segmentada condicional | registros de pagamentos/abertos | Pós-MVP ou condicional | Open question / Needs validation |

---

## Referências externas usadas para justificar recomendações analíticas

As referências abaixo reforçam:

1. por que concessões (desconto/bolsa) devem ser monitoradas em relação à receita efetiva;
2. por que capacidade/ocupação é dimensão crítica para eficiência e planejamento.

- AIR — “Net tuition revenue (gross tuition and fees – grant aid)” e risco de erosão por discounting.
- NACUBO — importância de entender a relação entre discount rate, matrículas e net tuition revenue.
- Department for Education (Inglaterra) — método de “Net Capacity” e comparação com matrícula (“number on roll”) para identificar vagas excedentes.
- GOV.UK — guia do “school capacity survey” (SCAP) coletando dados de capacidade e previsões, reforçando a prática de medir capacidade e demanda.

### Links (opcional, caso queira manter URLs explícitas no arquivo)

- `https://www.airweb.org/resources/publications/professional-file/article-133`
- `https://www.nacubo.org/Events/2025/Tuition-Discounting-Results`
- `https://assets.publishing.service.gov.uk/media/6543e2e2d36c91000d935ce8/Measuring_school_capacity_guide_for_LAs_-_summary_guide_for_local_authorities.pdf`
- `https://www.gov.uk/guidance/school-capacity-survey-guide-for-local-authorities`
```
