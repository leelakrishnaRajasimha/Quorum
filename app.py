import streamlit as st

from PIL import Image

from agents.ceo.ceo import CEOAgent
from core.models.models import StartupIdea
from frontend.components.score_card import show_agent
from frontend.components.charts import show_vote_chart, show_confidence_chart
from frontend.components.score_card import show_agent
from frontend.components.success_card import show_success
from frontend.components.financial_card import show_financial
from frontend.components.investor_card import show_investor
from frontend.components.roadmap_card import show_roadmap

from tools.report.pdf_report import generate_pdf

st.set_page_config(
    page_title="Quorum",
    page_icon="assets/logo.png",
    layout="wide"
)

from PIL import Image

logo = Image.open("assets/logo.png")

col1, col2 = st.columns([1, 6])

with col1:
    st.image(logo, width=70)

with col2:
    st.title("QUORUM")
st.subheader("AI Executive Board for Startup Due Diligence")

st.write(
    "Describe any startup idea. Quorum simulates an executive board meeting where AI executives evaluate market, finance, technology, product, marketing, and risks before giving an investment recommendation.")

provider = st.selectbox(
    "AI Provider",
    [
        "Gemini",
        "OpenAI (Coming Soon)",
        "Claude (Coming Soon)",
        "Grok (Coming Soon)",
        "NVIDIA",
        "OpenRouter (Coming Soon)"
    ]
)

title = st.text_input("Startup Name")
description = st.text_area("Describe your startup idea in detail")
budget = st.text_input("Estimated Initial Budget")
timeline = st.text_input("Expected Timeline")
target = st.text_input("Target Users")

st.caption(
    "⚠️ AI estimates are based on market assumptions and should not be treated as financial or legal advice."
)

if st.button("Conduct Board Meeting", use_container_width=True):

    idea = StartupIdea(
        title=title,
        description=description,
        budget=budget,
        timeline=timeline,
        target_users=target
    )

    ceo = CEOAgent(provider.lower())

    status = st.empty()

    progress = st.progress(0)

    status.info("🏛️ Executive Board Meeting Started...")

    completed = {"count": 0}

    def update_progress(agent_name):

        completed["count"] += 1

        progress.progress(completed["count"] / 6)

        status.info(f"✅ {agent_name} Executive Finished")

    meeting, decision, summary, scorecard, responses, success, financial, investor, roadmap = ceo.conduct_board_meeting(idea, progress_callback=update_progress)

    progress.progress(100)

    status.success("✅ Executive Board Meeting Completed")

    st.success("✅ Executive Board Meeting Completed")

    st.divider()

    st.header("Executive Board")

    col1, col2, col3 = st.columns(3)

    with col1:
        show_agent(responses[0])
        show_agent(responses[1])

    with col2:
        show_agent(responses[2])
        show_agent(responses[3])

    with col3:
        show_agent(responses[4])
        show_agent(responses[5])

    st.divider()

    st.header("Board Overview")

    kpi1, kpi2, kpi3 = st.columns(3)

    with kpi1:
        st.metric(
            "Final Decision",
            decision["decision"]
        )

    with kpi2:
        st.metric(
            "Board Confidence",
            f"{decision['confidence']}%"
            )

    with kpi3:
        st.metric(
            "Executives",
            len(responses)
        )

    st.header("Executive Analytics")

    col1, col2 = st.columns(2)

    with col1:
        show_vote_chart(decision)

    with col2:
        show_confidence_chart(responses)

    st.divider()

    st.header("Executive Scorecard")
    st.text(scorecard)

    st.divider()

    st.header("CEO Summary")
    st.write(summary)

    st.divider()

    show_success(success)

    st.divider()

    show_financial(financial)

    st.divider()

    show_investor(investor)

    st.divider()

    show_roadmap(roadmap)

    st.divider()

    import os

    os.makedirs("reports", exist_ok=True)

    pdf_path = f"reports/{title}_Executive_Report.pdf"

    generate_pdf(
        filename=pdf_path,
        startup_name=title,
        decision=decision["decision"],
        ceo_summary=summary,
        scorecard=scorecard,
        financial=financial,
        investor=investor,
        roadmap=roadmap
    )

    with open(pdf_path, "rb") as pdf_file:
        st.download_button(
            label="📄 Download Executive Report",
            data=pdf_file,
            file_name=f"{title}_Executive_Report.pdf",
            mime="application/pdf",
            )
