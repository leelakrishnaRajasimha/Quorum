import streamlit as st
import re


def show_financial(financial_text):

    st.subheader("💰 Financial Projection")

    money = re.findall(r'₹\s?[\d.,]+\s?(?:Lakh|Lakhs|Crore|Crores|Million|Billion)?', financial_text)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "💵 MVP Cost",
            money[0] if len(money) > 0 else "N/A"
        )

    with col2:
        st.metric(
            "🔥 Burn Rate",
            money[1] if len(money) > 1 else "N/A"
        )

    with col3:
        st.metric(
            "📈 Revenue",
            money[2] if len(money) > 2 else "N/A"
        )

    st.write(financial_text)