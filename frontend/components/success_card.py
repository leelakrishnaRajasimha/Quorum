import streamlit as st
import re


def show_success(success_text):

    st.subheader("🎯 Startup Success Prediction")

    match = re.search(r'(\d+)', success_text)

    if match:
        probability = int(match.group(1))

        st.progress(probability / 100)

        if probability >= 70:
            st.success(f"Estimated Success Probability: {probability}%")

        elif probability >= 40:
            st.warning(f"Estimated Success Probability: {probability}%")

        else:
            st.error(f"Estimated Success Probability: {probability}%")

    st.write(success_text)