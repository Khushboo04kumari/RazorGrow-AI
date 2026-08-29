# RazorGrow AI: Intelligent Merchant Growth Agent

**Track:** Track 1 — AI Growth & Agentic Commerce
**Submission for:** Razorpay AI Builder Internship 2026

## 🎯 Problem Statement
Small and medium merchants often don't have the resources to analyze
customer buying patterns manually. As a result, they miss out on
upselling (recommending a higher-value alternative) and cross-selling
(recommending a complementary product) opportunities that could
significantly boost revenue.

## 💡 Solution
**RazorGrow AI** is an AI-powered merchant growth agent that analyzes
product and customer purchase behavior to automatically recommend
personalized upselling and cross-selling opportunities. It acts as a
lightweight, conversational purchase assistant — helping merchants
increase revenue through intelligent, data-driven product
recommendations at checkout.

## ⚙️ How It Works
1. The app loads historical transaction data (`data/sample_data.csv`)
   containing which customers bought which products together.
2. It builds a **co-purchase map** — a record of how often each pair
   of products has been bought together across all customers
   (a simplified market basket analysis).
3. When a merchant selects a product a customer is currently buying,
   the AI agent recommends:
   - **Upsell suggestions** — related, higher-value products
   - **Cross-sell suggestions** — related, complementary products
4. These are presented as friendly, conversational recommendations,
   simulating how an AI sales assistant would speak to a merchant.

**Example:** If a customer is buying a **Phone Case**, the app notices
that many past customers who bought a Phone Case also bought a
**Screen Protector** (cross-sell, cheaper/complementary) and sometimes
upgraded to a **Wireless Charger** (upsell, higher value).

## 🛠️ Tech Stack
- **Python 3**
- **Streamlit** — for the interactive web app / UI
- **Pandas** — for data processing and analysis
- Core recommendation logic is custom-built (co-occurrence based
  market basket analysis) — no external paid API required, so it runs
  fully offline and free of cost.

## 🚀 How to Run Locally
```bash
# 1. Clone this repository
git clone https://github.com/<your-username>/RazorGrow-AI.git
cd RazorGrow-AI

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```
The app will open automatically in your browser at `http://localhost:8501`.

## 🌐 Live Demo
[Add your deployed Streamlit Cloud link here after deployment]

## 🧩 Build Challenges & Technical Obstacles
- **Challenge:** Deciding how to generate meaningful recommendations
  without access to a large real-world dataset or a paid AI API.
  **Solution:** Built a custom co-purchase (market basket) analysis
  algorithm using Pandas that identifies which products are frequently
  bought together, and used that as the recommendation logic —
  making the app free to run and fully explainable.
- **Challenge:** Distinguishing between "upsell" (pricier item) and
  "cross-sell" (complementary item) automatically.
  **Solution:** Compared the price of the related product to the
  current product's price — if higher, it's classified as an upsell;
  otherwise, a cross-sell.
- **Challenge:** Making the recommendations feel conversational rather
  than a plain data table.
  **Solution:** Added a `generate_pitch()` function that converts the
  raw recommendation data into natural-language suggestions, similar
  to what a sales assistant might say.

## 📂 Project Structure
```
RazorGrow-AI/
├── app.py                # Streamlit web app (UI)
├── recommender.py        # Core recommendation logic
├── data/
│   └── sample_data.csv   # Sample merchant transaction data
├── requirements.txt
└── README.md
```

## 🔮 Future Improvements
- Connect to live merchant transaction data via Razorpay APIs
- Add a true conversational chatbot interface using an LLM
- Include collaborative filtering for personalization per customer
- A/B test recommendation impact on actual revenue
