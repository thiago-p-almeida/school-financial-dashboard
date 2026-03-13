import sys
import os
import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime

# 1. Configuração de Caminhos e Imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.services.analytics import SchoolAnalytics
from src.services.ingestion import DataIngestionService

# 2. Configuração da Página
st.set_page_config(
    page_title="Gestão Escolar Pro", 
    page_icon="🎓", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicialização dos Serviços
@st.cache_resource
def get_services():
    return SchoolAnalytics(), DataIngestionService()

analytics, ingestor = get_services()

# --- 3. SIDEBAR (FILTROS E PARÂMETROS) ---
st.sidebar.header("🔍 Filtros de Visualização")

# Coleta dados base para os filtros
df_all_active = analytics.get_active_students_df()

if not df_all_active.empty:
    selected_segments = st.sidebar.multiselect(
        "Selecione o Segmento:",
        options=sorted(df_all_active['segment'].unique()),
        default=sorted(df_all_active['segment'].unique())
    )

    df_filtered_step1 = df_all_active[df_all_active['segment'].isin(selected_segments)]
    
    selected_grades = st.sidebar.multiselect(
        "Selecione a Série:",
        options=sorted(df_filtered_step1['grade'].unique()),
        default=sorted(df_filtered_step1['grade'].unique())
    )
    df_final = df_filtered_step1[df_filtered_step1['grade'].isin(selected_grades)]
else:
    df_final = df_all_active

# --- SEÇÃO DE FORECASTING NA SIDEBAR ---
st.sidebar.markdown("---")
st.sidebar.header("🔮 Parâmetros de Projeção")
delinquency = st.sidebar.slider(
    "Taxa de Inadimplência Estimada (%)", 
    min_value=0, 
    max_value=50, 
    value=10,
    help="Redutor aplicado sobre a receita bruta para prever o risco de caixa."
) / 100

months_to_forecast = st.sidebar.number_input(
    "Meses de Projeção", 
    min_value=1, 
    max_value=24, 
    value=6
)

# Coleta de dados de Churn (Visão Histórica)
churn_data = analytics.get_churn_analysis()

# --- 4. DASHBOARD UI ---
st.title("🎓 Gestão Escolar Inteligente")
st.markdown(f"Análise baseada em **{len(df_all_active)}** alunos ativos no sistema.")

# Organização por Tabs (Nível Analytics Engineer)
tab_fin, tab_retencao, tab_forecast, tab_admin = st.tabs([
    "💰 Análise Financeira", 
    "📉 Retenção e Churn", 
    "🔮 Projeção (Forecasting)",
    "⚙️ Admin/Ingestão"
])

# --- ABA 1: FINANCEIRO ---
with tab_fin:
    st.subheader("Performance Financeira e Segmentação")
    
    if df_final.empty:
        st.warning("Nenhum dado disponível para os filtros selecionados.")
    else:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Alunos no Filtro", len(df_final))
        with col2:
            ticket = df_final['net_tuition'].mean()
            st.metric("Ticket Médio Real", f"R$ {ticket:,.2f}")
        with col3:
            total_receita = df_final['net_tuition'].sum()
            st.metric("Receita Líquida Prevista", f"R$ {total_receita:,.2f}")

        st.markdown("---")
        c1, c2 = st.columns(2)
        with c1:
            st.write("#### Receita por Série")
            fig_grade = px.bar(
                df_final.groupby('grade')['net_tuition'].sum().reset_index(),
                x='grade', y='net_tuition', color='grade',
                labels={'net_tuition': 'Receita (R$)', 'grade': 'Série'},
                template="plotly_white"
            )
            st.plotly_chart(fig_grade, use_container_width=True)
        with c2:
            st.write("#### Ocupação por Turma")
            fig_class = px.pie(
                df_final, names='classroom', hole=0.4,
                color_discrete_sequence=px.colors.qualitative.Pastel
            )
            st.plotly_chart(fig_class, use_container_width=True)

# --- ABA 2: RETENÇÃO ---
with tab_retencao:
    st.subheader("Saúde da Base e Análise de Evasão")
    kpi1, kpi2, kpi3 = st.columns(3)
    with kpi1:
        st.metric("Taxa de Retenção", f"{100 - churn_data['churn_rate']:.1f}%")
    with kpi2:
        st.metric("Alunos Inativos", churn_data['total_inativos'], delta_color="inverse")
    with kpi3:
        st.metric("Taxa de Churn", f"{churn_data['churn_rate']:.1f}%")

    st.markdown("---")
    col_churn1, col_churn2 = st.columns(2)
    with col_churn1:
        st.write("#### Motivos de Saída")
        if not churn_data['reasons_df'].empty:
            fig_reasons = px.pie(
                churn_data['reasons_df'], values='Quantidade', names='Motivo',
                color_discrete_sequence=px.colors.sequential.RdBu_r
            )
            st.plotly_chart(fig_reasons, use_container_width=True)
        else:
            st.info("Nenhuma evasão registrada.")
    with col_churn2:
        st.write("#### 💡 Insights")
        st.info(f"""
            * Alunos Ativos Atuais: **{churn_data['total_ativos']}**
            * Ponto de atenção: O motivo principal de saída é **'{churn_data['reasons_df'].iloc[0]['Motivo'] if not churn_data['reasons_df'].empty else 'N/A'}'**.
        """)

# --- ABA 3: FORECASTING (TB-026) ---
with tab_forecast:
    st.subheader("Projeção de Fluxo de Caixa Futuro")
    st.markdown("Simulação baseada na base de alunos ativos e taxa de risco selecionada.")
    
    df_forecast = analytics.get_financial_forecasting(
        months=months_to_forecast, 
        delinquency_rate=delinquency
    )
    
    if not df_forecast.empty:
        fig_forecast = px.area(
            df_forecast, 
            x="Mês", 
            y=["Receita Projetada (Líquida)", "Risco de Inadimplência"],
            title=f"Expectativa de Receita para {months_to_forecast} meses",
            color_discrete_map={
                "Receita Projetada (Líquida)": "#2ecc71",
                "Risco de Inadimplência": "#e74c3c"
            },
            template="plotly_white"
        )
        st.plotly_chart(fig_forecast, use_container_width=True)
        
        st.markdown("#### Planilha de Projeção")
        st.dataframe(
            df_forecast.style.format({
                "Receita Bruta": "R$ {:,.2f}",
                "Receita Projetada (Líquida)": "R$ {:,.2f}",
                "Risco de Inadimplência": "R$ {:,.2f}"
            }), 
            use_container_width=True
        )

        # SEÇÃO DE EXPORTAÇÃO (NOVO)
        st.markdown("---")
        st.subheader("📤 Exportar Análise")
        
        col_exp1, col_exp2 = st.columns(2)
        
        with col_exp1:
            try:
                # Geramos o arquivo Excel em memória
                excel_data = analytics.to_excel(df_forecast)
                st.download_button(
                    label="📥 Baixar Projeção em Excel",
                    data=excel_data,
                    file_name=f"projecao_financeira_{datetime.now().strftime('%Y%m%d')}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
                st.caption("Gera um arquivo .xlsx com o detalhamento mês a mês.")
            except Exception as e:
                st.error(f"Erro ao preparar download: {e}")

        with col_exp2:
            st.button("📄 Gerar Relatório PDF (Em breve)", disabled=True)
            st.caption("O módulo de PDF requer bibliotecas adicionais de renderização.")

    else:
        st.warning("Não há alunos ativos para gerar a projeção financeira.")

# --- ABA 4: ADMIN/INGESTÃO ---
with tab_admin:
    st.subheader("⚙️ Central de Ingestão de Dados")
    st.markdown("Carregar novos alunos via arquivo CSV.")
    
    with st.expander("Ver formato de arquivo aceito"):
        st.write("O CSV deve conter: `name`, `segment`, `grade`, `full_tuition`, `discount_value`, `scholarship_value`")
    
    uploaded_file = st.file_uploader("Escolha o arquivo CSV de alunos", type="csv")
    
    if uploaded_file is not None:
        if st.button("🚀 Processar Importação"):
            try:
                msg = ingestor.process_students_csv(uploaded_file, uploaded_file.name)
                st.success(msg)
                st.cache_resource.clear()
                st.rerun() 
            except Exception as e:
                st.error(f"Erro crítico na importação: {e}")