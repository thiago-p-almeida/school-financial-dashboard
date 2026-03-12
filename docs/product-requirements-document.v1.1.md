# PRD — @CESOL School Financial and Administrative Dashboard v1.1

## PARTE 1 — Change Summary

### O que foi alterado em relação ao PRD original

O PRD v1.1 preserva o núcleo funcional do PRD v1.0 — visão consolidada financeira, acompanhamento de receitas, despesas, resultado mensal, rematrícula, retenção, evasão, leitura de desconto, sustentabilidade da mensalidade e simplicidade para baixa maturidade digital — e incorpora a nova camada analítica introduzida pelo BRD v1.1.

As principais mudanças são:

- inclusão de leitura **segmentada** por:
  - segmento de ensino
  - série/ano
  - turma
- ampliação de filtros para suportar:
  - status do aluno
  - status de rematrícula
  - faixa de desconto
  - situação financeira
  - bolsista / não bolsista
  - motivo de saída
- evolução funcional dos módulos para permitir:
  - comparação entre segmentos, séries e turmas
  - leitura de ocupação por turma
  - leitura de bolsas separadamente de descontos
  - cruzamento entre evasão e motivo de saída
- ampliação dos requisitos analíticos com KPIs por recorte
- ampliação dos requisitos de dados com novos campos mínimos necessários
- revisão da priorização entre:
  - MVP
  - Pós-MVP
  - itens que dependem de validação

### Por que essas alterações foram necessárias

O BRD v1.1 deixa claro que a visão consolidada continua importante, mas não é suficiente sozinha para orientar decisões melhores sobre:

- sustentabilidade financeira
- concentração de descontos
- impacto das bolsas
- evasão
- retenção
- baixa ocupação
- risco por etapa da jornada escolar

Em termos de produto, isso significa que o dashboard precisa deixar de responder apenas “como a escola está no total” e passar a responder também:

- **onde** estão os problemas
- **onde** estão as pressões de margem
- **onde** estão as perdas
- **onde** descontos e bolsas estão concentrados
- **onde** a ocupação está baixa

### Seções impactadas

As seções atualizadas foram:

- Product Overview
- BRD Alignment Summary
- Target Users
- Product Goals
- Key Business Questions the Product Must Answer
- Product Scope
- Core Product Modules
- Functional Requirements
- Analytical and KPI Requirements
- Business Rules
- Data Requirements
- UX and Adoption Requirements
- Non-Functional Requirements
- MVP Definition
- Acceptance Criteria
- Dependencies and Risks
- Open Questions / Items to Validate
- Traceability Matrix
- SDD Readiness Notes
- Recommended Next Step

### O que mudou no MVP

Entram no MVP v1.1:

- filtros por período, segmento, série/ano e turma
- leitura segmentada de indicadores principais
- visão de ocupação por turma
- visão de desconto por recorte
- leitura por status do aluno e status de rematrícula
- comparação entre segmentos/séries/turmas
- estrutura funcional para separar bolsa de desconto, quando houver dados e política mínima definidas

### O que ficou como Pós-MVP ou dependente de validação

Ficam como **Pós-MVP / Future Release** ou **Needs validation before prioritization**:

- módulo robusto de inadimplência segmentada
- análises mais profundas por bolsa, se a política de bolsas não estiver minimamente estruturada
- comparações históricas avançadas por turma/série
- cenários simulados por recorte
- margem detalhada por turma, se os dados não permitirem cálculo consistente
- segmentações adicionais que aumentem complexidade sem valor imediato

---

# PRD — @CESOL School Financial and Administrative Dashboard v1.1

## 1. Product Overview

O **@CESOL School Financial and Administrative Dashboard** é um produto de gestão orientado por dados, criado para oferecer à liderança escolar uma visão clara, confiável e simples do desempenho financeiro, da retenção de alunos e da sustentabilidade operacional da escola.

Na versão v1.1, o produto deixa de ser apenas um painel de leitura consolidada da escola e passa a incluir também uma camada de leitura **segmentada, comparativa e gerencial**, permitindo que a liderança entenda não apenas o desempenho total da operação, mas também **onde** estão receita, risco, pressão de margem, evasão, concentração de descontos, bolsas e baixa ocupação.

O produto continua destinado principalmente à liderança e à gestão administrativa, com uso operacional secundário pela secretária escolar ou por uma pessoa designada para cuidar dos dados. Seu objetivo permanece sendo transformar registros dispersos em uma visão gerencial confiável, com a diferença de que agora essa visão precisa suportar comparação por **segmento, série/ano e turma**, sem perder simplicidade de uso.

---

## 2. BRD Alignment Summary

### Principais dores de negócio endereçadas
- controle financeiro manual e baixa digitalização
- falta de planilhas estruturadas e de informações consolidadas
- perda de dados e lentidão na verificação de registros
- pressão competitiva de escolas com mensalidades menores
- pressão por descontos sem clareza sobre o impacto
- risco de evasão e baixa visibilidade sobre retenção
- forte pressão de custos com aluguel
- baixa maturidade digital em parte da liderança
- falta de visibilidade por segmento, série e turma
- ausência de leitura estruturada de bolsas e seu impacto financeiro
- ausência de leitura estruturada de ocupação por turma
- dificuldade de localizar com precisão onde estão as pressões de evasão e concessão

### Principais objetivos estratégicos suportados
- estabelecer controle financeiro mensal confiável
- melhorar a visibilidade da estrutura de custos, especialmente aluguel e folha
- avaliar a sustentabilidade da mensalidade
- monitorar retenção, rematrícula e perda de alunos
- apoiar decisões mais objetivas sobre descontos
- reduzir dependência de controles manuais e da memória operacional
- criar uma cultura inicial de gestão orientada por dados
- obter visibilidade segmentada da operação por nível, série, turma e condições gerenciais associadas

### Principais restrições absorvidas
- o produto deve continuar simples e utilizável por pessoas com baixa maturidade digital
- a nova profundidade analítica não pode transformar o dashboard em uma ferramenta difícil de usar
- parte relevante dos novos recortes depende de padronização mínima de dados
- algumas leituras, como bolsas e inadimplência segmentada, dependem de validação de política e disponibilidade de dados

### Principais riscos considerados
- resistência cultural à adoção digital
- baixa qualidade inicial dos dados
- expectativa excessiva de que o dashboard resolva sozinho os problemas de processo
- dependência de alimentação regular e correta dos dados
- risco de visualização complexa demais para o público principal
- risco de inconsistência entre desconto e bolsa
- risco de segmentação pouco confiável por falta de cadastro estruturado de série/turma
- risco de leitura distorcida por falta de capacidade por turma

---

## 3. Target Users

### 3.1 Usuários Primários

#### A. Sócios / Liderança Escolar
- **Papel:** tomadores de decisão estratégica e financeira
- **Necessidades:** visibilidade clara do desempenho financeiro mensal, da estrutura de custos, da sustentabilidade da mensalidade, da retenção de alunos e das áreas de risco do negócio
- **Frequência de uso esperada:** semanal e mensal, com uso mais intenso em períodos de revisão financeira e rematrícula
- **Valor esperado:** melhor qualidade de decisão, visão gerencial compartilhada, identificação mais rápida de riscos e prioridades
- **Evolução v1.1:** passam a precisar de leitura comparativa por segmento, série/ano e turma para localizar concentração de risco, pressão de margem e pontos de perda

#### B. Gestão Administrativa
- **Papel:** acompanhamento diário dos indicadores operacionais e financeiros
- **Necessidades:** visão consolidada de recebimentos, despesas, movimentação de alunos e indicadores críticos
- **Frequência de uso esperada:** diária ou várias vezes por semana
- **Valor esperado:** melhor controle, menos retrabalho, maior rapidez na verificação da saúde operacional da escola
- **Evolução v1.1:** passam a precisar de filtros e recortes que permitam entender onde estão descontos, bolsas, baixa ocupação e maior risco de evasão

### 3.2 Usuários Secundários

#### C. Secretária Escolar / Operador(a) Designado(a) dos Dados
- **Papel:** alimentação operacional e manutenção das bases de registro
- **Necessidades:** fluxos simples, interação de baixo atrito, organização compreensível dos dados
- **Frequência de uso esperada:** uso operacional frequente
- **Valor esperado:** maior facilidade de consolidação das informações, menor dependência de papel, rotinas mais organizadas
- **Evolução v1.1:** passa a depender de maior clareza sobre campos mínimos obrigatórios de segmentação e status

#### D. Futuro Responsável por Dados ou Financeiro
- **Papel:** futuro responsável pela governança dos dados ou pelo acompanhamento financeiro
- **Necessidades:** base de produto confiável e estruturada
- **Frequência de uso esperada:** precisa ser validada
- **Valor esperado:** sustentabilidade das rotinas de gestão e continuidade das informações

---

## 4. Product Goals

### PG-01 — Fornecer visibilidade financeira mensal confiável
- **Relação com objetivo do BRD:** estabelecer controle financeiro mensal confiável
- **Prioridade:** MVP
- **Origem:** Directly stated in BRD v1.1

### PG-02 — Tornar a estrutura de custos da escola visível e interpretável
- **Relação com objetivo do BRD:** dar visibilidade aos custos, especialmente aluguel e folha
- **Prioridade:** MVP
- **Origem:** Directly stated in BRD v1.1

### PG-03 — Apoiar a avaliação da sustentabilidade da mensalidade
- **Relação com objetivo do BRD:** avaliar se a mensalidade atual sustenta a operação
- **Prioridade:** MVP
- **Origem:** Directly stated in BRD v1.1

### PG-04 — Monitorar retenção e perda de alunos com indicadores objetivos
- **Relação com objetivo do BRD:** monitorar rematrícula, retenção e perda de alunos
- **Prioridade:** MVP
- **Origem:** Directly stated in BRD v1.1

### PG-05 — Apoiar decisões mais objetivas sobre descontos
- **Relação com objetivo do BRD:** criar base objetiva para decisões sobre desconto
- **Prioridade:** MVP
- **Origem:** Directly stated in BRD v1.1

### PG-06 — Reduzir dependência de controles manuais e não consolidados
- **Relação com objetivo do BRD:** reduzir dependência de papel e memória
- **Prioridade:** MVP
- **Origem:** Directly stated in BRD v1.1

### PG-07 — Criar uma primeira camada utilizável de cultura de gestão orientada por dados
- **Relação com objetivo do BRD:** construir cultura inicial de tomada de decisão orientada por dados
- **Prioridade:** MVP
- **Origem:** Directly stated in BRD v1.1

### PG-08 — Criar visibilidade segmentada da operação escolar
- **Relação com objetivo do BRD:** obter visibilidade segmentada por nível, série, turma e condições gerenciais associadas
- **Prioridade:** MVP
- **Origem:** Directly stated in BRD v1.1

### PG-09 — Permitir leitura comparativa de pressão de margem, retenção e risco por recorte
- **Relação com objetivo do BRD:** localizar onde estão receita, risco, pressão e retenção
- **Prioridade:** MVP
- **Origem:** Derived from BRD v1.1

### PG-10 — Dar transparência ao impacto de bolsas e descontos na receita efetiva
- **Relação com objetivo do BRD:** separar bolsa de desconto e avaliar impacto financeiro das concessões
- **Prioridade:** Needs validation before prioritization
- **Origem:** Derived from BRD v1.1 / Open question

### PG-11 — Ampliar a profundidade analítica após melhoria da maturidade dos dados
- **Relação com objetivo do BRD:** preparar a escola para uma gestão mais profissional e escalável
- **Prioridade:** Post-MVP / Future Release
- **Origem:** Directly stated in BRD v1.1

---

## 5. Key Business Questions the Product Must Answer

### Perguntas consolidadas preservadas

#### Q-01 — Estamos operando com lucro ou prejuízo no mês?
- **Por que importa:** requisito central para a sustentabilidade do negócio
- **Respondida por:** Resumo Executivo; KPIs de receita, despesa e resultado
- **Classificação:** Directly stated in BRD v1.1

#### Q-02 — Quanto realmente entra e quanto realmente sai da escola em cada mês?
- **Por que importa:** necessário para o controle financeiro básico e visibilidade de caixa
- **Respondida por:** Resumo Executivo e Receitas
- **Classificação:** Directly stated in BRD v1.1

#### Q-03 — Quanto o aluguel pesa na operação?
- **Por que importa:** aluguel é um custo crítico e uma desvantagem competitiva
- **Respondida por:** Estrutura de Custos
- **Classificação:** Directly stated in BRD v1.1

#### Q-04 — Quanto a folha pesa na operação?
- **Por que importa:** custo crítico para sustentabilidade
- **Respondida por:** Estrutura de Custos
- **Classificação:** Directly stated in BRD v1.1

#### Q-05 — Quanto custa manter a escola funcionando?
- **Por que importa:** necessário para entender a carga operacional mensal
- **Respondida por:** Estrutura de Custos
- **Classificação:** Directly stated in BRD v1.1

#### Q-06 — Quanto custa manter cada aluno?
- **Por que importa:** apoia decisões de preço, desconto e sustentabilidade
- **Respondida por:** Viabilidade e Sustentabilidade da Mensalidade
- **Classificação:** Directly stated in BRD v1.1

#### Q-07 — A mensalidade atual sustenta a estrutura de custos da escola?
- **Por que importa:** sustentabilidade da mensalidade é uma das principais preocupações do negócio
- **Respondida por:** Viabilidade e Sustentabilidade da Mensalidade
- **Classificação:** Directly stated in BRD v1.1

#### Q-08 — Os descontos concedidos estão comprometendo a margem?
- **Por que importa:** a pressão por desconto é alta e precisa ser avaliada objetivamente
- **Respondida por:** Receitas + Viabilidade
- **Classificação:** Directly stated in BRD v1.1

#### Q-09 — Quantos alunos entram, permanecem e saem?
- **Por que importa:** retenção e perda impactam diretamente a sustentabilidade financeira
- **Respondida por:** Alunos e Retenção
- **Classificação:** Directly stated in BRD v1.1

#### Q-10 — Qual é a taxa de rematrícula?
- **Por que importa:** indicador-chave de retenção
- **Respondida por:** Alunos e Retenção
- **Classificação:** Directly stated in BRD v1.1

#### Q-11 — Qual é a taxa de perda de alunos?
- **Por que importa:** necessário para entender evasão e risco
- **Respondida por:** Alunos e Retenção
- **Classificação:** Directly stated in BRD v1.1

#### Q-12 — Estamos perdendo alunos principalmente por preço, concorrência ou outros fatores?
- **Por que importa:** necessário para sair da reação e partir para ações de retenção mais informadas
- **Respondida por:** Alunos e Retenção
- **Classificação:** Directly stated in BRD v1.1

#### Q-13 — Qual é o impacto financeiro de perder alunos para a concorrência?
- **Por que importa:** transforma a evasão em impacto gerencial concreto
- **Respondida por:** Viabilidade + Alunos e Retenção
- **Classificação:** Directly stated in BRD v1.1

#### Q-14 — Qual é o ponto de equilíbrio mínimo da operação?
- **Por que importa:** é crítico para decisões em cenário de pressão financeira
- **Respondida por:** Viabilidade
- **Classificação:** Directly stated in BRD v1.1

#### Q-15 — Quantos alunos precisamos manter para operar sem prejuízo?
- **Por que importa:** apoia decisões sobre mensalidade, capacidade e sustentabilidade
- **Respondida por:** Viabilidade
- **Classificação:** Directly stated in BRD v1.1

### Perguntas novas da versão v1.1

#### Q-16 — Em quais segmentos a margem parece mais pressionada?
- **Por que importa:** o consolidado pode esconder pressão concentrada
- **Respondida por:** Desempenho por Segmento + Viabilidade
- **Classificação:** Derived from BRD v1.1

#### Q-17 — Em quais séries/turmas a taxa de rematrícula e a taxa de perda são mais críticas?
- **Por que importa:** ajuda a localizar onde a retenção falha
- **Respondida por:** Alunos e Retenção por Recorte
- **Classificação:** Derived from BRD v1.1

#### Q-18 — Onde descontos estão mais concentrados por segmento, série ou turma?
- **Por que importa:** ajuda a localizar compressão de receita
- **Respondida por:** Receitas + Concessões
- **Classificação:** Derived from BRD v1.1

#### Q-19 — Onde bolsas estão mais concentradas e qual seu impacto financeiro?
- **Por que importa:** bolsa e desconto não devem ser misturados
- **Respondida por:** Concessões / Bolsas
- **Classificação:** Open question / Needs validation

#### Q-20 — Quais turmas apresentam baixa ocupação?
- **Por que importa:** baixa ocupação pode elevar custo por aluno e reduzir eficiência
- **Respondida por:** Ocupação por Turma
- **Classificação:** Derived from BRD v1.1

#### Q-21 — Há turmas aparentemente cheias, mas com margem baixa?
- **Por que importa:** ocupação isolada não garante sustentabilidade
- **Respondida por:** Ocupação + Viabilidade
- **Classificação:** Derived from BRD v1.1

#### Q-22 — Motivos de saída variam por segmento, série ou turma?
- **Por que importa:** ajuda a entender se o problema é preço, concorrência ou outro fator por etapa
- **Respondida por:** Alunos e Retenção por Recorte
- **Classificação:** Derived from BRD v1.1

#### Q-23 — Qual recorte concentra maior risco de inadimplência?
- **Por que importa:** permite localizar pressão financeira se houver dados
- **Respondida por:** Inadimplência por Recorte
- **Classificação:** Open question / Needs validation

---

## 6. Product Scope

### 6.1 In Scope (MVP)

- dashboard único de gestão, com foco em visibilidade administrativa, financeira e de retenção
- resumo executivo com indicadores mensais de alto nível
- visão de retenção de alunos incluindo entradas, saídas, rematrículas e indicadores de perda
- consolidação de receitas e despesas por mês
- visibilidade da estrutura de custos com destaque para aluguel e folha
- análise de viabilidade da mensalidade com base em custo e receita por aluno
- suporte ao registro e análise dos motivos de saída de alunos
- alertas visuais para condições críticas de risco
- filtros por:
  - período
  - segmento
  - série/ano
  - turma
- leitura por:
  - status do aluno
  - status de rematrícula
  - faixa de desconto
- comparação entre segmentos, séries e turmas nos indicadores principais
- leitura de ocupação por turma, se houver capacidade por turma validada
- leitura funcional preparada para diferenciar bolsa de desconto, quando houver dados mínimos validados

### 6.2 Post-MVP / Future Releases

- análises históricas mais profundas por segmento/série/turma
- módulo mais robusto de inadimplência por recorte
- simulações de cenário por turma, segmento ou política de concessão
- análises operacionais mais amplas além do escopo financeiro e de retenção
- regras mais sofisticadas de alerta por recorte
- comparações avançadas entre bolsa, desconto, margem e retenção
- expansão de governança e auditabilidade

### 6.3 Out of Scope

- substituição completa de um ERP
- plataforma completa de gestão escolar
- analytics preditivo avançado no primeiro ciclo
- análises pedagógicas amplas não relacionadas aos objetivos do BRD
- suporte complexo a múltiplas unidades
- automação altamente sofisticada na primeira versão

---

## 7. Core Product Modules

### 7.1 Filtros Gerais
- **Objetivo:** permitir que a liderança restrinja as visualizações por dimensões relevantes
- **Principais dados exibidos:** período, segmento, série/ano, turma e, quando viável, status do aluno, status de rematrícula, faixa de desconto, situação financeira e motivo de saída
- **Perguntas que responde:** como o desempenho varia por recorte acadêmico e gerencial?
- **Prioridade:** MVP
- **Origem no BRD:** Derived from BRD v1.1

### 7.2 Resumo Executivo
- **Objetivo:** oferecer uma visão rápida e de alto nível da situação financeira e operacional da escola
- **Principais dados exibidos:** alunos ativos, receita recebida, despesas totais, resultado mensal, indicadores principais de risco
- **Perguntas que responde:** estamos financeiramente saudáveis neste mês? Qual é a situação imediata do negócio?
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1

### 7.3 Alunos e Retenção
- **Objetivo:** tornar a movimentação de alunos visível e mensurável
- **Principais dados exibidos:** novos alunos, rematrículas, saídas, taxa de rematrícula, taxa de perda, motivos de saída
- **Extensão v1.1:** suportar leitura por segmento, série/ano, turma e status do aluno
- **Perguntas que responde:** estamos conseguindo reter alunos? Onde a retenção está falhando? Por que os alunos estão saindo?
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1 + Derived

### 7.4 Visão de Receitas
- **Objetivo:** mostrar o que era esperado em receita versus o que foi efetivamente recebido
- **Principais dados exibidos:** receita bruta, receita recebida, média de mensalidade, impacto de descontos
- **Extensão v1.1:** suportar leitura por recorte acadêmico e por faixa de desconto
- **Perguntas que responde:** quanto dinheiro realmente está entrando? Onde os descontos estão mais concentrados?
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1 + Derived

### 7.5 Estrutura de Custos
- **Objetivo:** mostrar para onde o dinheiro está indo, especialmente nas categorias críticas
- **Principais dados exibidos:** despesas totais, aluguel, folha, categorias de custo, participação dos custos
- **Perguntas que responde:** quais são os principais fatores de custo? Qual o peso do aluguel e da folha?
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1

### 7.6 Viabilidade e Sustentabilidade da Mensalidade
- **Objetivo:** conectar receita, mensalidade, custos e base de alunos em indicadores de sustentabilidade
- **Principais dados exibidos:** custo por aluno, receita por aluno, margem por aluno, ponto de equilíbrio, alunos mínimos para operar
- **Extensão v1.1:** permitir leitura comparativa por segmento, série/ano e, quando viável, por turma
- **Perguntas que responde:** a mensalidade atual sustenta a operação? Onde a margem está mais pressionada?
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1 + Derived

### 7.7 Concessões (Descontos e Bolsas)
- **Objetivo:** tornar visível o impacto das concessões na receita efetiva
- **Principais dados exibidos:** desconto médio, concentração de descontos, bolsistas, percentual de bolsistas, valor concedido em bolsas
- **Perguntas que responde:** onde a concessão está mais concentrada? Qual o impacto financeiro total de descontos e bolsas?
- **Prioridade:** MVP para descontos; Needs validation before prioritization para bolsas
- **Origem no BRD:** Derived from BRD v1.1 / Open question for bolsas

### 7.8 Ocupação por Turma
- **Objetivo:** permitir leitura de eficiência de capacidade
- **Principais dados exibidos:** capacidade da turma, matriculados, taxa de ocupação
- **Perguntas que responde:** quais turmas estão ociosas? Onde a ocupação parece baixa?
- **Prioridade:** MVP, condicionado à disponibilidade de capacidade por turma
- **Origem no BRD:** Derived from BRD v1.1 / Open question

### 7.9 Alertas e Ações Prioritárias
- **Objetivo:** transformar métricas em sinais gerenciais rápidos
- **Principais dados exibidos:** alertas de risco para resultado mensal, pressão de aluguel, pressão de folha, perda de alunos, pressão de margem, baixa ocupação e concentração de concessões
- **Perguntas que responde:** o que exige atenção imediata?
- **Prioridade:** MVP
- **Origem no BRD:** Derived from BRD v1.1

### 7.10 Visão de Inadimplência
- **Objetivo:** mostrar valores em aberto e seu impacto na visibilidade financeira
- **Principais dados exibidos:** saldos em aberto, taxa de inadimplência, alunos afetados
- **Perguntas que responde:** quanto da pressão financeira está sendo causada por mensalidades não pagas? Onde isso se concentra?
- **Prioridade:** Needs validation before prioritization
- **Origem no BRD:** Open question / Needs validation

---

## 8. Functional Requirements

### PR-01
- **Descrição:** o produto deve exibir um resumo financeiro mensal consolidado.
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1
- **Módulo relacionado:** Resumo Executivo

### PR-02
- **Descrição:** o produto deve mostrar a receita total recebida no mês.
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1
- **Módulo relacionado:** Resumo Executivo / Visão de Receitas

### PR-03
- **Descrição:** o produto deve mostrar a despesa total do mês.
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1
- **Módulo relacionado:** Resumo Executivo / Estrutura de Custos

### PR-04
- **Descrição:** o produto deve calcular e exibir o resultado operacional mensal.
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1
- **Módulo relacionado:** Resumo Executivo

### PR-05
- **Descrição:** o produto deve exibir as principais categorias de custo com destaque para aluguel e folha.
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1
- **Módulo relacionado:** Estrutura de Custos

### PR-06
- **Descrição:** o produto deve calcular o aluguel como proporção da receita.
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1
- **Módulo relacionado:** Estrutura de Custos

### PR-07
- **Descrição:** o produto deve calcular a folha como proporção da receita.
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1
- **Módulo relacionado:** Estrutura de Custos

### PR-08
- **Descrição:** o produto deve calcular o custo por aluno.
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1
- **Módulo relacionado:** Viabilidade e Sustentabilidade da Mensalidade

### PR-09
- **Descrição:** o produto deve exibir média de mensalidade e impacto dos descontos.
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1
- **Módulo relacionado:** Visão de Receitas / Viabilidade

### PR-10
- **Descrição:** o produto deve calcular a receita por aluno.
- **Prioridade:** MVP
- **Origem no BRD:** Derived from BRD v1.1
- **Módulo relacionado:** Viabilidade

### PR-11
- **Descrição:** o produto deve calcular a margem por aluno.
- **Prioridade:** MVP
- **Origem no BRD:** Derived from BRD v1.1
- **Módulo relacionado:** Viabilidade

### PR-12
- **Descrição:** o produto deve calcular e exibir o ponto de equilíbrio.
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1
- **Módulo relacionado:** Viabilidade

### PR-13
- **Descrição:** o produto deve mostrar a quantidade mínima de alunos necessária para operar sem prejuízo.
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1
- **Módulo relacionado:** Viabilidade

### PR-14
- **Descrição:** o produto deve mostrar o número de alunos ativos.
- **Prioridade:** MVP
- **Origem no BRD:** Derived from BRD v1.1
- **Módulo relacionado:** Resumo Executivo / Alunos e Retenção

### PR-15
- **Descrição:** o produto deve mostrar o número de novos alunos no período selecionado.
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1
- **Módulo relacionado:** Alunos e Retenção

### PR-16
- **Descrição:** o produto deve mostrar o total de rematrículas e a taxa de rematrícula.
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1
- **Módulo relacionado:** Alunos e Retenção

### PR-17
- **Descrição:** o produto deve mostrar as saídas de alunos e a taxa de perda de alunos.
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1
- **Módulo relacionado:** Alunos e Retenção

### PR-18
- **Descrição:** o produto deve permitir categorização de motivo de saída e exibir o detalhamento dos motivos de saída.
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1
- **Módulo relacionado:** Alunos e Retenção

### PR-19
- **Descrição:** o produto deve fornecer alertas visuais para condições críticas do negócio.
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1 / Derived
- **Módulo relacionado:** Alertas e Ações Prioritárias

### PR-20
- **Descrição:** o produto deve suportar filtro por período.
- **Prioridade:** MVP
- **Origem no BRD:** Derived from BRD v1.1
- **Módulo relacionado:** Filtros Gerais

### PR-21
- **Descrição:** o produto deve suportar filtro por segmento.
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1
- **Módulo relacionado:** Filtros Gerais

### PR-22
- **Descrição:** o produto deve suportar filtro por série/ano.
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1
- **Módulo relacionado:** Filtros Gerais

### PR-23
- **Descrição:** o produto deve suportar filtro por turma.
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1
- **Módulo relacionado:** Filtros Gerais

### PR-24
- **Descrição:** o produto deve suportar leitura por status do aluno.
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1
- **Módulo relacionado:** Filtros Gerais / Alunos e Retenção

### PR-25
- **Descrição:** o produto deve suportar leitura por status de rematrícula.
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1
- **Módulo relacionado:** Filtros Gerais / Alunos e Retenção

### PR-26
- **Descrição:** o produto deve suportar leitura por faixa de desconto.
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1
- **Módulo relacionado:** Filtros Gerais / Concessões

### PR-27
- **Descrição:** o produto deve exibir comparativos principais por segmento, série/ano e turma.
- **Prioridade:** MVP
- **Origem no BRD:** Derived from BRD v1.1
- **Módulo relacionado:** Desempenho por Recorte

### PR-28
- **Descrição:** o produto deve exibir a taxa de ocupação por turma, quando houver capacidade da turma validada.
- **Prioridade:** MVP
- **Origem no BRD:** Derived from BRD v1.1 / Open question
- **Módulo relacionado:** Ocupação por Turma

### PR-29
- **Descrição:** o produto deve distinguir funcionalmente desconto comercial de bolsa, quando houver política mínima e dados disponíveis.
- **Prioridade:** Needs validation before prioritization
- **Origem no BRD:** Directly stated in BRD v1.1 / Open question
- **Módulo relacionado:** Concessões

### PR-30
- **Descrição:** o produto deve exibir número total e percentual de bolsistas, quando houver dados válidos.
- **Prioridade:** Needs validation before prioritization
- **Origem no BRD:** Open question / Needs validation
- **Módulo relacionado:** Concessões / Bolsas

### PR-31
- **Descrição:** o produto deve exibir o valor total concedido em bolsas por período e por recorte, quando houver dados válidos.
- **Prioridade:** Needs validation before prioritization
- **Origem no BRD:** Open question / Needs validation
- **Módulo relacionado:** Concessões / Bolsas

### PR-32
- **Descrição:** o produto deve permitir cruzamento entre motivo de saída e segmento/série/turma.
- **Prioridade:** MVP
- **Origem no BRD:** Derived from BRD v1.1
- **Módulo relacionado:** Alunos e Retenção por Recorte

### PR-33
- **Descrição:** o produto deve exibir métricas de inadimplência se existirem dados confiáveis de inadimplência.
- **Prioridade:** Needs validation before prioritization
- **Origem no BRD:** Open question / Needs validation
- **Módulo relacionado:** Visão de Inadimplência

---

## 9. Analytical and KPI Requirements

### KPIs consolidados preservados

#### KPI-01 — Alunos Ativos
- **Definição:** total de alunos considerados ativos no período selecionado
- **Objetivo de negócio atendido:** base para sustentabilidade operacional e financeira
- **Fórmula / lógica esperada:** contagem de alunos com status ativo no período
- **Dados necessários:** status do aluno, lógica do período ativo
- **Prioridade:** MVP
- **Origem no BRD:** Derived from BRD v1.1

#### KPI-02 — Novos Alunos
- **Definição:** número de alunos que entraram no período selecionado
- **Objetivo de negócio atendido:** monitorar crescimento e entrada de alunos
- **Fórmula / lógica esperada:** contagem de entradas de novos alunos no período
- **Dados necessários:** data de entrada do aluno ou marcador de entrada
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1

#### KPI-03 — Total de Rematrículas
- **Definição:** número de alunos elegíveis que concluíram a rematrícula
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1

#### KPI-04 — Taxa de Rematrícula
- **Definição:** proporção de alunos elegíveis que se rematricularam
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1

#### KPI-05 — Total de Saídas de Alunos
- **Definição:** número de alunos que saíram no período selecionado
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1

#### KPI-06 — Taxa de Perda de Alunos
- **Definição:** proporção da base de alunos perdida no período selecionado
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1

#### KPI-07 — Receita Bruta
- **Definição:** receita total esperada de mensalidades antes de deduções
- **Prioridade:** MVP
- **Origem no BRD:** Derived from BRD v1.1

#### KPI-08 — Receita Recebida
- **Definição:** receita total efetivamente recebida no período selecionado
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1

#### KPI-09 — Despesas Totais
- **Definição:** despesas totais registradas no período selecionado
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1

#### KPI-10 — Resultado Mensal
- **Definição:** resultado operacional líquido do mês
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1

#### KPI-11 — Total de Aluguel
- **Definição:** despesa total com aluguel no período selecionado
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1

#### KPI-12 — Total de Folha
- **Definição:** despesa total relacionada à folha no período selecionado
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1

#### KPI-13 — Aluguel como % da Receita
- **Definição:** participação da receita consumida pelo aluguel
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1

#### KPI-14 — Folha como % da Receita
- **Definição:** participação da receita consumida pela folha
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1

#### KPI-15 — Mensalidade Média
- **Definição:** valor médio de mensalidade na base relevante de alunos ativos
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1

#### KPI-16 — Desconto Médio
- **Definição:** desconto médio concedido na base relevante de alunos ou cobranças
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1

#### KPI-17 — Custo por Aluno
- **Definição:** custo mensal médio alocado por aluno ativo
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1

#### KPI-18 — Receita por Aluno
- **Definição:** receita média recebida por aluno ativo
- **Prioridade:** MVP
- **Origem no BRD:** Derived from BRD v1.1

#### KPI-19 — Margem por Aluno
- **Definição:** diferença entre receita por aluno e custo por aluno
- **Prioridade:** MVP
- **Origem no BRD:** Derived from BRD v1.1

#### KPI-20 — Ponto de Equilíbrio
- **Definição:** limite mínimo de receita necessário para cobrir os custos
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1

#### KPI-21 — Alunos Mínimos para Operar
- **Definição:** quantidade mínima de alunos necessária para operar sem prejuízo mensal
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1

### KPIs segmentados novos ou revisados

#### KPI-22 — Alunos Ativos por Segmento
- **Definição:** total de alunos ativos por segmento de ensino
- **Objetivo de negócio atendido:** localizar distribuição da base por nível
- **Dados necessários:** segment, student_status
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1

#### KPI-23 — Alunos Ativos por Série/Ano
- **Definição:** total de alunos ativos por série/ano
- **Objetivo de negócio atendido:** localizar pontos de concentração ou fragilidade na jornada
- **Dados necessários:** grade_level, student_status
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1

#### KPI-24 — Alunos Ativos por Turma
- **Definição:** total de alunos ativos por turma
- **Objetivo de negócio atendido:** análise operacional e de ocupação
- **Dados necessários:** class_name, student_status
- **Prioridade:** MVP
- **Origem no BRD:** Directly stated in BRD v1.1

#### KPI-25 — Receita Recebida por Recorte
- **Definição:** receita recebida por segmento, série/ano e turma
- **Objetivo de negócio atendido:** localizar onde está a receita real
- **Dados necessários:** revenues + recortes acadêmicos
- **Prioridade:** MVP
- **Origem no BRD:** Derived from BRD v1.1

#### KPI-26 — Desconto Médio por Recorte
- **Definição:** desconto médio por segmento, série/ano e turma
- **Objetivo de negócio atendido:** localizar concentração de concessões
- **Dados necessários:** desconto + recortes acadêmicos
- **Prioridade:** MVP
- **Origem no BRD:** Derived from BRD v1.1

#### KPI-27 — Taxa de Rematrícula por Recorte
- **Definição:** taxa de rematrícula por segmento, série/ano e turma
- **Objetivo de negócio atendido:** identificar onde a retenção é mais fraca
- **Dados necessários:** rematrícula + recortes
- **Prioridade:** MVP
- **Origem no BRD:** Derived from BRD v1.1

#### KPI-28 — Taxa de Perda por Recorte
- **Definição:** taxa de perda por segmento, série/ano e turma
- **Objetivo de negócio atendido:** localizar evasão concentrada
- **Dados necessários:** saída + recortes
- **Prioridade:** MVP
- **Origem no BRD:** Derived from BRD v1.1

#### KPI-29 — Margem por Segmento
- **Definição:** aproximação de margem por segmento de ensino
- **Objetivo de negócio atendido:** localizar onde a margem parece mais pressionada
- **Dados necessários:** receitas e custos por segmento ou alocação compatível
- **Prioridade:** MVP
- **Origem no BRD:** Derived from BRD v1.1
- **Observações / riscos:** depende da lógica de alocação por recorte

#### KPI-30 — Taxa de Ocupação por Turma
- **Definição:** percentual de ocupação da turma com base em matriculados e capacidade
- **Objetivo de negócio atendido:** localizar ociosidade e eficiência
- **Dados necessários:** class_capacity, class_name, active students
- **Prioridade:** MVP
- **Origem no BRD:** Derived from BRD v1.1 / Open question

### KPIs de bolsas

#### KPI-31 — Total de Bolsistas
- **Definição:** número total de alunos bolsistas
- **Objetivo de negócio atendido:** dimensionar base subsidiada
- **Dados necessários:** scholarship_flag
- **Prioridade:** Needs validation before prioritization
- **Origem no BRD:** Open question / Needs validation

#### KPI-32 — Percentual de Bolsistas
- **Definição:** participação de bolsistas sobre a base relevante
- **Objetivo de negócio atendido:** medir peso da política de bolsas
- **Dados necessários:** scholarship_flag, active students
- **Prioridade:** Needs validation before prioritization
- **Origem no BRD:** Open question / Needs validation

#### KPI-33 — Valor Concedido em Bolsas
- **Definição:** soma do valor renunciado via bolsas
- **Objetivo de negócio atendido:** visibilidade sobre impacto financeiro das bolsas
- **Dados necessários:** scholarship_amount ou scholarship_percentage
- **Prioridade:** Needs validation before prioritization
- **Origem no BRD:** Open question / Needs validation

#### KPI-34 — Bolsistas por Recorte
- **Definição:** contagem e percentual de bolsistas por segmento, série/ano e turma
- **Objetivo de negócio atendido:** localizar concentração de bolsas
- **Dados necessários:** scholarship_flag + recortes
- **Prioridade:** Needs validation before prioritization
- **Origem no BRD:** Open question / Needs validation

### KPIs condicionais

#### KPI-35 — Valor de Inadimplência
- **Definição:** total de mensalidades em aberto no período
- **Prioridade:** Needs validation before prioritization
- **Origem no BRD:** Open question / Needs validation

#### KPI-36 — Taxa de Inadimplência
- **Definição:** proporção da receita esperada não recebida por inadimplência
- **Prioridade:** Needs validation before prioritization
- **Origem no BRD:** Open question / Needs validation

#### KPI-37 — Inadimplência por Recorte
- **Definição:** distribuição da inadimplência por segmento, série/ano ou turma
- **Prioridade:** Needs validation before prioritization
- **Origem no BRD:** Open question / Needs validation

---

## 10. Business Rules

### BR-01 — Definição de Aluno Ativo
- **Descrição:** um aluno deve ser classificado como ativo com base em um status definido e em participação válida no período selecionado.
- **Impacto no produto:** afeta contagem de alunos, custo por aluno, receita por aluno e cálculos de perda
- **Origem no BRD:** Derived from BRD v1.1
- **Status:** Needs validation

### BR-02 — Definição de Novo Aluno
- **Descrição:** um novo aluno é aquele cuja entrada ocorre no período de análise selecionado.
- **Impacto no produto:** afeta relatórios de entrada
- **Origem no BRD:** Derived from BRD v1.1
- **Status:** Derived

### BR-03 — Definição de Saída de Aluno
- **Descrição:** uma saída de aluno deve ser registrada com data de saída e motivo de saída.
- **Impacto no produto:** afeta taxa de perda e análise de motivo de saída
- **Origem no BRD:** Directly stated in BRD v1.1
- **Status:** Confirmed

### BR-04 — Elegibilidade para Rematrícula
- **Descrição:** somente alunos definidos como elegíveis para rematrícula devem compor o denominador da taxa de rematrícula.
- **Impacto no produto:** afeta a precisão da taxa de rematrícula
- **Origem no BRD:** Derived from BRD v1.1
- **Status:** Needs validation

### BR-05 — Lógica de Receita Recebida
- **Descrição:** receita recebida deve representar somente valores efetivamente recebidos no período selecionado.
- **Impacto no produto:** afeta resultado mensal, receita por aluno e controle financeiro
- **Origem no BRD:** Directly stated in BRD v1.1
- **Status:** Confirmed

### BR-06 — Lógica de Classificação de Despesas
- **Descrição:** todas as despesas devem pertencer a uma estrutura padronizada de categorias, incluindo aluguel e folha.
- **Impacto no produto:** afeta visibilidade de custos e proporções de custo
- **Origem no BRD:** Derived from BRD v1.1
- **Status:** Derived

### BR-07 — Regra de Segmentação Acadêmica
- **Descrição:** cada aluno deve poder ser associado a um segmento, uma série/ano e uma turma.
- **Impacto no produto:** afeta filtros, comparativos e KPIs por recorte
- **Origem no BRD:** Directly stated in BRD v1.1
- **Status:** Needs validation

### BR-08 — Regra de Ocupação por Turma
- **Descrição:** a taxa de ocupação depende de capacidade da turma validada e de contagem confiável de alunos ativos na turma.
- **Impacto no produto:** afeta módulo de ocupação e análises de eficiência
- **Origem no BRD:** Derived from BRD v1.1 / Open question
- **Status:** Needs validation

### BR-09 — Regra de Desconto
- **Descrição:** descontos devem ser representados de forma consistente e rastreável para permitir visibilidade de impacto.
- **Impacto no produto:** afeta análise de mensalidade, receita efetiva e apoio à decisão
- **Origem no BRD:** Directly stated in BRD v1.1
- **Status:** Confirmed

### BR-10 — Regra de Bolsa vs Desconto
- **Descrição:** bolsa deve ser tratada como categoria funcional distinta de desconto comercial, quando houver política e dados mínimos definidos.
- **Impacto no produto:** afeta leitura de concessões e receita efetiva
- **Orig efetiva
- **Origem no BRD:** Directly stated in BRD v1.1
- **Status:** Needs validation

### BR-11 — Regra de Classificação de Motivos de Saída
- **Descrição:** os motivos de saída devem seguir estrutura controlada e gerenciável.
- **Impacto no produto:** afeta análise por recorte e qualidade da resposta gerencial
- **Origem no BRD:** Directly stated in BRD v1.1
- **Status:** Needs validation

### BR-12 — Regra de Situação Financeira
- **Descrição:** a classificação da situação financeira depende de critério definido pela escola e da granularidade desejada.
- **Impacto no produto:** afeta filtros, risco financeiro e futuras análises de inadimplência
- **Origem no BRD:** Open question / Needs validation
- **Status:** Needs validation

### BR-13 — Regra de Inadimplência
- **Descrição:** indicadores de inadimplência só podem ser calculados se saldos em aberto e receita esperada estiverem estruturados.
- **Impacto no produto:** afeta a viabilidade do módulo de inadimplência
- **Origem no BRD:** Open question / Needs validation
- **Status:** Needs validation

---

## 11. Data Requirements

### 11.1 Alunos
- **Campos mínimos esperados:**
  - `student_id`
  - `student_name`
  - `segment`
  - `grade_level`
  - `class_name`
  - `student_status`
  - `entry_date`
  - `exit_date`
  - `exit_reason`
  - `tuition_amount`
  - `discount_amount`
  - `discount_percentage`
  - `discount_band`
  - `scholarship_flag`
  - `scholarship_type`
  - `scholarship_amount`
  - `scholarship_percentage`
  - `financial_status`
- **Por que são necessários:** necessários para contagem de alunos, segmentação, entradas, saídas, análise de mensalidade, concessões, risco e métricas por aluno
- **Módulos que dependem deles:** Resumo Executivo, Alunos e Retenção, Visão de Receitas, Viabilidade, Concessões, Ocupação
- **Status:** Confirmed / Derived / Needs validation conforme cada campo

### 11.2 Receitas
- **Campos mínimos esperados:**
  - `revenue_id`
  - `student_id`
  - `reference_period`
  - `expected_amount`
  - `discount_amount`
  - `received_amount`
  - `payment_date`
  - `payment_status`
- **Por que são necessários:** necessários para distinguir receita esperada de receita recebida e apoiar cálculos de resultado e concessões
- **Módulos que dependem deles:** Resumo Executivo, Visão de Receitas, Viabilidade, Concessões
- **Status:** Confirmed / Derived

### 11.3 Despesas
- **Campos mínimos esperados:**
  - `expense_id`
  - `reference_period`
  - `category`
  - `subcategory`
  - `amount`
  - `expense_type`
  - `notes`
- **Por que são necessários:** necessários para totais mensais de custo e análise da estrutura de custos
- **Módulos que dependem deles:** Resumo Executivo, Estrutura de Custos, Viabilidade
- **Status:** Confirmed / Derived

### 11.4 Rematrículas
- **Campos mínimos esperados:**
  - `rematriculation_id`
  - `student_id`
  - `academic_year`
  - `eligible_flag`
  - `rematriculated_flag`
  - `confirmation_date`
  - `rematriculation_status`
- **Por que são necessários:** necessários para cálculo de volume e taxa de rematrícula por recorte
- **Módulos que dependem deles:** Alunos e Retenção
- **Status:** Confirmed / Needs validation

### 11.5 Ocupação / Turmas
- **Campos mínimos esperados:**
  - `class_name`
  - `class_capacity`
  - `segment`
  - `grade_level`
- **Por que são necessários:** necessários para taxa de ocupação e comparativos por turma
- **Módulos que dependem deles:** Ocupação por Turma, Filtros Gerais
- **Status:** Needs validation

### 11.6 Inadimplência
- **Campos mínimos esperados:**
  - `delinquency_id`
  - `student_id`
  - `reference_period`
  - `open_amount`
  - `due_date`
  - `delinquency_status`
- **Por que são necessários:** necessários apenas se a inadimplência entrar no MVP ou em versões futuras
- **Módulos que dependem deles:** Inadimplência, Receitas
- **Status:** Needs validation

### 11.7 Categorias de Custo
- **Campos mínimos esperados:**
  - `category_name`
  - `category_group`
  - `critical_cost_flag`
- **Por que são necessários:** necessários para padronizar aluguel, folha e outros grupos críticos de custo
- **Módulos que dependem deles:** Estrutura de Custos, Alertas
- **Status:** Derived

### 11.8 Referência Temporal
- **Campos mínimos esperados:**
  - `year`
  - `month`
  - `reporting_period`
- **Por que são necessários:** necessários para toda análise recorrente mensal
- **Módulos que dependem deles:** Filtros Gerais, todos os módulos analíticos
- **Status:** Derived

---

## 12. UX and Adoption Requirements

### UX-01 — O dashboard deve continuar simples para usuários com baixa maturidade digital
- **Motivo:** o BRD identifica risco de adoção e resistência à complexidade
- **Relação com o BRD:** Directly stated in BRD v1.1

### UX-02 — A nova segmentação deve ser acessada por filtros simples e previsíveis
- **Motivo:** profundidade analítica não pode virar barreira de uso
- **Relação com o BRD:** Derived from BRD v1.1

### UX-03 — O produto deve priorizar leitura visual rápida
- **Motivo:** a liderança precisa de interpretação rápida, não de atrito operacional
- **Relação com o BRD:** Directly stated in BRD v1.1

### UX-04 — O produto deve minimizar profundidade de cliques e complexidade de navegação
- **Motivo:** reduz atrito de adoção e favorece uso recorrente
- **Relação com o BRD:** Derived from BRD v1.1

### UX-05 — O produto deve usar linguagem de negócio compreensível
- **Motivo:** garante acessibilidade para usuários não técnicos
- **Relação com o BRD:** Directly stated in BRD v1.1

### UX-06 — O produto deve destacar visualmente métricas e alertas críticos
- **Motivo:** o valor gerencial depende de identificação rápida de prioridades
- **Relação com o BRD:** Derived from BRD v1.1

### UX-07 — O produto deve organizar a profundidade analítica em camadas
- **Motivo:** preservar simplicidade no topo e detalhamento sob demanda
- **Relação com o BRD:** Derived from BRD v1.1

### UX-08 — As interações de entrada/manutenção de dados devem permanecer separadas da leitura gerencial
- **Motivo:** diferentes perfis de usuário têm necessidades diferentes
- **Relação com o BRD:** Derived from BRD v1.1

---

## 13. Non-Functional Requirements

### NFR-01 — Simplicidade de Usabilidade
- **Descrição:** o produto deve ser fácil de entender e usar por usuários não técnicos.
- **Prioridade:** MVP
- **Origem:** Directly stated in BRD v1.1

### NFR-02 — Confiabilidade das Métricas Exibidas
- **Descrição:** o produto deve exibir métricas baseadas em regras consistentes e estruturadas.
- **Prioridade:** MVP
- **Origem:** Derived from BRD v1.1

### NFR-03 — Legibilidade
- **Descrição:** o dashboard deve permitir interpretação rápida por meio de layout claro e destaque visual das métricas.
- **Prioridade:** MVP
- **Origem:** Derived from BRD v1.1

### NFR-04 — Desempenho com filtros
- **Descrição:** o dashboard deve manter boa experiência de uso mesmo com filtros por segmento, série e turma.
- **Prioridade:** MVP
- **Origem:** Derived from BRD v1.1

### NFR-05 — Baixa Complexidade Operacional
- **Descrição:** a primeira versão deve evitar carga operacional desnecessária.
- **Prioridade:** MVP
- **Origem:** Directly stated in BRD v1.1 / Derived

### NFR-06 — Lógica de Métricas Manutenível
- **Descrição:** definições de KPI e regras de cálculo devem ser explícitas e reutilizáveis.
- **Prioridade:** MVP
- **Origem:** Derived from BRD v1.1

### NFR-07 — Auditabilidade Mínima dos Dados
- **Descrição:** os principais números do negócio devem ser rastreáveis até registros estruturados.
- **Prioridade:** MVP
- **Origem:** Derived from BRD v1.1

### NFR-08 — Preparação Controlada para Expansão
- **Descrição:** o produto deve ser estruturado de forma que permita expansão futura sem redesenhar o propósito central.
- **Prioridade:** Post-MVP / Future Release
- **Origem:** Derived from BRD v1.1

### NFR-09 — Modelo técnico de implantação
- **Descrição:** ainda não está suficientemente definido no BRD.
- **Prioridade:** Needs validation before prioritization
- **Origem:** Open question / Needs validation

---

## 14. MVP Definition

### Objetivos do MVP v1.1
- dar à liderança uma visão consolidada e confiável do desempenho financeiro da escola
- tornar visível a estrutura de custos, especialmente aluguel e folha
- mostrar se a mensalidade parece sustentável na escala atual de operação
- oferecer visibilidade objetiva sobre retenção e perda de alunos
- localizar onde a pressão está concentrada por segmento, série/ano e turma
- apoiar decisões mais disciplinadas sobre desconto e sustentabilidade
- substituir a visibilidade gerencial fragmentada por uma base mínima de gestão segmentada

### Componentes obrigatórios do MVP v1.1
- filtros gerais por período, segmento, série/ano e turma
- módulo de Resumo Executivo
- módulo de Alunos e Retenção
- módulo de Visão de Receitas
- módulo de Estrutura de Custos
- módulo de Viabilidade e Sustentabilidade da Mensalidade
- módulo de Concessões (mínimo para descontos; bolsas condicionais)
- módulo de Ocupação por Turma, se capacidade por turma estiver disponível
- módulo de Alertas e Ações Prioritárias

### KPIs mínimos do MVP v1.1
- alunos ativos
- novos alunos
- total de rematrículas
- taxa de rematrícula
- total de saídas de alunos
- taxa de perda de alunos
- receita recebida
- despesas totais
- resultado mensal
- total de aluguel
- total de folha
- aluguel como % da receita
- folha como % da receita
- mensalidade média
- desconto médio
- custo por aluno
- receita por aluno
- margem por aluno
- ponto de equilíbrio
- alunos mínimos para operar
- alunos ativos por segmento
- alunos ativos por série/ano
- alunos ativos por turma
- receita por recorte
- desconto médio por recorte
- taxa de rematrícula por recorte
- taxa de perda por recorte
- taxa de ocupação por turma, se houver capacidade validada

### Itens do MVP que dependem de validação
- leitura de bolsas
- taxa de ocupação por turma, se não houver capacidade por turma
- leitura por situação financeira
- inadimplência segmentada

### Limite de sucesso do MVP
A versão 1.1 será suficientemente útil se a liderança conseguir:
1. entender o resultado financeiro mensal;
2. entender as principais pressões de custo;
3. avaliar a sustentabilidade da mensalidade em nível básico;
4. identificar se a perda de alunos está se tornando crítica;
5. identificar em quais segmentos, séries ou turmas a pressão está mais concentrada;
6. usar o produto em uma rotina recorrente de gestão.

---

## 15. Acceptance Criteria

### AC-01
O dashboard deve exibir uma visão mensal consolidada de receita recebida, despesas totais e resultado mensal.

### AC-02
O dashboard deve exibir totais de aluguel e folha, bem como suas proporções em relação à receita.

### AC-03
O dashboard deve exibir número de alunos ativos, novos alunos, saídas de alunos, total de rematrículas e taxa de rematrícula.

### AC-04
O dashboard deve exibir custo por aluno e receita por aluno.

### AC-05
O dashboard deve exibir ponto de equilíbrio e número mínimo de alunos para operar sem prejuízo, com base em lógica de negócio aprovada.

### AC-06
O dashboard deve permitir que os usuários identifiquem motivos de saída por meio de um detalhamento visível.

### AC-07
O dashboard deve incluir alertas visuais para pelo menos os riscos gerenciais mais críticos definidos no MVP.

### AC-08
O produto deve permitir filtro por segmento, série/ano e turma.

### AC-09
O produto deve exibir comparativos principais por recorte acadêmico nos indicadores definidos como MVP.

### AC-10
O produto deve exibir taxa de ocupação por turma se a capacidade por turma estiver disponível e validada.

### AC-11
Se houver dados mínimos e política válida, o produto deve diferenciar bolsa de desconto nas leituras de concessão.

### AC-12
O produto deve continuar compreensível para usuários não técnicos após revisão inicial com a liderança.

### AC-13
Todos os KPIs do MVP devem ter lógica explicitamente documentada.

### AC-14
Questões em aberto que afetem a precisão dos KPIs devem estar explicitamente documentadas antes do início da implementação técnica.

---

## 16. Dependencies and Risks

### D-01 — Registros estruturados de alunos
- **Impacto:** Alto
- **Mitigação:** criar padrão mínimo de base de alunos antes da implementação
- **Relação com o BRD:** falta de base estruturada de dados

### D-02 — Registros estruturados de receitas
- **Impacto:** Alto
- **Mitigação:** padronizar campos de receita esperada versus recebida
- **Relação com o BRD:** o controle financeiro atual é frágil

### D-03 — Categorização estruturada de despesas
- **Impacto:** Alto
- **Mitigação:** definir categorias padronizadas de custo antes da implementação dos KPIs
- **Relação com o BRD:** necessidade de visualizar custos e seus direcionadores

### D-04 — Cadastro confiável de segmento, série e turma
- **Impacto:** Alto
- **Mitigação:** validar taxonomia e obrigatoriedade desses campos no cadastro
- **Relação com o BRD:** segmentação é requisito central da v1.1

### D-05 — Regras de elegibilidade para rematrícula
- **Impacto:** Médio
- **Mitigação:** validar regras de elegibilidade e confirmação com a liderança
- **Relação com o BRD:** rematrícula é KPI central

### D-06 — Padronização de motivos de saída
- **Impacto:** Médio
- **Mitigação:** definir taxonomia controlada de motivos de saída
- **Relação com o BRD:** necessário para análise por recorte

### D-07 — Registro da capacidade por turma
- **Impacto:** Médio/Alto
- **Mitigação:** validar se há capacidade instalada por turma e como será mantida
- **Relação com o BRD:** requisito para ocupação por turma

### D-08 — Diferenciação entre bolsa e desconto
- **Impacto:** Alto
- **Mitigação:** validar política, nomenclatura e estrutura mínima antes de priorizar bolsas no MVP
- **Relação com o BRD:** requisito novo e crítico

### D-09 — Resistência cultural às rotinas digitais
- **Impacto:** Alto
- **Mitigação:** manter o MVP simples, priorizar usabilidade, limitar sobrecarga de funcionalidades
- **Relação com o BRD:** baixa maturidade digital e risco de adoção

### D-10 — Baixa qualidade inicial dos dados
- **Impacto:** Alto
- **Mitigação:** tratar limpeza e validação inicial dos dados como parte da implementação
- **Relação com o BRD:** controles manuais e falta de estrutura

### D-11 — Interpretação incorreta dos indicadores
- **Impacto:** Médio
- **Mitigação:** incluir definições de métricas e possivelmente notas explicativas
- **Relação com o BRD:** confiança da liderança é essencial

### D-12 — Disponibilidade de dados de inadimplência
- **Impacto:** Médio
- **Mitigação:** manter inadimplência fora do MVP, salvo validação de dados
- **Relação com o BRD:** lacuna explícita de validação

### D-13 — Ambiguidade na fórmula de ponto de equilíbrio
- **Impacto:** Alto
- **Mitigação:** validar premissas de mensalidade e custo antes da implementação final
- **Relação com o BRD:** ponto de equilíbrio é saída obrigatória

---

## 17. Open Questions / Items to Validate

### Alta criticidade
1. Qual é a definição aprovada de aluno ativo?
2. Qual é a fórmula aprovada para ponto de equilíbrio e alunos mínimos para operar?
3. Qual é a estrutura real disponível de receitas e despesas?
4. Existe cadastro confiável de segmento, série/ano e turma por aluno?
5. Existe capacidade máxima definida por turma?
6. Existe política formal de bolsa distinta de desconto?
7. Bolsa deve ser medida em valor, percentual ou ambos?
8. Quem será o responsável pela governança dos dados e pela alimentação correta das novas dimensões?

### Média criticidade
9. Qual é a classificação padrão dos motivos de saída?
10. Qual é a representação padrão de descontos: valor, percentual ou ambos?
11. A mensalidade média deve ser analisada em valor bruto, líquido ou ambos?
12. Qual taxonomia será usada para status do aluno e status de rematrícula?
13. Como a escola deseja registrar situação financeira?
14. Quais limites devem disparar alertas por recorte?

### Baixa criticidade
15. Versões futuras devem incluir comparações históricas mais profundas por recorte?
16. O módulo de bolsas deve entrar no MVP ou ficar logo após a estabilização do cadastro?
17. A inadimplência segmentada deve ser tratada como módulo posterior?
18. O produto deve evoluir para análises mais sofisticadas de eficiência por turma?

---

## 18. Traceability Matrix

| Business Pain / Need | Strategic Objective | Product Module | KPI / Functional Requirement | Priority | BRD Source Type |
|---|---|---|---|---|---|
| Falta de controle financeiro confiável | Estabelecer controle financeiro mensal confiável | Resumo Executivo | Resultado Mensal / PR-01 / PR-04 | MVP | Directly stated in BRD v1.1 |
| Pressão de custo com aluguel | Dar visibilidade à estrutura de custos | Estrutura de Custos | Total de Aluguel / PR-05 / PR-06 | MVP | Directly stated in BRD v1.1 |
| Necessidade de entender impacto da folha | Dar visibilidade à estrutura de custos | Estrutura de Custos | Total de Folha / PR-07 | MVP | Directly stated in BRD v1.1 |
| Sustentabilidade pouco clara da mensalidade | Avaliar sustentabilidade da mensalidade | Viabilidade | Custo por Aluno / Receita por Aluno / Margem por Aluno | MVP | Direct + Derived |
| Pressão por descontos | Criar base objetiva para decisões sobre desconto | Receitas / Concessões | Desconto Médio / PR-09 / PR-26 | MVP | Directly stated in BRD v1.1 |
| Risco de evasão | Monitorar retenção e perda de alunos | Alunos e Retenção | Taxa de Perda / PR-17 / PR-18 | MVP | Directly stated in BRD v1.1 |
| Necessidade de visibilidade sobre rematrícula | Monitorar retenção e rematrícula | Alunos e Retenção | Taxa de Rematrícula / PR-16 / PR-25 | MVP | Directly stated in BRD v1.1 |
| Falta de visibilidade por recorte | Obter visibilidade segmentada da operação | Filtros Gerais / Desempenho por Recorte | PR-21 / PR-22 / PR-23 / PR-27 | MVP | Directly stated in BRD v1.1 |
| Baixa ocupação não visível | Melhorar eficiência operacional | Ocupação por Turma | KPI-30 / PR-28 | MVP / Needs validation | Derived from BRD v1.1 |
| Falta de clareza sobre bolsas | Dar transparência ao impacto das concessões | Concessões / Bolsas | KPI-31 a KPI-34 / PR-29 / PR-30 / PR-31 | Needs validation | Open question / Needs validation |
| Inadimplência potencialmente relevante | Melhorar leitura da pressão financeira | Inadimplência | KPI-35 a KPI-37 / PR-33 | Needs validation | Open question / Needs validation |

---

## 19. SDD Readiness Notes

### Suficientemente definido para avançar ao SDD
- propósito central do produto
- principais grupos de usuários
- módulos do MVP v1.1
- filtros e recortes principais
- lista principal de KPIs do MVP
- principais riscos e restrições de adoção
- necessidade explícita de segmentação por segmento, série/ano e turma
- necessidade de manter simplicidade, mesmo com maior profundidade analítica

### Ainda depende de validação
- lógica exata de aluno ativo
- lógica exata de elegibilidade para rematrícula
- lógica exata de cálculo do ponto de equilíbrio
- disponibilidade e qualidade real dos registros de receita e despesa
- cadastro confiável de segmento, série e turma
- capacidade por turma
- padronização de desconto vs bolsa
- existência e estrutura real de bolsas
- situação financeira e inadimplência segmentada
- thresholds de alertas por recorte

### Decisões técnicas provavelmente impactadas pelas lacunas abertas
- modelo de dados para entidades acadêmicas e gerenciais
- lógica de cálculo por recorte
- tratamento de bolsas no modelo analítico
- inclusão ou não de ocupação no MVP
- inclusão ou não de inadimplência no MVP
- desenho final dos filtros e da granularidade de visualização

---

## 20. Recommended Next Step

O próximo passo recomendado é usar este **PRD v1.1** como base para atualizar o **SDD v1.1**, preservando a lógica de revisão controlada.

A sequência ideal é:

1. validar com a liderança os pontos críticos em aberto:
   - aluno ativo
   - rematrícula elegível
   - segmentação acadêmica real
   - capacidade por turma
   - política de bolsas
   - granularidade de situação financeira

2. confirmar os limites do MVP v1.1:
   - quais leituras segmentadas entram na primeira versão
   - se bolsas entram já no MVP ou logo após estabilização cadastral
   - se ocupação entra no MVP com base em capacidade validada

3. atualizar o SDD v1.1:
   - refletindo o novo modelo de dados
   - refletindo os filtros segmentados
   - refletindo a separação entre desconto e bolsa
   - refletindo a estratégia de implementação local-first
```
