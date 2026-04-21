import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Pricing System", layout="wide")

# ===== 🌙 深色科技风UI =====
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.big-title {
    color: #9FE870;
    font-size: 36px;
    font-weight: bold;
}
.card {
    background-color: #1c1f26;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 0px 10px rgba(0,0,0,0.5);
}
.metric {
    color: #9FE870;
    font-size: 32px;
    font-weight: bold;
}
.small-text {
    color: #AAAAAA;
}
</style>
""", unsafe_allow_html=True)

# ===== 🎯 标题 =====
st.markdown("<div class='big-title'>🚀 AI-Powered Pricing Decision System</div>", unsafe_allow_html=True)
st.markdown("<div class='small-text'>Real-time pricing optimization based on demand, elasticity and market conditions</div>", unsafe_allow_html=True)

st.markdown("---")

# ===== 📊 左侧输入 =====
st.sidebar.header("⚙️ Scenario Settings")

demand_level = st.sidebar.selectbox("Visitor Demand", ["Low", "Medium", "High"])
weather = st.sidebar.selectbox("Weather", ["Sunny", "Rainy"])
holiday = st.sidebar.selectbox("Holiday", ["No", "Yes"])
sensitivity = st.sidebar.selectbox("Price Sensitivity", ["Low", "High"])

# ===== 🧠 模型逻辑 =====
base = 500

if demand_level == "Low":
    demand = base * 0.7
elif demand_level == "Medium":
    demand = base
else:
    demand = base * 1.5

if weather == "Rainy":
    demand *= 0.7

if holiday == "Yes":
    demand *= 1.4

willingness = 180 if sensitivity == "High" else 260

def revenue(price):
    prob = 1 / (1 + np.exp((price - willingness)/20))
    return price * demand * prob

prices = np.arange(100, 300, 5)
revenues = [revenue(p) for p in prices]

best_price = prices[np.argmax(revenues)]
best_revenue = max(revenues)

baseline_revenue = revenue(180)
lift = (best_revenue - baseline_revenue) / baseline_revenue * 100

# ===== 📈 第一行 =====
col1, col2 = st.columns([2,1])

# 客流预测
with col1:
    st.markdown("### 📊 Visitor Flow Prediction")
    flow = [400, 420, 450, 500, 480, 550, 600]

    fig, ax = plt.subplots()
    ax.plot(flow)
    ax.fill_between(range(len(flow)), flow, alpha=0.3)
    ax.set_xticks(range(7))
    ax.set_xticklabels(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
    st.pyplot(fig)

# 定价卡片
with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 💰 Recommended Price")
    st.markdown(f"<div class='metric'>¥ {best_price}</div>", unsafe_allow_html=True)

    st.markdown("### 📈 Revenue")
    st.markdown(f"<div class='metric'>{int(best_revenue):,}</div>", unsafe_allow_html=True)

    st.markdown("### 🚀 Revenue Lift")
    st.markdown(f"<div class='metric'>+{lift:.1f}%</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ===== 📉 第二行 =====
col3, col4 = st.columns(2)

# 收入曲线
with col3:
    st.markdown("### 📊 Revenue vs Price")

    fig2, ax2 = plt.subplots()
    ax2.plot(prices, revenues)
    ax2.axvline(best_price, linestyle="--")
    ax2.set_xlabel("Price")
    ax2.set_ylabel("Revenue")
    st.pyplot(fig2)

# 决策解释（核心加分🔥）
with col4:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 🧠 Decision Explanation")

    explanation = []

    if demand_level == "High":
        explanation.append("High demand → increase price")

    if holiday == "Yes":
        explanation.append("Holiday effect → higher willingness to pay")

    if weather == "Rainy":
        explanation.append("Bad weather → demand drops")

    if sensitivity == "High":
        explanation.append("High price sensitivity → lower optimal price")

    for e in explanation:
        st.markdown(f"- {e}")

    st.markdown("<br><b>Key Drivers:</b> Demand · Elasticity · Benchmark", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ===== 🧱 底部模块 =====
st.markdown("---")

col5, col6, col7 = st.columns(3)

with col5:
    st.markdown("### 🧱 System Architecture")
    st.markdown("Data → Model → Application")

with col6:
    st.markdown("### 🔄 Workflow")
    st.markdown("Data → Prediction → Pricing → Execution")

with col7:
    st.markdown("### ⚡ Core Capabilities")
    st.markdown("Real-time · Optimization · Explainable AI")