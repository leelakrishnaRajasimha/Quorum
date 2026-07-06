import plotly.express as px
import streamlit as st


def show_vote_chart(decision):

    votes = {
        "Approve": decision["approve"],
        "Modify": decision["modify"],
        "Reject": decision["reject"]
    }

    fig = px.pie(
        names=list(votes.keys()),
        values=list(votes.values()),
        title="Executive Vote Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

import plotly.graph_objects as go

def show_confidence_chart(responses):

    names = [r.agent_name for r in responses]
    confidence = [r.confidence for r in responses]

    fig = go.Figure(
        go.Bar(
            x=names,
            y=confidence,
            text=confidence,
            textposition="outside"
        )
    )

    fig.update_layout(
        title="Executive Confidence",
        yaxis_title="Confidence %",
        xaxis_title="Executives"
    )

    st.plotly_chart(fig, use_container_width=True)