
# Solution Design Document — @CESOL

## PARTE 1 — Change Summary

### O que foi alterado em relação ao SDD original

O SDD v1.1 preserva o núcleo técnico do SDD v1.0 — arquitetura **local-first**, banco relacional, ingestão estruturada, camada analítica separada, dashboard em Streamlit, stack gratuita e preparação para evolução futura em nuvem — e incorpora a nova profundidade analítica introduzida pelo PRD v1.1.

As principais mudanças são:

- expansão da modelagem para suportar:
  - `segment`
  - `grade_level`
  - `class_name`
  - `student_status`
  - `rematriculation_status`
  - `discount_band`
  - `financial_status`
  - `exit_reason`
  - `scholarship_flag`
  - `scholarship_type`
  - `scholarship_amount` / `scholarship_percentage`
  - `class_capacity`
  - `class_occupancy_rate`
- atualização da camada analítica para:
  - agregações por segmento
  - agregações por série/ano
  - agregações por turma
  - cálculo de ocupação
  - leitura comparativa por recorte
  - separação analítica entre desconto e bolsa
- atualização da ingestão para exigir:
  - padronização de taxonomias
  - validação de recortes acadêmicos
  - validação de campos ligados a concessões e ocupação
- atualização do frontend para suportar:
  - filtros segmentados
  - leitura em camadas
  - comparativos entre segmentos/séries/turmas
  - novos blocos de concessões e ocupação
- reestruturação das fases de implementação para incluir:
  - evolução do schema
  - padronização dos recortes
  - novos KPIs por recorte
  - fase condicional para bolsa e inadimplência

### Por que essas alterações foram necessárias

O PRD v1.1 deixa claro que a solução não pode mais atender apenas a uma visão consolidada da escola. A arquitetura agora precisa suportar tecnicamente perguntas como:

- onde a margem está mais pressionada;
- em quais séries/turmas a evasão é maior;
- onde descontos e bolsas estão concentrados;
- quais turmas apresentam baixa ocupação;
- como a operação se comporta por segmento, série/ano e turma.

Isso exige que a segmentação deixe de ser apenas uma preocupação de visualização e passe a ser tratada desde:

- o modelo de dados;
- a ingestão;
- a validação;
- a camada analítica;
- os filtros e comparativos do dashboard.

### Seções impactadas

As seções atualizadas foram:

- Solution Overview
- PRD Alignment Summary
- Technical Design Principles
- Recommended Technology Stack
- High-Level Architecture
- Core Solution Components
- Data Architecture
- Data Ingestion and Update Strategy
- Data Processing and KPI Computation
- Application Flow
- API and Service Layer Design
- Frontend / Dashboard Design Approach
- Real-Time / Near-Real-Time Strategy
- Security and Access Considerations
- Local Development Architecture
- Cloud Evolution Strategy
- Observability and Maintenance Strategy
- Implementation Phases
- Technical Risks and Trade-offs
- Open Questions / Items to Validate
- Traceability Matrix
- Recommended Next Step

### O que mudou tecnicamente no MVP

Entram no MVP técnico v1.1:

- suporte estrutural à segmentação por segmento, série/ano e turma;
- filtros segmentados na camada de apresentação;
- suporte a `student_status`, `rematriculation_status` e `discount_band`;
- suporte a taxa de ocupação por turma, se `class_capacity` estiver disponível;
- agregações por recorte na camada analítica;
- estrutura de dados preparada para bolsa separada de desconto, mesmo que parte da análise de bolsas dependa de validação.

### O que ficou como Pós-MVP ou dependente de validação

Ficam como **Post-MVP / Future Release** ou **Needs validation before prioritization**:

- módulo analítico completo de bolsas, se a política e os dados ainda não estiverem minimamente estruturados;
- módulo robusto de inadimplência segmentada;
- alocação de margem por turma com precisão elevada;
- automações mais sofisticadas de governança e reconciliação;
- API dedicada, caso surja necessidade real de múltiplos consumidores;
- materializações avançadas, caso o volume cresça.

---

# SDD — @CESOL School Financial and Administrative Dashboard v1.1

## 1. Solution Overview

A solução proposta para o **@CESOL School Financial and Administrative Dashboard** continua sendo uma aplicação de gestão orientada por dados, construída com arquitetura **local-first** para o MVP e preparada para evolução posterior em nuvem.

Na versão v1.1, a solução deixa de atender apenas uma leitura consolidada da operação escolar e passa a suportar também uma leitura **segmentada, comparativa e gerencial**, permitindo que a liderança visualize desempenho por **segmento**, **série/ano** e **turma**, além de cruzamentos por **status**, **desconto**, **motivo de saída**, **ocupação** e, quando viável, **bolsas**.

O problema técnico-organizacional que a solução continua resolvendo é triplo:

- ausência de base estruturada para cálculo de KPIs;
- dificuldade de atualização consistente das informações;
- baixa visibilidade gerencial para tomada de decisão recorrente.

Na versão v1.1, esse escopo técnico é ampliado para incluir a necessidade de localizar **onde** estão os problemas e oportunidades, sem transformar a solução em uma arquitetura excessivamente complexa.

---

## 2. PRD Alignment Summary

### Módulos atendidos
- Filtros Gerais
- Resumo Executivo
- Alunos e Retenção
- Visão de Receitas
- Estrutura de Custos
- Viabilidade e Sustentabilidade da Mensalidade
- Concessões (Descontos e Bolsas)
- Ocupação por Turma
- Alertas e Ações Prioritárias
- Visão de Inadimplência como módulo condicional

### Requisitos funcionais cobertos
A solução suporta diretamente os requisitos funcionais ligados a:

- consolidação mensal de receitas e despesas;
- cálculo de resultado mensal;
- visualização de aluguel e folha;
- cálculo de custo, receita e margem por aluno;
- rematrícula, entradas, saídas e motivos de saída;
- filtros por período, segmento, série/ano e turma;
- leitura por status do aluno e status de rematrícula;
- leitura de desconto por recorte;
- ocupação por turma, quando houver capacidade validada;
- separação funcional entre desconto e bolsa, quando houver dados válidos;
- comparativos por recorte acadêmico.

### KPIs suportados
A arquitetura suporta os KPIs do MVP v1.1, incluindo:

- KPIs consolidados financeiros;
- KPIs de retenção;
- KPIs de sustentabilidade;
- KPIs segmentados por segmento, série/ano e turma;
- taxa de ocupação por turma, se houver capacidade;
- KPIs de bolsas e inadimplência apenas quando houver base minimamente confiável.

### Restrições absorvidas
- usuários com baixa maturidade digital;
- necessidade de simplicidade visual e operacional;
- necessidade de começar localmente e validar antes de migrar para nuvem;
- necessidade de padronizar taxonomias antes de liberar análises mais profundas;
- necessidade de evitar overengineering.

### Riscos considerados
- baixa qualidade inicial dos dados;
- taxonomias inconsistentes;
- falta de capacidade por turma;
- confusão entre desconto e bolsa;
- ambiguidade em regras de negócio críticas;
- risco de complexidade excessiva na visualização.

---

## 3. Technical Design Principles

1. **Simplicity first**  
   A solução deve resolver corretamente o problema com o menor número de componentes possível.

2. **Local-first, cloud-later**  
   O MVP deve rodar localmente com estabilidade antes de qualquer evolução para nuvem.

3. **Low operational friction**  
   Atualização e uso devem exigir o mínimo possível de retrabalho manual adicional.

4. **Modularity**  
   Camadas de dados, cálculo e visualização devem ser separadas.

5. **Maintainability**  
   Regras de cálculo, taxonomias e acesso a dados devem ser explícitos e fáceis de alterar.

6. **Traceability**  
   Cada componente técnico deve estar ligado a um módulo, requisito ou KPI do PRD.

7. **Low-cost architecture**  
   A solução deve usar stack gratuita ou com uso gratuito suficiente para MVP.

8. **Pragmatic near-real-time**  
   Atualização dos dados deve ser próxima do tempo real quando isso for realista, sem introduzir arquitetura desnecessária.

9. **Segmentação sem complexidade excessiva**  
   A modelagem deve suportar recortes por segmento/série/turma sem multiplicar componentes desnecessários.

10. **Comparability by design**  
   A camada analítica deve ser preparada para comparativos por recorte desde a estrutura dos dados.

11. **Layered consumption**  
   O dashboard deve consumir profundidade analítica em camadas, preservando simplicidade na experiência.

---

## 4. Recommended Technology Stack

### 4.1 Preferred Stack

#### Python 3.11+
- **Função:** linguagem principal da solução
- **Por que foi escolhida:** excelente aderência ao ambiente existente, ecossistema forte para dados e dashboard
- **Aderente ao ambiente existente:** sim
- **MVP-ready:** sim
- **Cloud-ready:** sim
- **Custo:** 100% gratuita

#### PostgreSQL local
- **Função:** banco de dados principal no MVP
- **Por que foi escolhido:** robusto, gratuito, maduro e compatível com futura migração para Supabase
- **Aderente ao ambiente existente:** parcialmente
- **MVP-ready:** sim
- **Cloud-ready:** sim
- **Custo:** 100% gratuito

#### SQLAlchemy 2.x
- **Função:** camada de acesso a dados e modelagem ORM/SQL
- **Por que foi escolhida:** separação entre aplicação e banco, alta manutenibilidade
- **Aderente ao ambiente existente:** sim
- **MVP-ready:** sim
- **Cloud-ready:** sim
- **Custo:** 100% gratuita

#### Alembic
- **Função:** versionamento de schema
- **Por que foi escolhido:** garante evolução controlada do banco
- **Aderente ao ambiente existente:** compatível
- **MVP-ready:** sim
- **Cloud-ready:** sim
- **Custo:** 100% gratuita

#### Pandas
- **Função:** ingestão, padronização e processamento tabular
- **Por que foi escolhida:** ideal para importação inicial e padronização de dados históricos
- **Aderente ao ambiente existente:** sim
- **MVP-ready:** sim
- **Cloud-ready:** sim
- **Custo:** 100% gratuita

#### Streamlit
- **Função:** interface do dashboard e possíveis telas internas de entrada simplificada
- **Por que foi escolhida:** rápida implementação, ótima aderência ao caso de uso gerencial
- **Aderente ao ambiente existente:** sim
- **MVP-ready:** sim
- **Cloud-ready:** sim
- **Custo:** 100% gratuita

#### Plotly
- **Função:** gráficos interativos
- **Por que foi escolhida:** integra bem com Streamlit e facilita leitura comparativa
- **Aderente ao ambiente existente:** sim
- **MVP-ready:** sim
- **Cloud-ready:** sim
- **Custo:** 100% gratuita

#### Pydantic / pydantic-settings
- **Função:** configuração e validação de schemas
- **Por que foi escolhida:** melhora confiabilidade de inputs e configuração
- **Aderente ao ambiente existente:** compatível
- **MVP-ready:** sim
- **Cloud-ready:** sim
- **Custo:** 100% gratuita

#### OpenPyXL / CSV
- **Função:** leitura de planilhas para carga inicial e importação em lote
- **Por que foi escolhida:** reduz retrabalho na migração de dados
- **Aderente ao ambiente existente:** compatível
- **MVP-ready:** sim
- **Cloud-ready:** sim
- **Custo:** 100% gratuita

#### APScheduler ou agendamento nativo do sistema
- **Função:** automação leve de importações e atualizações
- **Por que foi escolhido:** permite automação simples sem infraestrutura pesada
- **Aderente ao ambiente existente:** compatível
- **MVP-ready:** sim
- **Cloud-ready:** sim
- **Custo:** 100% gratuita

### 4.2 Alternative Stack(s), if applicable

#### Alternativa A — Supabase + Streamlit direto
- boa opção quando a migração para nuvem acontecer;
- simplifica banco gerenciado;
- útil se a governança do PostgreSQL local se tornar frágil;
- não é a melhor base do MVP enquanto a prioridade for validação local.

#### Alternativa B — PostgreSQL/Supabase + Flask/FastAPI + Streamlit
- boa opção quando houver necessidade clara de:
  - múltiplos consumidores de dados;
  - integrações externas;
  - desacoplamento forte entre backend e frontend;
  - regras centralizadas em serviço.
- no MVP, tende a aumentar complexidade sem ganho proporcional.

#### Alternativa C — SQLite + Streamlit
- extremamente simples para protótipo;
- inadequada como base do projeto pela futura necessidade de comparativos, consistência e evolução.

### 4.3 Trade-off Analysis

#### Opção A — Banco de dados + Streamlit direto
**Vantagens**
- menor complexidade
- implementação mais rápida
- menos componentes para manter
- ótimo encaixe para MVP local-first

**Desvantagens**
- menor desacoplamento
- pode exigir refatoração moderada se o projeto crescer muito

**Adequação ao MVP**
- alta

#### Opção B — Banco de dados + API + Streamlit
**Vantagens**
- melhor desacoplamento
- mais escalável para múltiplos consumidores
- favorece integrações futuras

**Desvantagens**
- mais componentes
- mais manutenção
- maior esforço inicial
- provavelmente exagerado para o MVP

**Adequação ao MVP**
- média

### 4.4 Final Recommendation for Local-First MVP

**Recomendação final:**  
**PostgreSQL local + SQLAlchemy + Pandas + Streamlit**, sem API dedicada no MVP.

**Justificativa:**
- continua sendo o melhor equilíbrio entre simplicidade, robustez e velocidade;
- a nova segmentação não exige mudança de stack, apenas evolução do modelo de dados, da camada analítica e da interface;
- preserva coerência com a estratégia local-first e cloud-later.

---

## 5. High-Level Architecture

A solução continua organizada em cinco camadas principais:

1. **Camada de armazenamento**  
   Banco PostgreSQL local como fonte de verdade.

2. **Camada de ingestão**  
   Entradas manuais simplificadas + importação estruturada de arquivos.

3. **Camada de transformação e analytics**  
   Padronização, validação, taxonomias e cálculo de KPIs consolidados e segmentados.

4. **Camada de apresentação**  
   Dashboard em Streamlit para leitura gerencial em camadas.

5. **Camada de automação leve**  
   Jobs agendados e rotinas de atualização/importação.

```mermaid
flowchart LR
    A[Entradas manuais simples] --> B[Camada de ingestão]
    A2[Importação CSV/Excel] --> B
    B --> C[(PostgreSQL local)]
    C --> D[Camada de analytics e KPIs]
    D --> E[Dashboard Streamlit]
    F[Jobs agendados] --> B
    E --> G[Usuários de gestão]
````

### Ajuste v1.1 na arquitetura lógica

A nova leitura segmentada exige que a camada analítica passe a trabalhar explicitamente com:

* dimensões acadêmicas:

  * `segment`
  * `grade_level`
  * `class_name`
* dimensões gerenciais:

  * `student_status`
  * `rematriculation_status`
  * `discount_band`
  * `financial_status`
  * `exit_reason`
* dimensões condicionais:

  * `scholarship_flag`
  * `scholarship_type`
  * `class_capacity`

---

## 6. Core Solution Components

### 6.1 Database Layer

* **Objetivo:** armazenar dados operacionais e analíticos
* **Responsabilidades:** persistência, integridade, versionamento de schema
* **Entradas:** registros de alunos, receitas, despesas, rematrículas, turmas, categorias, concessões
* **Saídas:** tabelas operacionais e visões analíticas
* **Relação com o PRD:** suporta todos os módulos e KPIs
* **Prioridade:** MVP

### 6.2 Ingestion Layer

* **Objetivo:** permitir entrada e atualização de dados sem retrabalho excessivo
* **Responsabilidades:** ingestão manual simplificada, importação em lote, validação inicial e padronização de taxonomias
* **Entradas:** formulários, CSV, Excel
* **Saídas:** dados padronizados no banco
* **Relação com o PRD:** responde à necessidade de reduzir dependência de papel e dar confiabilidade à segmentação
* **Prioridade:** MVP

### 6.3 Taxonomy and Validation Layer

* **Objetivo:** controlar consistência dos recortes acadêmicos e gerenciais
* **Responsabilidades:** validar segmento, série/ano, turma, status, desconto, bolsa e motivos de saída
* **Entradas:** dados operacionais brutos
* **Saídas:** registros aceitos ou rejeitados com mensagens de erro
* **Relação com o PRD:** fundamental para leitura segmentada confiável
* **Prioridade:** MVP
* **Origem:** Derived from PRD v1.1

### 6.4 Transformation / Analytics Layer

* **Objetivo:** organizar regras de negócio e cálculo de KPIs
* **Responsabilidades:** cálculo de métricas consolidadas e segmentadas, comparativos, views e validações de consistência
* **Entradas:** tabelas operacionais
* **Saídas:** datasets analíticos e KPIs
* **Relação com o PRD:** suporta todos os requisitos analíticos
* **Prioridade:** MVP

### 6.5 Frontend / Dashboard Layer

* **Objetivo:** fornecer leitura gerencial clara e rápida
* **Responsabilidades:** filtros, cards, gráficos, tabelas, alertas, leitura em camadas
* **Entradas:** datasets analíticos e KPIs
* **Saídas:** visualização para usuários
* **Relação com o PRD:** implementa os módulos do dashboard
* **Prioridade:** MVP

### 6.6 Scheduling / Automation Layer

* **Objetivo:** automatizar importações e atualizações leves
* **Responsabilidades:** execução programada de rotinas de carga, refresh e validação periódica
* **Entradas:** arquivos, comandos agendados, triggers simples
* **Saídas:** dados atualizados e reprocessados
* **Relação com o PRD:** reduz retrabalho técnico e melhora atualização
* **Prioridade:** MVP

### 6.7 Configuration and Secrets Layer

* **Objetivo:** isolar configurações e credenciais
* **Responsabilidades:** gerenciar URLs de banco, flags de ambiente, segredos e parâmetros de taxonomia
* **Entradas:** `.env`, variáveis de ambiente
* **Saídas:** configuração consistente da aplicação
* **Relação com o PRD:** atende requisitos de manutenção e futura evolução
* **Prioridade:** MVP

### 6.8 API Layer (optional)

* **Objetivo:** expor lógica ou dados a múltiplos consumidores
* **Responsabilidades:** endpoints, autenticação adicional, serviços externos
* **Entradas:** requests externos
* **Saídas:** respostas padronizadas
* **Relação com o PRD:** não obrigatória para o MVP
* **Prioridade:** Future / Needs validation

---

## 7. Data Architecture

### Visão geral

A arquitetura de dados continuará usando o **PostgreSQL local** como fonte única de verdade. Os dados serão organizados em:

* **camada operacional**: registros brutos e padronizados;
* **camada analítica**: visões e agregações para KPIs consolidados e segmentados.

### Entidades centrais

* alunos
* receitas
* despesas
* rematrículas
* turmas / capacidade
* categorias de custo
* inadimplência (condicional)
* lotes de importação
* tabelas de taxonomia / domínio (recomendadas)

### Estratégia de modelagem

* tabelas normalizadas para dados operacionais;
* views SQL e/ou consultas analíticas para agregações;
* regras de cálculo centralizadas fora da UI;
* taxonomias separadas sempre que isso reduzir inconsistência.

### Granularidade

* dados financeiros: mensal com possibilidade de granularidade por lançamento;
* dados de alunos: por evento de entrada/saída/status;
* rematrícula: por ciclo letivo;
* ocupação: por turma;
* concessões: por aluno / por período, quando aplicável;
* indicadores: por período de referência e por recorte.

### 7.1 Conceptual Data Model

```mermaid
erDiagram
    STUDENTS ||--o{ REVENUES : has
    STUDENTS ||--o{ REMATRICULATIONS : has
    STUDENTS ||--o{ DELINQUENCIES : may_have
    STUDENTS }o--|| CLASSES : belongs_to
    CLASSES }o--|| SEGMENTS : part_of
    CLASSES }o--|| GRADE_LEVELS : part_of
    EXPENSES }o--|| COST_CATEGORIES : belongs_to
```

### 7.2 Logical Data Model

#### Tabela `students`

* `student_id`
* `student_name`
* `segment`
* `grade_level`
* `class_name`
* `student_status`
* `entry_date`
* `exit_date`
* `exit_reason`
* `tuition_amount`
* `discount_amount`
* `discount_percentage`
* `discount_band`
* `scholarship_flag`
* `scholarship_type`
* `scholarship_amount`
* `scholarship_percentage`
* `financial_status`
* `created_at`
* `updated_at`

#### Tabela `classes`

* `class_name`
* `segment`
* `grade_level`
* `class_capacity`
* `created_at`
* `updated_at`

#### Tabela `revenues`

* `revenue_id`
* `student_id`
* `reference_period`
* `expected_amount`
* `discount_amount`
* `received_amount`
* `payment_date`
* `payment_status`
* `created_at`
* `updated_at`

#### Tabela `expenses`

* `expense_id`
* `reference_period`
* `category_id`
* `subcategory`
* `amount`
* `expense_type`
* `notes`
* `created_at`
* `updated_at`

#### Tabela `cost_categories`

* `category_id`
* `category_name`
* `category_group`
* `critical_cost_flag`

#### Tabela `rematriculations`

* `rematriculation_id`
* `student_id`
* `academic_year`
* `eligible_flag`
* `rematriculated_flag`
* `rematriculation_status`
* `confirmation_date`
* `created_at`
* `updated_at`

#### Tabela `delinquencies` *(condicional)*

* `delinquency_id`
* `student_id`
* `reference_period`
* `open_amount`
* `due_date`
* `delinquency_status`
* `created_at`
* `updated_at`

#### Tabela técnica `import_batches`

* `batch_id`
* `source_type`
* `file_name`
* `processed_at`
* `status`
* `validation_notes`

#### Tabelas de domínio recomendadas *(opcional, mas desejável)*

* `segments`
* `grade_levels`
* `student_statuses`
* `rematriculation_statuses`
* `discount_bands`
* `financial_statuses`
* `exit_reasons`
* `scholarship_types`

### 7.3 Data Ownership and Source of Truth

* **Fonte de verdade:** PostgreSQL local
* **Responsável operacional pelos dados:** secretária ou operador designado, com supervisão da gestão
* **Responsável por governança dos dados:** precisa validação
* **Responsável por regras de cálculo:** camada analítica documentada na aplicação
* **Responsável por taxonomias:** precisa validação com liderança / gestão administrativa

---

## 8. Data Ingestion and Update Strategy

### Origem dos dados

1. registros manuais do dia a dia;
2. planilhas/arquivos históricos;
3. possíveis planilhas operacionais de transição.

### Mecanismos de entrada

#### A. Entrada manual simplificada

Ideal para:

* receitas;
* despesas;
* mudanças de status do aluno;
* rematrículas;
* motivos de saída;
* manutenção de turma/capacidade, se houver processo definido.

#### B. Importação estruturada de CSV/Excel

Indicada para:

* carga inicial;
* correções em lote;
* migração gradual do papel/planilhas.

#### C. Atualização programada

Usada para:

* reprocessar datasets analíticos;
* validar arquivos em diretório monitorado;
* recalcular agregações por recorte.

### Impacto do v1.1 na ingestão

A ingestão agora precisa considerar explicitamente:

* obrigatoriedade ou validação forte de `segment`, `grade_level` e `class_name`;
* validação de `student_status` e `rematriculation_status`;
* validação de `discount_band`, quando o desconto existir;
* suporte opcional a `scholarship_*`, sem assumir presença obrigatória até validação;
* suporte opcional a `class_capacity`.

### Estratégia recomendada

A abordagem mais sustentável continua sendo:

* **entrada manual simplificada para operação corrente**;
* **importação em lote para carga histórica e ajustes**;
* **atualização near-real-time do dashboard via leitura direta do banco**.

### O que será automático

* persistência imediata após envio de formulário;
* disponibilidade quase imediata no dashboard;
* reprocessamento dos KPIs sob demanda e/ou em ciclos curtos;
* validações automáticas de taxonomia e consistência básica.

### O que continuará manual

* alimentação de registros quando não houver integração externa;
* correção de inconsistências;
* classificação de motivos de saída;
* definição operacional de bolsas e capacidades, se ainda não existirem.

### O que exige validação

* taxonomia oficial de segmento/série/turma;
* regras para status do aluno;
* regras para status de rematrícula;
* política de bolsa distinta de desconto;
* capacidade por turma;
* granularidade de situação financeira.

---

## 9. Data Processing and KPI Computation

### Princípio geral

Os KPIs não devem ser calculados no frontend. A UI deve apenas consumir resultados de uma camada analítica confiável.

### Estratégia recomendada

* **agregações simples e views**: no banco;
* **regras de negócio e KPIs compostos**: em camada Python dedicada;
* **frontend**: apenas leitura, filtros e renderização.

### Organização da lógica

* `repositories`: leitura/escrita no banco
* `services`: operações de aplicação
* `analytics`: cálculo de KPIs e datasets do dashboard
* `dashboard`: visualização

### Evolução v1.1 da camada analítica

A camada analítica deve passar a suportar explicitamente:

* agregações por `segment`;
* agregações por `grade_level`;
* agregações por `class_name`;
* comparações entre recortes;
* cálculo de taxa de ocupação por turma;
* separação entre desconto e bolsa;
* cálculos condicionais quando bolsa e inadimplência estiverem disponíveis.

### Cálculo por camada

* **No banco:** views e agregações base
* **Na camada Python:** KPIs, comparativos, métricas condicionais e regras de negócio
* **No frontend:** apenas formatação, filtros e exibição

### Materialização

* MVP: views simples ou queries agregadas
* Future: materialized views, se houver necessidade de performance

### Jobs de atualização

* MVP: atualização por leitura direta e processamento leve sob demanda
* Future: jobs periódicos para snapshots e materializações mais sofisticadas

### Regras condicionais

Os seguintes cálculos devem ser tratados como **condicionais**:

* métricas de bolsa;
* inadimplência por recorte;
* margem detalhada por turma;
* alocações mais profundas de custo por turma.

---

## 10. Application Flow

1. Usuário operacional registra dados em formulários simples ou importa arquivo.
2. Camada de ingestão valida esquema mínimo e consistência básica.
3. Taxonomias e classificações são verificadas:

   * segmento
   * série/ano
   * turma
   * status
   * desconto
   * bolsa
   * motivo de saída
4. Dados válidos são persistidos no PostgreSQL local.
5. Camada analítica consulta e transforma dados operacionais.
6. KPIs consolidados e segmentados são montados.
7. Dashboard Streamlit lê os resultados e renderiza módulos e comparativos.
8. Ao novo envio de dados, o banco é atualizado e a visualização reflete o estado mais recente na próxima leitura/refresh.

---

## 11. API and Service Layer Design

### Recomendação para o MVP

**Não adotar API separada no MVP.**

### Justificativa

A nova profundidade analítica **não exige**, por si só, uma API dedicada. O principal impacto está no:

* modelo de dados;
* camada analítica;
* estrutura dos filtros;
* visualização por recorte.

Manter:

* PostgreSQL local
* SQLAlchemy
* serviços internos
* Streamlit

continua sendo suficiente para a primeira versão.

### Quando uma API passa a fazer sentido

* múltiplos consumidores além do dashboard;
* integrações externas;
* autenticação/autorização mais robusta;
* necessidade de separar frontend e backend por razões de escala ou segurança.

### Tecnologia recomendada se a API for adotada futuramente

* Flask ou FastAPI

---

## 12. Frontend / Dashboard Design Approach

### Organização geral

A interface deve continuar privilegiando leitura rápida, poucos cliques e linguagem simples.

### Estrutura recomendada

* página principal de dashboard com módulos empilhados;
* páginas internas separadas para entrada/atualização de dados;
* filtros globais no topo;
* leitura em camadas:

  * consolidado
  * recorte por segmento
  * recorte por série/ano
  * recorte por turma

### Componentes visuais

* cards executivos
* gráficos de barras, linha e composição
* tabelas resumidas
* alertas visuais
* blocos comparativos por recorte

### Módulos da interface

1. Filtros Gerais
2. Resumo Executivo
3. Alunos e Retenção
4. Visão de Receitas
5. Estrutura de Custos
6. Viabilidade e Sustentabilidade da Mensalidade
7. Concessões (Descontos e Bolsas)
8. Ocupação por Turma
9. Alertas e Ações Prioritárias
10. Entrada de Dados / Importação

### Diretrizes de UX

* evitar telas excessivas;
* evitar formulários longos;
* destacar indicadores críticos;
* manter navegação previsível;
* permitir profundidade sob demanda;
* preservar clareza mesmo com segmentação.

---

## 13. Real-Time / Near-Real-Time Strategy

### Estratégia escolhida

**Near-real-time pragmático**, não realtime pleno.

### Mecanismo

* formulários escrevem diretamente no banco;
* dashboard consulta banco em leitura direta;
* atualização refletida em novo carregamento ou refresh leve;
* jobs programados tratam importações e reprocessamentos.

### Mudança na v1.1

O aumento de recortes não exige mudança estrutural nessa estratégia, mas aumenta a importância de:

* consultas otimizadas;
* agregações bem organizadas;
* filtros eficientes;
* eventuais views de apoio.

### Limitações esperadas

* atualizações dependem de refresh ou intervalo configurado;
* importações em lote podem ter pequena latência;
* comparativos mais pesados podem exigir otimização futura.

---

## 14. Security and Access Considerations

1. Credenciais devem ficar fora do código-fonte.
2. Configurações devem ser carregadas por `.env`.
3. Acesso ao banco deve usar usuário com permissões adequadas ao ambiente local.
4. Informações sensíveis devem ser limitadas ao necessário.
5. Área de entrada/manutenção deve ser separada logicamente da leitura gerencial.
6. Campos ligados a situação financeira e concessões devem receber atenção adicional de exposição.
7. Em evolução para nuvem, autenticação e perfis de acesso podem ser reforçados com mecanismos do Supabase.
8. Logs não devem expor dados sensíveis desnecessariamente.

---

## 15. Local Development Architecture

### Estrutura sugerida do projeto

```text
project-root/
  app/
    config/
    db/
    models/
    repositories/
    services/
    analytics/
    dashboard/
    ingestion/
    jobs/
    utils/
    taxonomies/
  data/
    raw/
    processed/
    templates/
  scripts/
  tests/
  docs/
  migrations/
  .env.example
  pyproject.toml
  README.md
```

### Ambiente virtual

* usar `.venv` no projeto

### Gestão de dependências

* `pyproject.toml`
* grupos de dependências para runtime e dev

### Banco

* PostgreSQL local como padrão do MVP

### Execução local

* serviços executados localmente;
* Streamlit como aplicação principal;
* jobs acionados por script ou agendamento local.

### Ajustes locais v1.1

* novos scripts de validação de taxonomia;
* novos templates de importação com campos segmentados;
* novos testes para regras de segmentação, ocupação e concessões;
* novas migrations para campos adicionais.

### Compatibilidade com o ambiente

* compatível com MacBook informado;
* compatível com IDE moderna local;
* compatível com terminal Unix.

### Versionamento

* Git local
* GitHub remoto
* migrations, taxonomias e documentação versionadas junto ao projeto

---

## 16. Cloud Evolution Strategy

A evolução para nuvem deve ocorrer **somente após validação funcional local**.

### O que já nasce preparado

* uso de PostgreSQL como base;
* separação de configuração por variáveis de ambiente;
* organização modular da aplicação;
* camada analítica separada da UI;
* modelo de dados preparado para segmentação.

### O que pode continuar igual

* Python
* SQLAlchemy
* Alembic
* Pandas
* Streamlit
* estrutura modular
* regras de KPI
* taxonomias e validações

### O que precisaria mudar

* `DATABASE_URL`
* gestão de segredos
* estratégia de agendamento
* backup e observabilidade
* políticas de acesso
* eventual otimização de consultas segmentadas

### Como Supabase pode ajudar

* atuar como PostgreSQL gerenciado;
* reduzir esforço operacional do banco;
* oferecer storage e auth futuros;
* facilitar disponibilização em nuvem após maturidade local.

### Estratégia prudente de migração

1. validar MVP local;
2. estabilizar schema, taxonomias e KPIs;
3. migrar banco para Supabase;
4. adaptar variáveis de ambiente;
5. validar desempenho e acesso;
6. decidir se API continua desnecessária ou passa a ser útil.

---

## 17. Observability and Maintenance Strategy

### Logging

* logs simples para:

  * importações;
  * falhas de validação;
  * falhas de consulta;
  * erros de atualização;
  * falhas de taxonomia;
  * inconsistências entre bolsa e desconto.

### Monitoramento mínimo

* status dos jobs;
* registros de importação;
* erros de conexão com banco;
* falhas em consultas de KPI;
* erros de classificação de recortes;
* ausência de capacidade por turma quando necessária.

### Troubleshooting

* logs por componente;
* validação de entrada com mensagens claras;
* isolamento de lógica analítica fora da UI;
* rastreio de registros rejeitados por taxonomia inválida.

### Manutenção da base

* migrations controladas;
* categorias e taxonomias padronizadas;
* revisão periódica de consistência;
* revisão periódica de turma/capacidade.

### Manutenção dos jobs

* scripts pequenos e explícitos;
* rotinas com logs;
* frequência configurável.

### Manutenção do dashboard

* módulos independentes;
* KPIs centralizados;
* layout evolutivo sem reescrever lógica.

---

## 18. Implementation Phases

### Phase 0 — Project Bootstrap

* **Objetivo:** estruturar o projeto base
* **Entregáveis:** estrutura de diretórios, ambiente virtual, configuração inicial, documentação base
* **Dependências:** nenhuma
* **Riscos:** definição insuficiente de convenções

### Phase 1 — Local Database and Schema

* **Objetivo:** implantar banco local e schema inicial revisado
* **Entregáveis:** models, migrations, tabelas principais e novos campos de segmentação
* **Dependências:** validação inicial de entidades e taxonomias
* **Riscos:** ambiguidades de regra de negócio

### Phase 2 — Taxonomy and Data Standardization

* **Objetivo:** padronizar taxonomias e validar campos de segmentação
* **Entregáveis:** domínios, validações, templates de importação revisados
* **Dependências:** schema estável
* **Riscos:** baixa qualidade dos dados históricos

### Phase 3 — Local Ingestion and Data Standardization

* **Objetivo:** permitir entrada de dados e importação básica já com recortes
* **Entregáveis:** formulários internos, templates CSV/Excel, validações
* **Dependências:** taxonomias mínimas definidas
* **Riscos:** baixa adesão operacional

### Phase 4 — KPI Layer

* **Objetivo:** implementar lógica analítica e KPIs consolidados e segmentados
* **Entregáveis:** serviços analíticos, views, cálculos documentados
* **Dependências:** dados minimamente estruturados
* **Riscos:** divergência em fórmulas críticas

### Phase 5 — Local Dashboard MVP

* **Objetivo:** implementar o dashboard funcional com filtros segmentados
* **Entregáveis:** módulos do MVP, filtros, cards, gráficos, tabelas, alertas
* **Dependências:** KPI layer funcional
* **Riscos:** excesso de escopo na interface

### Phase 6 — Conditional Features

* **Objetivo:** incorporar componentes dependentes de validação
* **Entregáveis:** bolsas, ocupação por turma e inadimplência, quando viáveis
* **Dependências:** política mínima e dados disponíveis
* **Riscos:** priorização inadequada sem base confiável

### Phase 7 — Automation and Refinements

* **Objetivo:** reduzir retrabalho e melhorar atualização
* **Entregáveis:** jobs agendados, refresh leve, melhorias de UX
* **Dependências:** MVP estabilizado
* **Riscos:** automação prematura de fluxos ainda não padronizados

### Phase 8 — Cloud Readiness / Migration

* **Objetivo:** preparar ou executar evolução para nuvem
* **Entregáveis:** adaptação de ambiente, banco gerenciado, validação em cloud
* **Dependências:** sucesso local comprovado
* **Riscos:** migração precoce sem estabilidade funcional

---

## 19. Technical Risks and Trade-offs

### Risco 1 — Dados iniciais inconsistentes

* **Impacto:** alto
* **Mitigação:** validação de schema, importação controlada, revisão inicial
* **Relação com o PRD:** falta de base estruturada

### Risco 2 — Ambiguidade de regras de negócio

* **Impacto:** alto
* **Mitigação:** validar definições antes da implementação final dos KPIs
* **Relação com o PRD:** aluno ativo, rematrícula, ponto de equilíbrio

### Risco 3 — Resistência à adoção

* **Impacto:** alto
* **Mitigação:** interface simples, poucos passos, foco no essencial
* **Relação com o PRD:** baixa maturidade digital

### Risco 4 — Inclusão prematura de API

* **Impacto:** médio
* **Mitigação:** manter sem API no MVP
* **Relação com o PRD:** necessidade de simplicidade

### Risco 5 — Segmentação inconsistente

* **Impacto:** alto
* **Mitigação:** taxonomias controladas e validações obrigatórias
* **Relação com o PRD:** filtros e comparativos segmentados

### Risco 6 — Capacidade por turma ausente

* **Impacto:** médio/alto
* **Mitigação:** tratar ocupação como condicional até validação
* **Relação com o PRD:** módulo de ocupação

### Risco 7 — Bolsa confundida com desconto

* **Impacto:** alto
* **Mitigação:** separar modelo e validação de concessões
* **Relação com o PRD:** módulo de concessões

### Risco 8 — Frontend ficar complexo demais

* **Impacto:** médio
* **Mitigação:** leitura em camadas, poucos filtros visíveis por vez, hierarquia clara
* **Relação com o PRD:** simplicidade para baixa maturidade digital

### Trade-off 1 — Desacoplamento versus velocidade

* **Descrição:** evitar API acelera MVP, mas reduz separação inicial
* **Impacto:** aceitável no primeiro ciclo
* **Mitigação:** manter arquitetura interna modular

### Trade-off 2 — Realtime pleno versus simplicidade

* **Descrição:** near-real-time é menos sofisticado, mas muito mais sustentável
* **Impacto:** positivo para o MVP
* **Mitigação:** planejar evolução futura se necessário

### Trade-off 3 — Supabase imediato versus banco local

* **Descrição:** Supabase acelera cloud, mas antecipa dependência externa
* **Impacto:** médio
* **Mitigação:** começar com PostgreSQL local e migrar depois

### Trade-off 4 — Profundidade analítica versus simplicidade de uso

* **Descrição:** mais recortes aumentam valor, mas também podem aumentar carga cognitiva
* **Impacto:** médio
* **Mitigação:** dashboard em camadas, filtros graduais, comparativos focados

---

## 20. Open Questions / Items to Validate

### Alta criticidade

1. Definição final de aluno ativo.
2. Fórmula final de ponto de equilíbrio.
3. Fórmula final de alunos mínimos para operar.
4. Estrutura real disponível de receitas e despesas.
5. Cadastro confiável de segmento, série/ano e turma.
6. Existência e confiabilidade de capacidade por turma.
7. Política formal de bolsa distinta de desconto.
8. Responsabilidade formal pela governança dos dados.

### Média criticidade

9. Classificação final dos motivos de saída.
10. Padrão final de desconto.
11. Escopo final da folha.
12. Taxonomias de status do aluno e rematrícula.
13. Situação financeira e granularidade do seu registro.
14. Thresholds de alertas por recorte.

### Baixa criticidade

15. Necessidade futura de API.
16. Necessidade futura de materialized views.
17. Conveniência de Supabase na fase cloud.
18. Profundidade futura de comparações históricas por turma/série.

---

## 21. Traceability Matrix

| PRD Module / Requirement            | Technical Component                                | Data Dependency                        | Implementation Priority | Source Type                      |
| ----------------------------------- | -------------------------------------------------- | -------------------------------------- | ----------------------- | -------------------------------- |
| Resumo Executivo / PR-01 a PR-04    | Dashboard Layer + Analytics Layer                  | revenues, expenses, students           | MVP                     | Directly stated in PRD v1.1      |
| Estrutura de Custos / PR-05 a PR-07 | Database Layer + Analytics Layer                   | expenses, cost_categories              | MVP                     | Directly stated in PRD v1.1      |
| Viabilidade / PR-08 a PR-13         | Analytics Layer                                    | students, revenues, expenses           | MVP                     | Direct + Derived                 |
| Alunos e Retenção / PR-14 a PR-18   | Database Layer + Analytics Layer + Dashboard Layer | students, rematriculations             | MVP                     | Directly stated in PRD v1.1      |
| Filtros Gerais / PR-20 a PR-26      | Frontend Layer + Data Model                        | students, rematriculations, taxonomies | MVP                     | Directly stated in PRD v1.1      |
| Comparativos por recorte / PR-27    | Analytics Layer + Frontend Layer                   | students, revenues, aggregated views   | MVP                     | Derived from PRD v1.1            |
| Ocupação por turma / PR-28          | Database Layer + Analytics Layer                   | classes, students                      | MVP / Needs validation  | Derived from PRD v1.1            |
| Bolsa vs desconto / PR-29 a PR-31   | Taxonomy Layer + Analytics Layer                   | students, scholarship fields           | Needs validation        | Open question / Needs validation |
| Motivo de saída por recorte / PR-32 | Analytics Layer + Dashboard Layer                  | students, exit_reason                  | MVP                     | Derived from PRD v1.1            |
| Inadimplência / PR-33               | Optional component                                 | delinquencies, revenues                | Needs validation        | Open question / Needs validation |

---

## 22. Recommended Next Step

O próximo passo recomendado é:

1. validar as questões críticas em aberto do PRD/SDD;
2. aprovar formalmente a stack do MVP:

   * PostgreSQL local
   * SQLAlchemy
   * Pandas
   * Streamlit
   * sem API dedicada no MVP
3. aprovar as taxonomias mínimas da versão v1.1:

   * segmento
   * série/ano
   * turma
   * status do aluno
   * status de rematrícula
   * faixa de desconto
   * motivo de saída
   * política de bolsa, se aplicável
4. iniciar a implementação pela atualização do schema e da camada de validação;
5. estruturar dados mínimos e migrations antes de qualquer expansão visual do dashboard.
