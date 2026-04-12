import streamlit as st
from recommender import hybrid_recommend

st.set_page_config(
    page_title="DevStack AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #081225 0%, #0f172a 45%, #111827 100%);
    color: white;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1250px;
}

.hero {
    padding: 28px 30px;
    border-radius: 24px;
    background: linear-gradient(135deg, rgba(37,99,235,0.95), rgba(124,58,237,0.95));
    box-shadow: 0 12px 35px rgba(0,0,0,0.28);
    margin-bottom: 22px;
    border: 1px solid rgba(255,255,255,0.08);
}

.hero h1 {
    margin: 0;
    font-size: 2.3rem;
    color: white;
}

.hero p {
    margin-top: 10px;
    font-size: 1rem;
    color: #e5e7eb;
}

.glass {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.10);
    backdrop-filter: blur(14px);
    border-radius: 22px;
    padding: 22px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.22);
}

.section-title {
    font-size: 1.15rem;
    font-weight: 700;
    margin-bottom: 10px;
    color: white;
}

.result-card {
    background: linear-gradient(145deg, rgba(255,255,255,0.06), rgba(255,255,255,0.03));
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 22px;
    padding: 22px;
    margin-bottom: 18px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.22);
}

.result-card h3 {
    margin: 0 0 8px 0;
    color: white;
    font-size: 1.6rem;
}

.muted {
    color: #cbd5e1;
    font-size: 0.95rem;
    margin-bottom: 12px;
}

.badge {
    display: inline-block;
    padding: 7px 14px;
    border-radius: 999px;
    font-size: 0.82rem;
    font-weight: 600;
    margin-right: 8px;
    margin-bottom: 10px;
    color: white;
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
}

.stack-tag {
    display: inline-block;
    padding: 7px 12px;
    border-radius: 999px;
    font-size: 0.80rem;
    font-weight: 500;
    margin: 5px 8px 0 0;
    color: #e0ecff;
    background: rgba(59,130,246,0.16);
    border: 1px solid rgba(96,165,250,0.30);
}

.why-box {
    margin-top: 16px;
    padding: 14px 16px;
    background: rgba(15,23,42,0.55);
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,0.06);
    color: #e5e7eb;
    line-height: 1.6;
}

.small-box {
    margin-top: 14px;
    display: inline-block;
    padding: 10px 14px;
    border-radius: 14px;
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    color: #cbd5e1;
    font-size: 0.9rem;
    margin-right: 10px;
}

.stTextArea textarea, .stSelectbox div[data-baseweb="select"] > div {
    background-color: rgba(255,255,255,0.04) !important;
    color: white !important;
    border-radius: 14px !important;
    border: 1px solid rgba(255,255,255,0.10) !important;
}

.stButton > button {
    width: 100%;
    border: none;
    border-radius: 14px;
    padding: 0.8rem 1rem;
    font-weight: 700;
    color: white;
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    box-shadow: 0 10px 20px rgba(37,99,235,0.25);
}

.stButton > button:hover {
    filter: brightness(1.08);
}

hr.custom-line {
    border: none;
    border-top: 1px solid rgba(255,255,255,0.08);
    margin: 14px 0;
}
</style>
""", unsafe_allow_html=True)


def split_stack(stack_text: str):
    if not isinstance(stack_text, str):
        return []
    items = [item.strip() for item in stack_text.replace("/", ",").split(",")]
    cleaned = [x for x in items if x]
    if cleaned:
        return cleaned
    return stack_text.split()


def domain_icon(domain: str):
    icons = {
        "Web Dev": "🌐",
        "AIML": "🤖",
        "Data Analyst": "📊",
        "Data Engineer": "⚙️",
        "Data Scientist": "🧠",
        "Mobile Dev": "📱",
        "App Dev": "💻"
    }
    return icons.get(domain, "🚀")


# ---------- Hero ----------
st.markdown("""
<div class="hero">
    <h1>🚀 DevStack AI</h1>
    <p>Advanced hybrid recommender for project ideas, domains, levels, and complete tech stack suggestions.</p>
</div>
""", unsafe_allow_html=True)

left, right = st.columns([1, 1.7], gap="large")

# ---------- Left Panel ----------
with left:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🎯 Project Input</div>', unsafe_allow_html=True)

    query = st.text_area(
        "Describe your idea",
        placeholder="Example: I want to build a real-time AI chatbot for students",
        height=150
    )

    domain = st.selectbox(
        "Choose domain",
        ["Any", "Web Dev", "AIML", "Data Analyst", "Data Engineer", "Data Scientist", "Mobile Dev", "App Dev"]
    )

    level = st.selectbox(
        "Choose level",
        ["Any", "Beginner", "Intermediate", "Advanced"]
    )

    top_n = st.slider("Number of recommendations", 1, 5, 3)

    recommend_btn = st.button("✨ Generate Recommendations")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Right Panel ----------
with right:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">📌 Recommendations</div>', unsafe_allow_html=True)

    if recommend_btn:
        if not query.strip():
            st.warning("Please enter your project idea first.")
        else:
            with st.spinner("Analyzing your project idea..."):
                results = hybrid_recommend(query, domain, level, top_n=top_n)

            if results is None or len(results) == 0:
                st.error("No recommendations found.")
            else:
                for idx, (_, row) in enumerate(results.iterrows(), start=1):
                    stack_items = split_stack(row["recommended_stack"])
                    stack_html = "".join(
                        [f"<span class='stack-tag'>{item}</span>" for item in stack_items]
                    )

                    icon = domain_icon(str(row["domain"]))

                    st.markdown(f"""
                    <div class="result-card">
                        <h3>{icon} #{idx} {row['project_type']}</h3>
                        <div class="muted">Smart match based on your input, selected filters, and hybrid scoring.</div>

                        <span class="badge">{row['domain']}</span>
                        <span class="badge">{row['level']}</span>

                        <hr class="custom-line"/>

                        <div style="font-weight:700; margin-bottom:8px;">⚙️ Recommended Stack</div>
                        <div>{stack_html}</div>

                        <div class="why-box">
                            <b>💡 Why this recommendation?</b><br>
                            This project is relevant to <b>{row['domain']}</b>, fits the
                            <b>{row['level']}</b> level, and matches your idea:
                            <i>{query}</i>.
                        </div>

                        <div class="small-box"><b>Domain:</b> {row['domain']}</div>
                        <div class="small-box"><b>Level:</b> {row['level']}</div>
                    </div>
                    """, unsafe_allow_html=True)
    else:
        st.info("Enter your project idea and click generate to see recommendations.")

    st.markdown('</div>', unsafe_allow_html=True)