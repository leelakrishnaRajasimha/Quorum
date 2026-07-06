import streamlit as st


def show_agent(response):

    vote = response.vote.value

    if vote == "Approve":
        color = "🟢"

    elif vote == "Modify":
        color = "🟡"

    else:
        color = "🔴"

    with st.container(border=True):

        st.subheader(f"{color} {response.agent_name}")

        st.write(f"**Vote:** {vote}")

        st.write(f"**Confidence:** {response.confidence}%")

        st.write("**Recommendation**")
        st.write(response.recommendation)

        st.write("**Finding**")
        st.write(response.finding)

        if response.concerns:

            with st.expander("Concerns"):

                for concern in response.concerns:
                    st.write("•", concern)