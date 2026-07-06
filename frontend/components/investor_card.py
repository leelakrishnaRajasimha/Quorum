import streamlit as st


def show_investor(text):

    st.subheader("📈 Investor Recommendation")

    upper = text.upper()

    if "DO NOT INVEST" in upper:
        st.error("🔴 DO NOT INVEST")

    elif "INVEST" in upper:
        st.success("🟢 INVEST")

    else:
        st.warning("🟡 NEEDS IMPROVEMENT")

    st.write(text)