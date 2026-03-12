# Technical Backlog / Implementation Plan — @CESOL School Financial and Administrative Dashboard

## 1. Implementation Overview

Este plano traduz o BRD v1.1, o PRD v1.1 e o SDD v1.1 em uma sequência técnica executável para construir o dashboard administrativo e financeiro da @CESOL com foco em controle financeiro, retenção/evasão, sustentabilidade da mensalidade, impacto de descontos e leitura segmentada por segmento, série/ano e turma.

A organização do backlog segue três eixos:

- fases técnicas reais de construção
- módulos/KPIs do produto
- pontos críticos de validação que afetam a confiabilidade dos indicadores

A filosofia de entrega adotada é:

- validar primeiro o que pode distorcer KPI
- estabilizar a base local
- construir a camada analítica mínima confiável
- entregar o dashboard MVP em camadas
- só então incorporar itens condicionais e preparação para nuvem

Isso mantém aderência à estratégia local-first, evita overengineering e reduz retrabalho causado por taxonomias ou fórmulas mal definidas.

O backlog abaixo foi montado para permitir início de execução sem reinterpretar BRD/PRD/SDD do zero. Onde a documentação aponta ambiguidade, o item foi marcado como **Needs validation** em vez de virar implementação assumida.

---

## 2. Planning Assumptions

- **Confirmed** — O MVP deve ser **local-first** e **cloud-later**, com PostgreSQL local como fonte de verdade e sem API dedicada no MVP.
- **Confirmed** — A stack-base do MVP é Python, PostgreSQL local, SQLAlchemy, Alembic, Pandas, Streamlit, Plotly e configuração por `.env` / pydantic-settings.
- **Confirmed** — A solução precisa manter simplicidade de uso para usuários com baixa maturidade digital, com leitura em camadas e poucos filtros visíveis por vez.
- **Confirmed** — As entidades centrais do MVP são alunos, receitas, despesas, rematrículas, turmas/capacidade, categorias de custo e lotes de importação; inadimplência é condicional.
- **Confirmed** — O MVP funcional precisa cobrir visão financeira consolidada, custos, viabilidade da mensalidade, retenção/rematrícula, filtros segmentados, comparativos por recorte, alertas e motivo de saída por recorte.
- **Confirmed** — Ocupação por turma entra apenas se houver capacidade por turma validada.
- **Confirmed** — Bolsas devem ser separadas de desconto no modelo, mas a análise de bolsas depende de política mínima e dados válidos.
- **Confirmed** — Inadimplência segmentada é item condicional / pós-MVP.
- **Derived** — A ordem de implementação mais segura é: validação de regras e taxonomias → schema → ingestão → KPIs → dashboard → condicionais → estabilização local → cloud readiness.
- **Derived** — A camada analítica deve centralizar fórmulas e não a UI, para preservar rastreabilidade e manutenção.
- **Needs validation** — Definição final de aluno ativo.
- **Needs validation** — Fórmula final de ponto de equilíbrio.
- **Needs validation** — Fórmula final de alunos mínimos para operar.
- **Needs validation** — Cadastro confiável de segmento, série/ano e turma, inclusive abrangência real do Fundamental II.
- **Needs validation** — Política formal de bolsa distinta de desconto e sua representação em valor/percentual/ambos.
- **Needs validation** — Granularidade de situação financeira e existência de dados confiáveis de inadimplência.

---

## 3. Implementation Strategy

A ordem proposta faz sentido porque os principais riscos do projeto não estão na visualização, mas na confiabilidade do dado e nas ambiguidades de regra de negócio. Os documentos tratam como críticos:

- cadastro estruturado de alunos
- padronização de receitas e despesas
- taxonomia de segmentação
- diferenciação bolsa vs desconto
- capacidade por turma
- fórmulas de aluno ativo e ponto de equilíbrio

Construir dashboard antes disso aumentaria retrabalho e risco de KPI incorreto.

A estratégia local-first foi preservada porque a documentação recomenda validar adoção, schema, taxonomias e KPIs localmente antes de migrar. A decisão técnica explícita é PostgreSQL local + Streamlit direto, sem API dedicada no MVP, para maximizar velocidade com o menor número de componentes.

O plano reduz risco e retrabalho por quatro mecanismos:

1. explicita uma fase de validação antes do build pesado
2. separa itens MVP de condicionais
3. trata taxonomia e qualidade de dados como parte da implementação
4. mantém as regras de KPI documentadas e fora da interface

---

## 4. Delivery Phases

### Phase 0 — Validation and project alignment

- **Objetivo:** fechar as definições que afetam schema, taxonomias e fórmulas de KPI.
- **Escopo:** aluno ativo, elegibilidade de rematrícula, ponto de equilíbrio, alunos mínimos, taxonomias de segmento/série/turma/status/motivo de saída/faixa de desconto, política de bolsa, capacidade por turma, granularidade da situação financeira, responsável por governança de dados.
- **Entregáveis:** documento de decisões validadas; taxonomias aprovadas; lista explícita de lacunas remanescentes; critérios para o que entra ou não no MVP.
- **Dependências:** nenhuma.
- **Riscos:** iniciar modelagem com regras ambíguas; abrir frentes condicionais sem base.
- **Classificação geral:** **Validation**

### Phase 1 — Project bootstrap

- **Objetivo:** estruturar o projeto base e o ambiente local.
- **Escopo:** estrutura de diretórios, ambiente virtual, configuração inicial, `.env`, convenções mínimas, documentação base.
- **Entregáveis:** repositório organizado; settings; documentação de setup; base inicial do app.
- **Dependências:** decisões mínimas da Phase 0.
- **Riscos:** convenções insuficientes e configuração inconsistente.
- **Classificação geral:** **MVP**

### Phase 2 — Database and schema foundation

- **Objetivo:** implantar o banco local e o schema revisado para o MVP v1.1.
- **Escopo:** models, migrations, tabelas principais, domínios/tabelas de taxonomia recomendadas, `import_batches`, campos de segmentação e concessões.
- **Entregáveis:** PostgreSQL local configurado; ORM; Alembic; schema operacional inicial.
- **Dependências:** Phase 0 concluída para evitar modelagem sobre taxonomias indefinidas.
- **Riscos:** ambiguidade de regra de negócio e mudanças frequentes de schema.
- **Classificação geral:** **MVP**

### Phase 3 — Taxonomy and data standardization

- **Objetivo:** padronizar conceitos e preparar templates de dados confiáveis.
- **Escopo:** domínios de segmento, série/ano, turma, status do aluno, status de rematrícula, faixas de desconto, motivos de saída; padrões para receitas e despesas; decisão formal sobre desconto vs bolsa.
- **Entregáveis:** taxonomias implementadas; regras de validação; templates CSV/Excel revisados; dicionário mínimo de dados.
- **Dependências:** schema estável.
- **Riscos:** baixa qualidade dos dados históricos e resistência à obrigatoriedade de campos.
- **Classificação geral:** **MVP**

### Phase 4 — Data ingestion and operational input

- **Objetivo:** permitir entrada manual simplificada e importação estruturada já com recortes.
- **Escopo:** páginas internas de entrada/atualização, importação de CSV/Excel, validação inicial, rejeição de registros inválidos, logs de importação.
- **Entregáveis:** fluxo operacional de carga; templates; validação de lotes; primeira carga histórica.
- **Dependências:** taxonomias mínimas definidas.
- **Riscos:** baixa adesão operacional; importações com inconsistência.
- **Classificação geral:** **MVP**

### Phase 5 — KPI and analytics layer

- **Objetivo:** implementar lógica analítica consolidada e segmentada.
- **Escopo:** KPIs financeiros, retenção, viabilidade, descontos, comparativos por recorte, cruzamento de motivo de saída; fórmulas documentadas fora da UI.
- **Entregáveis:** serviços analíticos, consultas/views, catálogo de KPIs, datasets consumíveis pelo dashboard.
- **Dependências:** dados minimamente estruturados.
- **Riscos:** divergência em fórmulas críticas; comparação por recorte sobre base incompleta.
- **Classificação geral:** **MVP**

### Phase 6 — Dashboard MVP

- **Objetivo:** entregar o dashboard funcional do MVP.
- **Escopo:** filtros gerais, resumo executivo, alunos e retenção, receitas, custos, viabilidade, descontos, alertas, leitura em camadas, comparativos por segmento/série/turma.
- **Entregáveis:** app Streamlit funcional; cards, gráficos, tabelas e alertas; navegação simples; leitura comparativa mínima.
- **Dependências:** KPI layer funcional.
- **Riscos:** excesso de escopo na interface; carga cognitiva excessiva.
- **Classificação geral:** **MVP**

### Phase 7 — Conditional modules and refinements

- **Objetivo:** incorporar componentes dependentes de validação.
- **Escopo:** ocupação por turma, diferenciação analítica de bolsa, KPIs de bolsa, eventual situação financeira/inadimplência.
- **Entregáveis:** módulos condicionais ativados apenas se dados e política existirem.
- **Dependências:** Phase 0 fechada para o tópico correspondente; dados disponíveis.
- **Riscos:** priorização inadequada de módulos ainda sem base confiável.
- **Classificação geral:** **Needs validation / Future**

### Phase 8 — Stabilization and local validation

- **Objetivo:** consolidar o MVP local, reduzir retrabalho e preparar rotina de uso.
- **Escopo:** revisão de consistência, UAT com liderança, refinamentos de UX, logs, jobs simples, documentação operacional.
- **Entregáveis:** MVP estabilizado; problemas conhecidos documentados; rotina local sustentável.
- **Dependências:** dashboard MVP entregue.
- **Riscos:** automatizar cedo demais processos ainda instáveis.
- **Classificação geral:** **MVP (hardening)**

### Phase 9 — Cloud readiness / future evolution

- **Objetivo:** preparar migração segura para nuvem depois da validação local.
- **Escopo:** adaptação de ambiente, migração para banco gerenciado, revisão de acesso, possível Supabase, eventual avaliação futura de API.
- **Entregáveis:** plano de migração; variáveis adaptáveis; validação em cloud.
- **Dependências:** sucesso local comprovado.
- **Riscos:** migrar antes de estabilizar schema e KPI.
- **Classificação geral:** **Future**

---

## 5. Epic Breakdown

### EP-01 — Validation and business rules alignment

- **Objetivo:** fechar regras e taxonomias que afetam precisão do produto.
- **Relação com PRD/SDD:** open questions, dependencies and risks, SDD readiness.
- **Prioridade:** Highest / MVP-enabler.
- **Dependências:** nenhuma.
- **Definição de pronto:** taxonomias e fórmulas críticas aprovadas; condicionais explicitamente separados.

### EP-02 — Local platform bootstrap and schema

- **Objetivo:** estruturar ambiente local, banco, migrations e modelo de dados base.
- **Relação com PRD/SDD:** stack recomendada, database layer, logical data model, implementation phases 0-1.
- **Prioridade:** MVP.
- **Dependências:** EP-01 mínimo concluído.
- **Definição de pronto:** app sobe localmente; banco local acessível; schema versionado criado.

### EP-03 — Taxonomy, validation and ingestion foundation

- **Objetivo:** garantir consistência dos dados antes dos KPIs.
- **Relação com PRD/SDD:** data requirements, taxonomy and validation layer, ingestion layer, dependencies.
- **Prioridade:** MVP.
- **Dependências:** EP-02.
- **Definição de pronto:** templates, validadores e primeira carga funcionando com rejeição rastreável de inconsistências.

### EP-04 — Core financial analytics

- **Objetivo:** entregar KPIs consolidados financeiros e de custos.
- **Relação com PRD/SDD:** requisitos funcionais financeiros e analytics layer.
- **Prioridade:** MVP.
- **Dependências:** EP-03.
- **Definição de pronto:** receita, despesa, resultado, aluguel, folha, custo por aluno, receita por aluno, margem, ponto de equilíbrio e alunos mínimos calculados e documentados.

### EP-05 — Retention and segmented analytics

- **Objetivo:** entregar KPIs de alunos, rematrícula, perda e comparativos por recorte.
- **Relação com PRD/SDD:** requisitos funcionais de retenção e segmentação.
- **Prioridade:** MVP.
- **Dependências:** EP-03.
- **Definição de pronto:** indicadores de retenção e cruzamentos por segmento/série/turma operando sobre taxonomias válidas.

### EP-06 — Dashboard MVP and UX

- **Objetivo:** materializar o MVP em Streamlit com leitura simples em camadas.
- **Relação com PRD/SDD:** core product modules, acceptance criteria, frontend design approach.
- **Prioridade:** MVP.
- **Dependências:** EP-04 e EP-05.
- **Definição de pronto:** dashboard navegável, filtros globais, módulos MVP, alertas e revisão inicial de compreensibilidade com liderança.

### EP-07 — Conditional concessions, occupancy and delinquency

- **Objetivo:** incorporar os módulos dependentes de validação sem contaminar o core do MVP.
- **Relação com PRD/SDD:** requisitos condicionais e phase 6 conditional features.
- **Prioridade:** Needs validation / Future.
- **Dependências:** EP-01 e EP-03, além de dados mínimos.
- **Definição de pronto:** módulos habilitados apenas com política e dados aprovados.

### EP-08 — Stabilization, automation and local operations

- **Objetivo:** sustentar o uso real do MVP local.
- **Relação com PRD/SDD:** scheduling layer, observability and maintenance, automation and refinements.
- **Prioridade:** MVP-hardening.
- **Dependências:** EP-06.
- **Definição de pronto:** logs, jobs leves, documentação operacional, revisão de consistência e UAT local concluídos.

### EP-09 — Cloud readiness

- **Objetivo:** preparar evolução futura sem reescrever o modelo.
- **Relação com PRD/SDD:** cloud readiness / migration, Supabase strategy, optional API.
- **Prioridade:** Future.
- **Dependências:** EP-08.
- **Definição de pronto:** guia de migração, parametrização de ambiente e decisão explícita sobre quando migrar.

---

## 6. Detailed Backlog Items

> Os itens abaixo são derivados das fases do SDD, dos módulos e requisitos do PRD e das lacunas/next steps do BRD. Itens condicionais foram marcados como **Needs validation** ou **Future** conforme a documentação.

- **TB-001**
  - **Título:** Validar definição de aluno ativo
  - **Descrição:** Formalizar regra temporal e cadastral para KPI de alunos ativos.
  - **Fase:** 0
  - **Épico relacionado:** EP-01
  - **Tipo:** Validation
  - **Prioridade:** Needs validation
  - **Dependências:** nenhuma
  - **Critério de pronto:** definição aprovada e documentada
  - **Observações:** bloqueia KPI de alunos ativos, custo por aluno, receita por aluno e ocupação.

- **TB-002**
  - **Título:** Validar elegibilidade e status de rematrícula
  - **Descrição:** Definir elegível/rematriculado/não rematriculado/pendente.
  - **Fase:** 0
  - **Épico relacionado:** EP-01
  - **Tipo:** Validation
  - **Prioridade:** Needs validation
  - **Dependências:** nenhuma
  - **Critério de pronto:** taxonomia aprovada
  - **Observações:** bloqueia taxa de rematrícula.

- **TB-003**
  - **Título:** Validar fórmula de ponto de equilíbrio
  - **Descrição:** Fechar cálculo de break-even e premissas de custo/receita.
  - **Fase:** 0
  - **Épico relacionado:** EP-01
  - **Tipo:** Validation
  - **Prioridade:** Needs validation
  - **Dependências:** definição mínima de categorias de custo e mensalidade
  - **Critério de pronto:** fórmula aprovada e documentada
  - **Observações:** bloqueia KPI de break-even.

- **TB-004**
  - **Título:** Validar fórmula de alunos mínimos para operar
  - **Descrição:** Definir cálculo derivado do break-even.
  - **Fase:** 0
  - **Épico relacionado:** EP-01
  - **Tipo:** Validation
  - **Prioridade:** Needs validation
  - **Dependências:** TB-003
  - **Critério de pronto:** fórmula aprovada e documentada
  - **Observações:** bloqueia KPI de alunos mínimos.

- **TB-005**
  - **Título:** Validar taxonomia acadêmica
  - **Descrição:** Confirmar segmentos, séries/anos reais e convenção de turma.
  - **Fase:** 0
  - **Épico relacionado:** EP-01
  - **Tipo:** Validation
  - **Prioridade:** Needs validation
  - **Dependências:** nenhuma
  - **Critério de pronto:** lista oficial aprovada
  - **Observações:** bloqueia filtros e comparativos.

- **TB-006**
  - **Título:** Validar taxonomia gerencial
  - **Descrição:** Aprovar status do aluno, motivos de saída e faixas de desconto.
  - **Fase:** 0
  - **Épico relacionado:** EP-01
  - **Tipo:** Validation
  - **Prioridade:** Needs validation
  - **Dependências:** nenhuma
  - **Critério de pronto:** taxonomias documentadas
  - **Observações:** impacta validação, analytics e UI.

- **TB-007**
  - **Título:** Validar política de bolsa
  - **Descrição:** Confirmar se bolsa existe, como se diferencia de desconto e quais campos mínimos serão mantidos.
  - **Fase:** 0
  - **Épico relacionado:** EP-01
  - **Tipo:** Validation
  - **Prioridade:** Needs validation
  - **Dependências:** nenhuma
  - **Critério de pronto:** decisão explícita de incluir, adiar ou tratar como campo futuro
  - **Observações:** bloqueia KPIs de bolsa.

- **TB-008**
  - **Título:** Validar capacidade por turma
  - **Descrição:** Confirmar existência, confiabilidade e manutenção de `class_capacity`.
  - **Fase:** 0
  - **Épico relacionado:** EP-01
  - **Tipo:** Validation
  - **Prioridade:** Needs validation
  - **Dependências:** TB-005
  - **Critério de pronto:** fonte e regra de manutenção definidas
  - **Observações:** bloqueia ocupação por turma.

- **TB-009**
  - **Título:** Definir governança mínima dos dados
  - **Descrição:** Formalizar responsável operacional e responsável de decisão para taxonomias/regras.
  - **Fase:** 0
  - **Épico relacionado:** EP-01
  - **Tipo:** Validation
  - **Prioridade:** Needs validation
  - **Dependências:** nenhuma
  - **Critério de pronto:** papéis explicitados
  - **Observações:** reduz risco de deriva de conceito.

- **TB-010**
  - **Título:** Bootstrap do repositório local
  - **Descrição:** Criar estrutura base, ambiente virtual, settings, documentação inicial e app shell.
  - **Fase:** 1
  - **Épico relacionado:** EP-02
  - **Tipo:** Documentation
  - **Prioridade:** MVP
  - **Dependências:** decisões mínimas de Phase 0
  - **Critério de pronto:** projeto sobe localmente com configuração básica
  - **Observações:** sem CI/CD ou API no MVP.

- **TB-011**
  - **Título:** Provisionar PostgreSQL local e configuração segura
  - **Descrição:** Configurar banco local, usuário de acesso e `.env`.
  - **Fase:** 1
  - **Épico relacionado:** EP-02
  - **Tipo:** DevOps/Infra
  - **Prioridade:** MVP
  - **Dependências:** TB-010
  - **Critério de pronto:** conexão local funcional
  - **Observações:** credenciais fora do código.

- **TB-012**
  - **Título:** Implementar models e migrations base
  - **Descrição:** Criar models SQLAlchemy e Alembic para entidades centrais.
  - **Fase:** 2
  - **Épico relacionado:** EP-02
  - **Tipo:** Backend
  - **Prioridade:** MVP
  - **Dependências:** TB-011
  - **Critério de pronto:** migrations aplicam schema sem erro
  - **Observações:** inclui students, classes, revenues, expenses, cost_categories, rematriculations, import_batches.

- **TB-013**
  - **Título:** Implementar tabelas de domínio/taxonomia
  - **Descrição:** Criar domínios controlados para segmentação e status.
  - **Fase:** 2
  - **Épico relacionado:** EP-02
  - **Tipo:** Data
  - **Prioridade:** MVP
  - **Dependências:** TB-005, TB-006, TB-012
  - **Critério de pronto:** domínios persistidos e referenciáveis
  - **Observações:** reduz inconsistência segmentada.

- **TB-014**
  - **Título:** Implementar campos de concessões no schema
  - **Descrição:** Incluir campos de desconto e preparar campos de bolsa no modelo de alunos.
  - **Fase:** 2
  - **Épico relacionado:** EP-02
  - **Tipo:** Data
  - **Prioridade:** MVP
  - **Dependências:** TB-007, TB-012
  - **Critério de pronto:** schema suporta desconto e, se aprovado, bolsa separadamente
  - **Observações:** se bolsa não for aprovada, manter campos opcionais documentados.

- **TB-015**
  - **Título:** Implementar `import_batches` e rastreio de validação
  - **Descrição:** Registrar origem, status e notas de validação por lote.
  - **Fase:** 2
  - **Épico relacionado:** EP-02
  - **Tipo:** Backend
  - **Prioridade:** MVP
  - **Dependências:** TB-012
  - **Critério de pronto:** cargas ficam auditáveis
  - **Observações:** suporta troubleshooting.

- **TB-016**
  - **Título:** Definir template mínimo de cadastro de aluno
  - **Descrição:** Padronizar colunas obrigatórias para aluno com segmentação, status, concessões e saída.
  - **Fase:** 3
  - **Épico relacionado:** EP-03
  - **Tipo:** Documentation
  - **Prioridade:** MVP
  - **Dependências:** TB-005, TB-006, TB-014
  - **Critério de pronto:** template aprovado e distribuído
  - **Observações:** deriva do BRD.

- **TB-017**
  - **Título:** Definir templates financeiros mínimos
  - **Descrição:** Padronizar receitas esperadas vs recebidas e despesas por categoria.
  - **Fase:** 3
  - **Épico relacionado:** EP-03
  - **Tipo:** Documentation
  - **Prioridade:** MVP
  - **Dependências:** TB-003, TB-011
  - **Critério de pronto:** templates financeiros validados
  - **Observações:** bloqueia KPIs financeiros.

- **TB-018**
  - **Título:** Construir validador de taxonomias de aluno
  - **Descrição:** Validar segmento, série/ano, turma, status, desconto e motivo de saída.
  - **Fase:** 3
  - **Épico relacionado:** EP-03
  - **Tipo:** Backend
  - **Prioridade:** MVP
  - **Dependências:** TB-013, TB-016
  - **Critério de pronto:** registros inválidos são rejeitados com mensagem clara
  - **Observações:** crítico para comparativos.

- **TB-019**
  - **Título:** Construir validador de receitas e despesas
  - **Descrição:** Validar campos obrigatórios, categorias e períodos.
  - **Fase:** 3
  - **Épico relacionado:** EP-03
  - **Tipo:** Backend
  - **Prioridade:** MVP
  - **Dependências:** TB-017
  - **Critério de pronto:** lotes inválidos ficam rastreados
  - **Observações:** crítico para resultado mensal.

- **TB-020**
  - **Título:** Implementar importação CSV/Excel
  - **Descrição:** Criar rotina de importação estruturada para dados históricos e operacionais.
  - **Fase:** 4
  - **Épico relacionado:** EP-03
  - **Tipo:** Backend
  - **Prioridade:** MVP
  - **Dependências:** TB-015, TB-018, TB-019
  - **Critério de pronto:** arquivos válidos entram no banco com log por lote
  - **Observações:** formato simples, sem ETL complexo.

- **TB-021**
  - **Título:** Implementar páginas internas de entrada manual
  - **Descrição:** Criar páginas/telas simples para receitas, despesas, rematrículas, mudanças de status e motivo de saída.
  - **Fase:** 4
  - **Épico relacionado:** EP-03
  - **Tipo:** Frontend
  - **Prioridade:** MVP
  - **Dependências:** TB-020
  - **Critério de pronto:** fluxo manual funcional com gravação direta no banco
  - **Observações:** formulários curtos.

- **TB-022**
  - **Título:** Realizar carga histórica inicial
  - **Descrição:** Importar base inicial de alunos, receitas, despesas e rematrículas.
  - **Fase:** 4
  - **Épico relacionado:** EP-03
  - **Tipo:** Data
  - **Prioridade:** MVP
  - **Dependências:** TB-020, TB-021
  - **Critério de pronto:** base inicial carregada e validada
  - **Observações:** registrar gaps remanescentes.

- **TB-023**
  - **Título:** Implementar KPIs financeiros consolidados
  - **Descrição:** Receita bruta, receita recebida, despesas totais e resultado mensal.
  - **Fase:** 5
  - **Épico relacionado:** EP-04
  - **Tipo:** Analytics
  - **Prioridade:** MVP
  - **Dependências:** TB-022
  - **Critério de pronto:** KPIs calculados e conferíveis
  - **Observações:** base do resumo executivo.

- **TB-024**
  - **Título:** Implementar KPIs de estrutura de custos
  - **Descrição:** Totais de aluguel e folha, e suas proporções da receita.
  - **Fase:** 5
  - **Épico relacionado:** EP-04
  - **Tipo:** Analytics
  - **Prioridade:** MVP
  - **Dependências:** TB-017, TB-022
  - **Critério de pronto:** aluguel e folha identificáveis e calculados
  - **Observações:** depende do escopo final da folha.

- **TB-025**
  - **Título:** Implementar KPIs de viabilidade da mensalidade
  - **Descrição:** mensalidade média, desconto médio, custo por aluno, receita por aluno, margem por aluno.
  - **Fase:** 5
  - **Épico relacionado:** EP-04
  - **Tipo:** Analytics
  - **Prioridade:** MVP
  - **Dependências:** TB-001, TB-022, TB-024
  - **Critério de pronto:** indicadores documentados e comparáveis
  - **Observações:** usa aluno ativo.

- **TB-026**
  - **Título:** Implementar KPIs de break-even
  - **Descrição:** ponto de equilíbrio e alunos mínimos para operar.
  - **Fase:** 5
  - **Épico relacionado:** EP-04
  - **Tipo:** Analytics
  - **Prioridade:** MVP
  - **Dependências:** TB-003, TB-004, TB-024, TB-025
  - **Critério de pronto:** fórmulas aplicadas e documentadas
  - **Observações:** não iniciar sem validação.

- **TB-027**
  - **Título:** Implementar KPIs de retenção
  - **Descrição:** alunos ativos, novos alunos, rematrículas, taxa de rematrícula, saídas, taxa de perda.
  - **Fase:** 5
  - **Épico relacionado:** EP-05
  - **Tipo:** Analytics
  - **Prioridade:** MVP
  - **Dependências:** TB-001, TB-002, TB-022
  - **Critério de pronto:** indicadores por período calculados
  - **Observações:** rematrícula depende de elegibilidade validada.

- **TB-028**
  - **Título:** Implementar analytics segmentados por recorte
  - **Descrição:** Agregações por segmento, série/ano e turma para KPIs principais.
  - **Fase:** 5
  - **Épico relacionado:** EP-05
  - **Tipo:** Analytics
  - **Prioridade:** MVP
  - **Dependências:** TB-005, TB-022, TB-023 a TB-027
  - **Critério de pronto:** datasets comparativos consumíveis pela UI
  - **Observações:** comparability by design.

- **TB-029**
  - **Título:** Implementar leitura por faixa de desconto
  - **Descrição:** Construir agrupamentos e análises por faixa de desconto.
  - **Fase:** 5
  - **Épico relacionado:** EP-05
  - **Tipo:** Analytics
  - **Prioridade:** MVP
  - **Dependências:** TB-006, TB-025, TB-028
  - **Critério de pronto:** descontos comparáveis por recorte
  - **Observações:** atende ao requisito funcional de faixas de desconto.

- **TB-030**
  - **Título:** Implementar cruzamento de motivo de saída por recorte
  - **Descrição:** Analisar saída por motivo e segmento/série/turma.
  - **Fase:** 5
  - **Épico relacionado:** EP-05
  - **Tipo:** Analytics
  - **Prioridade:** MVP
  - **Dependências:** TB-006, TB-027, TB-028
  - **Critério de pronto:** corte visível e consistente
  - **Observações:** requisito funcional do PRD.

- **TB-031**
  - **Título:** Documentar catálogo de KPIs e premissas
  - **Descrição:** Registrar lógica, campos usados e dependências de cada KPI do MVP.
  - **Fase:** 5
  - **Épico relacionado:** EP-04
  - **Tipo:** Documentation
  - **Prioridade:** MVP
  - **Dependências:** TB-023 a TB-030
  - **Critério de pronto:** todos os KPIs do MVP documentados
  - **Observações:** necessário para rastreabilidade.

- **TB-032**
  - **Título:** Implementar filtros globais do dashboard
  - **Descrição:** período, segmento, série/ano, turma, status do aluno, status de rematrícula e faixa de desconto.
  - **Fase:** 6
  - **Épico relacionado:** EP-06
  - **Tipo:** Frontend
  - **Prioridade:** MVP
  - **Dependências:** TB-028, TB-029
  - **Critério de pronto:** filtros funcionam de forma previsível
  - **Observações:** visibilidade gradual.

- **TB-033**
  - **Título:** Construir módulo Resumo Executivo
  - **Descrição:** cards e visão consolidada de receita, despesa, resultado e alunos ativos.
  - **Fase:** 6
  - **Épico relacionado:** EP-06
  - **Tipo:** Frontend
  - **Prioridade:** MVP
  - **Dependências:** TB-023, TB-027, TB-032
  - **Critério de pronto:** responde às perguntas executivas principais
  - **Observações:** primeiro módulo da home.

- **TB-034**
  - **Título:** Construir módulo Estrutura de Custos
  - **Descrição:** totais, composição de custos, destaque para aluguel e folha.
  - **Fase:** 6
  - **Épico relacionado:** EP-06
  - **Tipo:** Frontend
  - **Prioridade:** MVP
  - **Dependências:** TB-024, TB-032
  - **Critério de pronto:** pesos de aluguel/folha visíveis
  - **Observações:** sem detalhamento desnecessário.

- **TB-035**
  - **Título:** Construir módulo Alunos e Retenção
  - **Descrição:** novos alunos, rematrículas, perdas, motivos de saída e recortes.
  - **Fase:** 6
  - **Épico relacionado:** EP-06
  - **Tipo:** Frontend
  - **Prioridade:** MVP
  - **Dependências:** TB-027, TB-030, TB-032
  - **Critério de pronto:** retenção e evasão visíveis por período e recorte
  - **Observações:** deve permitir localizar onde a retenção falha.

- **TB-036**
  - **Título:** Construir módulo Receitas e Viabilidade
  - **Descrição:** mensalidade média, desconto, receita por aluno, margem por aluno, break-even e alunos mínimos.
  - **Fase:** 6
  - **Épico relacionado:** EP-06
  - **Tipo:** Frontend
  - **Prioridade:** MVP
  - **Dependências:** TB-025, TB-026, TB-029, TB-032
  - **Critério de pronto:** sustentabilidade e pressão de margem visíveis
  - **Observações:** leitura simples.

- **TB-037**
  - **Título:** Implementar comparativos por recorte
  - **Descrição:** blocos comparativos entre segmento, série/ano e turma.
  - **Fase:** 6
  - **Épico relacionado:** EP-06
  - **Tipo:** Frontend
  - **Prioridade:** MVP
  - **Dependências:** TB-028, TB-032
  - **Critério de pronto:** comparativos principais renderizados no dashboard
  - **Observações:** foco nos indicadores MVP.

- **TB-038**
  - **Título:** Implementar alertas e ações prioritárias
  - **Descrição:** alertas visuais para riscos gerenciais críticos do MVP.
  - **Fase:** 6
  - **Épico relacionado:** EP-06
  - **Tipo:** Frontend
  - **Prioridade:** MVP
  - **Dependências:** TB-023 a TB-030, TB-032
  - **Critério de pronto:** alertas visíveis e documentados
  - **Observações:** thresholds podem começar simples se aprovados.

- **TB-039**
  - **Título:** Revisar compreensibilidade da UI com liderança
  - **Descrição:** rodada de revisão para confirmar que o dashboard permanece simples para usuários não técnicos.
  - **Fase:** 6
  - **Épico relacionado:** EP-06
  - **Tipo:** Validation
  - **Prioridade:** MVP
  - **Dependências:** TB-033 a TB-038
  - **Critério de pronto:** feedback incorporado ou registrado
  - **Observações:** validação de UX do MVP.

- **TB-040**
  - **Título:** Implementar módulo de ocupação por turma
  - **Descrição:** capacidade, matriculados e taxa de ocupação por turma.
  - **Fase:** 7
  - **Épico relacionado:** EP-07
  - **Tipo:** Analytics
  - **Prioridade:** Needs validation
  - **Dependências:** TB-008, TB-028
  - **Critério de pronto:** ocupação calculada apenas com capacidade validada
  - **Observações:** condicional.

- **TB-041**
  - **Título:** Implementar separação analítica bolsa vs desconto
  - **Descrição:** diferenciar leitura funcional e analítica entre concessões.
  - **Fase:** 7
  - **Épico relacionado:** EP-07
  - **Tipo:** Analytics
  - **Prioridade:** Needs validation
  - **Dependências:** TB-007, TB-014, TB-022
  - **Critério de pronto:** concessões não se misturam indevidamente
  - **Observações:** alto risco se política for ambígua.

- **TB-042**
  - **Título:** Implementar KPIs de bolsa
  - **Descrição:** número e percentual de bolsistas, valor concedido por período e recorte.
  - **Fase:** 7
  - **Épico relacionado:** EP-07
  - **Tipo:** Analytics
  - **Prioridade:** Needs validation
  - **Dependências:** TB-041
  - **Critério de pronto:** KPIs calculados sobre dados válidos
  - **Observações:** não priorizar sem base mínima.

- **TB-043**
  - **Título:** Implementar visão de inadimplência segmentada
  - **Descrição:** abrir módulo de métricas de inadimplência se existirem dados confiáveis.
  - **Fase:** 7/9
  - **Épico relacionado:** EP-07
  - **Tipo:** Analytics
  - **Prioridade:** Future
  - **Dependências:** validação de granularidade financeira e schema condicional
  - **Critério de pronto:** módulo opera sobre base confiável
  - **Observações:** fora do core MVP.

- **TB-044**
  - **Título:** Implementar logs operacionais mínimos
  - **Descrição:** logs de importação, falhas de validação, consultas e inconsistências.
  - **Fase:** 8
  - **Épico relacionado:** EP-08
  - **Tipo:** DevOps/Infra
  - **Prioridade:** MVP
  - **Dependências:** TB-020, TB-021, TB-023+
  - **Critério de pronto:** falhas críticas são rastreáveis
  - **Observações:** observabilidade mínima.

- **TB-045**
  - **Título:** Implementar jobs leves de atualização
  - **Descrição:** rotinas simples de refresh/reprocessamento/importação agendada.
  - **Fase:** 8
  - **Épico relacionado:** EP-08
  - **Tipo:** DevOps/Infra
  - **Prioridade:** MVP
  - **Dependências:** MVP funcional estabilizado
  - **Critério de pronto:** jobs pequenos e configuráveis funcionando
  - **Observações:** sem automação pesada.

- **TB-046**
  - **Título:** Executar validação local do MVP
  - **Descrição:** revisar KPIs, filtros, alertas e usabilidade com liderança/gestão.
  - **Fase:** 8
  - **Épico relacionado:** EP-08
  - **Tipo:** Validation
  - **Prioridade:** MVP
  - **Dependências:** TB-033 a TB-039
  - **Critério de pronto:** aceite funcional do MVP e gaps registrados
  - **Observações:** condição para cloud readiness.

- **TB-047**
  - **Título:** Documentar limitações conhecidas e itens em aberto
  - **Descrição:** registrar explicitamente lacunas que afetem precisão dos KPIs.
  - **Fase:** 8
  - **Épico relacionado:** EP-08
  - **Tipo:** Documentation
  - **Prioridade:** MVP
  - **Dependências:** TB-046
  - **Critério de pronto:** documento de limitações atualizado
  - **Observações:** necessário para transparência do MVP.

- **TB-048**
  - **Título:** Preparar parametrização para migração futura
  - **Descrição:** isolar `DATABASE_URL`, segredos e parâmetros para facilitar mudança para banco gerenciado.
  - **Fase:** 9
  - **Épico relacionado:** EP-09
  - **Tipo:** DevOps/Infra
  - **Prioridade:** Future
  - **Dependências:** TB-046
  - **Critério de pronto:** ambiente pode trocar de banco sem reescrever lógica
  - **Observações:** cloud-ready, não cloud-now.

- **TB-049**
  - **Título:** Elaborar guia de migração local → cloud
  - **Descrição:** registrar passos prudentes para eventual Supabase/postgres gerenciado.
  - **Fase:** 9
  - **Épico relacionado:** EP-09
  - **Tipo:** Documentation
  - **Prioridade:** Future
  - **Dependências:** TB-048
  - **Critério de pronto:** guia de migração revisado
  - **Observações:** seguir estratégia prudente do SDD.

---

## 7. MVP Implementation Scope

### Componentes mínimos

- Database Layer
- Ingestion Layer
- Taxonomy and Validation Layer
- Transformation / Analytics Layer
- Frontend / Dashboard Layer
- Configuration and Secrets Layer

Scheduling/automation pode entrar como hardening leve, mas não deve bloquear a primeira validação funcional do MVP local.

### Dados mínimos

- Cadastro estruturado de alunos com segmento, série/ano, turma, status do aluno, data de entrada, data de saída quando houver, motivo de saída, mensalidade e desconto.
- Receitas com período de referência, esperado, desconto e recebido.
- Despesas com período, categoria e valor.
- Rematrículas com ano acadêmico, elegibilidade, confirmação e status.
- Categorias de custo mínimas, especialmente aluguel e folha.

### KPIs mínimos

- Alunos ativos
- Novos alunos
- Total de rematrículas
- Taxa de rematrícula
- Saídas
- Taxa de perda
- Receita bruta
- Receita recebida
- Despesas totais
- Resultado mensal
- Total de aluguel
- Total de folha
- Aluguel como % da receita
- Folha como % da receita
- Mensalidade média
- Desconto médio
- Custo por aluno
- Receita por aluno
- Margem por aluno
- Ponto de equilíbrio
- Alunos mínimos para operar

Além disso, os comparativos principais por segmento/série/turma para os indicadores MVP.

### Módulos mínimos

- Filtros Gerais
- Resumo Executivo
- Alunos e Retenção
- Visão de Receitas
- Estrutura de Custos
- Viabilidade e Sustentabilidade da Mensalidade
- Alertas e Ações Prioritárias
- Comparativos por recorte

Concessões no MVP mínimo cobrem **descontos**. Bolsas entram apenas se validadas.

### Validações mínimas

- aluno ativo
- rematrícula elegível/status
- taxonomia acadêmica
- taxonomia de motivo de saída
- faixas de desconto
- fórmula de break-even/alunos mínimos
- categorias financeiras mínimas

Sem isso, o MVP pode até rodar, mas não é confiável.

### O que pode ficar de fora do MVP sem comprometer valor

- KPIs e visualizações de bolsa
- módulo robusto de inadimplência
- comparações históricas profundas por turma/série
- cenários simulados
- margem detalhada por turma com alta precisão
- API dedicada
- migração para nuvem
- materialized views e automações sofisticadas

---

## 8. Validation Items Before or During Build

### Alta criticidade

- **Definição de aluno ativo**
  - **Por que importa:** afeta base de quase todos os KPIs por aluno.
  - **Fase impactada:** 0, 5, 6
  - **Impacto de não validar:** custo/receita por aluno e ocupação podem ficar distorcidos.

- **Fórmula de ponto de equilíbrio**
  - **Por que importa:** sustenta a leitura de viabilidade.
  - **Fase impactada:** 0, 5, 6
  - **Impacto de não validar:** indicador estratégico pode ficar incorreto.

- **Fórmula de alunos mínimos para operar**
  - **Por que importa:** desdobra o break-even em decisão gerencial.
  - **Fase impactada:** 0, 5, 6
  - **Impacto de não validar:** leitura errada da sustentabilidade operacional.

- **Cadastro confiável de segmento/série/turma**
  - **Por que importa:** viabiliza filtros e comparativos.
  - **Fase impactada:** 0, 2, 3, 5, 6
  - **Impacto de não validar:** segmentação perde confiabilidade.

- **Estrutura real de receitas e despesas**
  - **Por que importa:** sem isso não há resultado mensal confiável.
  - **Fase impactada:** 0, 3, 5
  - **Impacto de não validar:** dashboard financeiro vira aproximação fraca.

- **Capacidade por turma**
  - **Por que importa:** determina se ocupação entra de fato.
  - **Fase impactada:** 0, 7
  - **Impacto de não validar:** módulo de ocupação deve ser despriorizado.

- **Política formal de bolsa distinta de desconto**
  - **Por que importa:** evita mistura conceitual em concessões.
  - **Fase impactada:** 0, 2, 7
  - **Impacto de não validar:** análises de bolsa não devem ser liberadas.

- **Responsável formal pela governança dos dados**
  - **Por que importa:** evita deriva de taxonomia e manutenção difusa.
  - **Fase impactada:** 0, 8
  - **Impacto de não validar:** alta chance de inconsistência recorrente.

### Média criticidade

- Classificação de motivos de saída.
- Padrão de desconto: valor, percentual ou ambos.
- Escopo final da folha.
- Taxonomia de status do aluno e rematrícula.
- Situação financeira e granularidade de registro.
- Thresholds de alertas por recorte.

### Baixa criticidade

- Necessidade futura de API.
- Necessidade futura de materialized views.
- Conveniência de Supabase na fase cloud.
- Profundidade futura de comparações históricas por turma/série.

---

## 9. Dependencies Map

- **Taxonomias acadêmicas aprovadas**
  - **O que bloqueia:** schema final, validadores, filtros, comparativos
  - **Risco associado:** segmentação inconsistente
  - **Mitigação sugerida:** fechar Phase 0 antes de migrations amplas

- **Cadastro mínimo de aluno**
  - **O que bloqueia:** ingestão, KPIs por aluno, retenção, desconto por recorte
  - **Risco associado:** base parcial e indicadores frágeis
  - **Mitigação sugerida:** template mínimo obrigatório

- **Receitas estruturadas**
  - **O que bloqueia:** receita recebida, resultado, receita por aluno, margem
  - **Risco associado:** visão financeira incompleta
  - **Mitigação sugerida:** padronizar esperado vs recebido

- **Despesas categorizadas**
  - **O que bloqueia:** custos, aluguel, folha, break-even
  - **Risco associado:** custo total sem interpretação
  - **Mitigação sugerida:** categorias mínimas antes dos KPIs

- **Definição de aluno ativo**
  - **O que bloqueia:** custo por aluno, receita por aluno, ocupação, alunos ativos
  - **Risco associado:** distorção estrutural
  - **Mitigação sugerida:** aprovar fórmula antes do build analítico

- **Regras de rematrícula**
  - **O que bloqueia:** taxa de rematrícula
  - **Risco associado:** comparações irreais
  - **Mitigação sugerida:** formalizar elegibilidade/status

- **Capacidade por turma**
  - **O que bloqueia:** ocupação
  - **Risco associado:** métrica falsa de ociosidade
  - **Mitigação sugerida:** tratar como módulo condicional

- **Política de bolsa**
  - **O que bloqueia:** diferenciação bolsa vs desconto e KPIs de bolsa
  - **Risco associado:** mistura conceitual de concessões
  - **Mitigação sugerida:** separar modelo e validação antes de priorizar

- **KPI layer funcional**
  - **O que bloqueia:** dashboard MVP
  - **Risco associado:** UI construída sobre queries ad hoc
  - **Mitigação sugerida:** centralizar lógica analítica antes da visualização

- **MVP local estabilizado**
  - **O que bloqueia:** automação e cloud readiness
  - **Risco associado:** escalar instabilidade
  - **Mitigação sugerida:** validar localmente primeiro

---

## 10. Risks to Execution

- **Descrição:** dados iniciais inconsistentes  
  **Impacto:** Alto  
  **Probabilidade:** Alta  
  **Mitigação:** schema validado, importação controlada, revisão inicial  
  **Fase mais afetada:** 2 a 5

- **Descrição:** ambiguidade de regras de negócio  
  **Impacto:** Alto  
  **Probabilidade:** Alta  
  **Mitigação:** fechar definições antes dos KPIs finais  
  **Fase mais afetada:** 0 e 5

- **Descrição:** resistência à adoção digital  
  **Impacto:** Alto  
  **Probabilidade:** Média/Alta  
  **Mitigação:** interface simples, poucos passos, foco no essencial  
  **Fase mais afetada:** 4, 6, 8

- **Descrição:** segmentação inconsistente  
  **Impacto:** Alto  
  **Probabilidade:** Alta  
  **Mitigação:** taxonomias controladas e validações obrigatórias  
  **Fase mais afetada:** 2 a 6

- **Descrição:** capacidade por turma ausente  
  **Impacto:** Médio/Alto  
  **Probabilidade:** Média  
  **Mitigação:** tratar ocupação como condicional até validação  
  **Fase mais afetada:** 7

- **Descrição:** bolsa confundida com desconto  
  **Impacto:** Alto  
  **Probabilidade:** Média/Alta  
  **Mitigação:** separar modelo e validação de concessões  
  **Fase mais afetada:** 2 e 7

- **Descrição:** frontend ficar complexo demais  
  **Impacto:** Médio  
  **Probabilidade:** Média  
  **Mitigação:** leitura em camadas, filtros graduais, comparativos focados  
  **Fase mais afetada:** 6

- **Descrição:** inclusão prematura de API ou cloud  
  **Impacto:** Médio  
  **Probabilidade:** Média  
  **Mitigação:** manter sem API no MVP e migrar só após validação local  
  **Fase mais afetada:** 1 e 9

---

## 11. Suggested Work Sequence

1. Fechar workshop de validação com direção/gestão.
2. Aprovar taxonomias e fórmulas críticas.
3. Bootstrapar repo e ambiente local.
4. Subir PostgreSQL local e configuração.
5. Criar schema + migrations.
6. Implementar domínios de taxonomia e rastreio de importação.
7. Definir templates mínimos de aluno, receita e despesa.
8. Construir validadores e importação.
9. Carregar base histórica inicial.
10. Implementar KPIs financeiros e de viabilidade.
11. Implementar KPIs de retenção e analytics segmentados.
12. Documentar todas as fórmulas do MVP.
13. Construir dashboard com filtros, módulos e alertas.
14. Validar usabilidade com liderança.
15. Só então decidir sobre ocupação, bolsas e inadimplência.
16. Estabilizar localmente com logs e jobs leves.
17. Preparar cloud readiness apenas após aceite local.

---

## 12. Recommended Repo / Project Workstreams

### 1. Data foundation

Objetivo: banco local, schema, migrations, modelos e domínios. É a frente que cria a fonte de verdade e destrava ingestão e analytics.

### 2. Taxonomy and data quality

Objetivo: templates, validações, regras de rejeição, padronização de conceitos e rastreio de lotes. É a frente que reduz o maior risco do projeto: base inconsistente.

### 3. Analytics layer

Objetivo: consultas/views/serviços que calculam KPIs consolidados e segmentados fora da UI. É a frente que garante rastreabilidade e manutenção.

### 4. App / dashboard

Objetivo: Streamlit, filtros, módulos, alertas, páginas internas de entrada e leitura em camadas. É a frente de consumo gerencial.

### 5. Validation and QA

Objetivo: fechar fórmulas, revisar amostras, validar consistência dos números e comprovar compreensibilidade com usuários reais.

### 6. Ops and maintenance

Objetivo: logs, jobs leves, revisão periódica de consistência e preparação para futura migração.

---

## 13. Definition of Done for the MVP

### Critérios técnicos

- aplicação roda localmente com PostgreSQL local e configuração por `.env`
- schema versionado por Alembic
- ingestão manual e/ou por importação funcionando
- validações de taxonomia ativas
- KPIs do MVP centralizados fora da UI
- fórmulas documentadas
- limitações conhecidas registradas

### Critérios funcionais

- dashboard exibe visão mensal consolidada de receita, despesas e resultado
- exibe aluguel/folha e seus pesos
- exibe alunos ativos, novos, saídas, rematrículas e taxa de rematrícula
- exibe custo por aluno e receita por aluno
- exibe ponto de equilíbrio e alunos mínimos com lógica aprovada
- permite detalhar motivos de saída
- possui alertas visuais críticos
- possui filtros por segmento, série/ano e turma
- exibe comparativos principais por recorte acadêmico

### Critérios de dados

- base mínima de alunos, receitas, despesas e rematrículas estruturada
- categorias financeiras mínimas padronizadas
- taxonomias acadêmicas e gerenciais aprovadas
- dados inválidos rejeitados ou explicitamente sinalizados

### Critérios de validação com usuário

- liderança revisou o dashboard e o considera compreensível
- questões abertas que afetam precisão estão documentadas
- decisão explícita tomada sobre ocupação e bolsas no primeiro ciclo

---

## 14. Post-MVP Roadmap

- ocupação por turma, se capacidade validada não estiver pronta no primeiro ciclo
- diferenciação completa de bolsa vs desconto
- KPIs e visões de bolsa por recorte
- módulo robusto de inadimplência segmentada
- comparações históricas avançadas por turma/série
- cenários simulados por recorte
- margem detalhada por turma com maior precisão
- automações mais sofisticadas de governança e reconciliação
- materializações avançadas
- eventual API, somente se houver múltiplos consumidores
- migração para cloud/Supabase após maturidade local

---

## 15. Recommended Next Step

O próximo passo mais adequado é executar uma **Phase 0 formal** de alinhamento com a liderança e a gestão administrativa para fechar, em uma única rodada controlada, as definições de aluno ativo, rematrícula, taxonomias, desconto vs bolsa, capacidade por turma e fórmulas de viabilidade.

Com isso aprovado, o trabalho deve começar imediatamente pela atualização do schema, das migrations e da camada de validação, antes de qualquer expansão visual do dashboard.
```
