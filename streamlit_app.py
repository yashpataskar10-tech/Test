import time
import pandas as pd
import streamlit as st

from agents.orchestrator import ConsultantOrchestrator

st.set_page_config(
    page_title="Agentic AI Strategy Consultant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("🤖 Agentic AI Strategy Consultant")

st.sidebar.markdown("""
Generate consulting-grade business reports using AI.

### Features

✅ Live Web Research

✅ AI Market Analysis

✅ Competitor Analysis

✅ SWOT Analysis

✅ Buyer Persona Generation

✅ Strategic Recommendations

---

### Tech Stack

• Gemini 3.5 Flash Lite

• Tavily Search

• Streamlit

• Pydantic

---

Enter a company name and industry, then click **Generate Report**.
""")

company = st.sidebar.text_input(
    "Company Name",
    
)

industry = st.sidebar.text_input(
    "Industry",
    
)

generate = st.sidebar.button(
    "🚀 Generate Strategy Report",
    use_container_width=True
)

# ==========================================================
# MAIN PAGE
# ==========================================================

st.title("🤖 Agentic AI Strategy Consultant")

st.caption(
    "AI Powered Management Consulting Platform"
)

st.divider()

if generate:

    if not company or not industry:

        st.error("Please enter Company Name and Industry.")

    else:

        start = time.time()

        progress = st.progress(0)

        status = st.empty()

        try:

            status.info("🔍 Collecting Market Research...")

            progress.progress(15)

            orchestrator = ConsultantOrchestrator()

            result = orchestrator.execute(
                company,
                industry
            )

            progress.progress(100)

            end = time.time()

            research = result["research"]

            analysis = result["analysis"]

            strategy = result["strategy"]

            st.balloons()

            status.success("✅ Report Generated Successfully")

            st.success(
                f"Execution Time: {round(end-start,2)} seconds"
            )

            st.divider()

            # ======================================================
            # KPI CARDS
            # ======================================================

            c1, c2, c3, c4 = st.columns(4)

            c1.metric(
                "Technologies",
                len(research.technologies)
            )

            c2.metric(
                "Competitors",
                len(analysis.competitors)
            )

            c3.metric(
                "Buyer Personas",
                len(analysis.buyer_personas)
            )

            c4.metric(
                "KPIs",
                len(strategy.kpis)
            )

            st.divider()

            tabs = st.tabs(
                [
                    "📊 Executive Summary",
                    "📈 Research",
                    "🔍 Analysis",
                    "🚀 Strategy",
                    "📄 Downloads"
                ]
            )

            # ======================================================
            # TAB 1
            # ======================================================

            with tabs[0]:

                st.header(company)

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Industry",
                        research.industry
                    )

                    st.metric(
                        "Market Size",
                        research.market_size
                    )

                with col2:

                    st.metric(
                        "Growth Rate",
                        research.growth_rate
                    )

                    st.metric(
                        "Technologies",
                        len(research.technologies)
                    )

                st.divider()

                st.subheader("Company Overview")

                st.write(
                    research.company_overview
                )

                st.subheader("Industry Overview")

                st.write(
                    research.industry_overview
                )

            # ======================================================
            # TAB 2
            # ======================================================

            with tabs[1]:

                left, right = st.columns(2)

                with left:

                    st.subheader("Market Trends")

                    for trend in research.trends:

                        st.success(trend)

                    st.subheader("Technologies")

                    for tech in research.technologies:

                        st.info(tech)

                with right:

                    st.subheader("Opportunities")

                    for item in research.opportunities:

                        st.success(item)

                    st.subheader("Challenges")

                    for item in research.challenges:

                        st.warning(item)
    
            # ======================================================
            # TAB 3
            # ======================================================

            with tabs[2]:

                st.header("Business Analysis")

                swot_col1, swot_col2 = st.columns(2)

                with swot_col1:

                    st.subheader("💪 Strengths")

                    for item in analysis.strengths:

                        st.success(item)

                    st.subheader("🚀 Opportunities")

                    for item in analysis.opportunities:

                        st.info(item)

                with swot_col2:

                    st.subheader("⚠ Weaknesses")

                    for item in analysis.weaknesses:

                        st.warning(item)

                    st.subheader("🔴 Threats")

                    for item in analysis.threats:

                        st.error(item)

                st.divider()

                st.subheader("Competitor Analysis")

                competitor_df = pd.DataFrame(

                    [

                        {

                            "Competitor": competitor.name,

                            "Position": competitor.position,

                            "Strengths": competitor.strengths,

                            "Weaknesses": competitor.weaknesses

                        }

                        for competitor in analysis.competitors

                    ]

                )

                st.dataframe(

                    competitor_df,

                    use_container_width=True,

                    hide_index=True

                )

                st.divider()

                st.subheader("Customer Segments")

                for segment in analysis.customer_segments:

                    st.markdown(f"✅ {segment}")

                st.divider()

                st.subheader("Buyer Personas")

                for persona in analysis.buyer_personas:

                    with st.expander(f"👤 {persona.title}"):

                        st.markdown("### Goals")

                        st.write(persona.goals)

                        st.markdown("### Pain Points")

                        st.write(persona.pain_points)

                        st.markdown("### Decision Factors")

                        st.write(persona.decision_factors)

                st.divider()

                st.success(
                    f"{len(analysis.competitors)} competitors analysed successfully."
                )

            # ======================================================
            # TAB 4
            # ======================================================

            with tabs[3]:

                st.header("Strategic Recommendations")

                st.subheader("Strategic Objectives")

                for objective in strategy.strategic_objectives:

                    st.markdown(f"✅ {objective}")

                st.divider()

                st.subheader("Growth Strategy")

                st.info(

                    strategy.growth_strategy

                )

                st.divider()

                st.subheader("Go-To-Market Strategy")

                st.write(

                    strategy.go_to_market

                )

                st.divider()

                st.subheader("Implementation Roadmap")

                roadmap_df = pd.DataFrame(

                    {

                        "Phase": [

                            f"Phase {i+1}"

                            for i in range(

                                len(strategy.implementation_plan)

                            )

                        ],

                        "Activity": strategy.implementation_plan

                    }

                )

                st.dataframe(

                    roadmap_df,

                    use_container_width=True,

                    hide_index=True

                )

                st.divider()

                st.subheader("Key Performance Indicators")

                for kpi in strategy.kpis:

                    st.success(kpi)

                st.divider()

                st.subheader("Conclusion")

                st.success(

                    strategy.conclusion

                )
                
            # ======================================================
            # TAB 5
            # ======================================================

            with tabs[4]:

                st.header("Downloads")

                md_path = (
                    f"outputs/{company.replace(' ', '_')}_Strategy_Report.md"
                )

                pdf_path = result["pdf_path"]

                col1, col2 = st.columns(2)

                with col1:

                    st.subheader("Markdown Report")

                    with open(md_path, "rb") as file:

                        st.download_button(

                            label="⬇ Download Markdown",

                            data=file,

                            file_name=f"{company}_Strategy_Report.md",

                            mime="text/markdown",

                            use_container_width=True

                        )

                with col2:

                    st.subheader("PDF Report")

                    with open(pdf_path, "rb") as file:

                        st.download_button(

                            label="⬇ Download PDF",

                            data=file,

                            file_name=f"{company}_Strategy_Report.pdf",

                            mime="application/pdf",

                            use_container_width=True

                        )

                st.divider()

                st.success("✅ Report generation completed successfully.")

                st.info(
                    "You can download both the Markdown and PDF versions of the report."
                )

        except Exception as e:

            progress.empty()

            status.empty()

            st.error("❌ Report generation failed.")

            st.exception(e)

else:

    st.info(
        """
### Welcome!

This application generates AI-powered consulting reports using:

- 🔍 Live market research
- 📊 Business analysis
- 🏢 Competitor analysis
- 👥 Buyer persona generation
- 🚀 Strategic recommendations
- 📄 Markdown and PDF reports

To begin:

1. Enter a company name.
2. Enter its industry.
3. Click **Generate Strategy Report**.
"""
    )

st.divider()

st.caption(
    "Built with ❤️ using Streamlit, Gemini, Tavily, and Pydantic"
)