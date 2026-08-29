"""
RazorGrow AI: Intelligent Merchant Growth Agent
------------------------------------------------
A Streamlit demo app built for the Razorpay AI Builder Internship 2026
(Track 1: AI Growth & Agentic Commerce).

Run locally with:
    streamlit run app.py
"""

import streamlit as st
import pandas as pd
from recommender import load_data, build_co_purchase_map, get_recommendations, generate_pitch

st.set_page_config(page_title="RazorGrow AI", page_icon="📈", layout="centered")

st.title("🛍️ RazorGrow AI")
st.subheader("Intelligent Merchant Growth Agent")
st.write(
    "I built this tool to help small merchants understand what their "
    "customers are buying together. Based on that pattern, it suggests "
    "what to recommend next to a customer — either a better version of "
    "the product they're buying (**upsell**), or something that goes "
    "well with it (**cross-sell**) — so merchants can increase their "
    "revenue with smarter, more personalized suggestions."
)

# Load data + build recommendation map
df = load_data("data/sample_data.csv")
co_map = build_co_purchase_map(df)

st.markdown("---")
st.markdown("### 🛒 Try it: Simulate a customer purchase")

products = sorted(df["product_bought"].unique())
selected_product = st.selectbox("Customer is currently buying:", products)

if st.button("Get AI Recommendations"):
    recs = get_recommendations(selected_product, co_map, df)
    pitch_lines = generate_pitch(selected_product, recs)

    st.markdown("#### 🤖 RazorGrow AI Assistant says:")
    for line in pitch_lines:
        st.info(line)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**⬆️ Upsell Suggestions**")
        if recs["upsell"]:
            st.table(pd.DataFrame(recs["upsell"]))
        else:
            st.write("None found.")
    with col2:
        st.markdown("**🔁 Cross-sell Suggestions**")
        if recs["cross_sell"]:
            st.table(pd.DataFrame(recs["cross_sell"]))
        else:
            st.write("None found.")

st.markdown("---")
st.markdown("### 📊 Underlying purchase data")
with st.expander("View sample transaction dataset"):
    st.dataframe(df)

st.markdown("---")
st.caption(
    "Built by Khushboo Kumari for Razorpay AI Builder Internship 2026 · "
    "Track 1: AI Growth & Agentic Commerce"
)
