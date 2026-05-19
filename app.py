import streamlit as st
from recommender import hybrid_recommend

st.set_page_config(page_title="DevStack AI", layout="wide")

# ---------- GLOBAL CSS ----------
st.markdown("""
<style>
body {
    background: #0f172a;
    color: white;
}

.card {
    padding:20px;
    border-radius:16px;
    background:rgba(255,255,255,0.05);
    border:1px solid rgba(255,255,255,0.1);
    margin-bottom:20px;
    box-shadow:0 0 15px rgba(56,189,248,0.15);
}
.tag {
    background:#2563eb;
    padding:5px 10px;
    border-radius:999px;
    color:white;
    margin-right:6px;
    font-size:12px;
}
.tag2 {
    background:#374151;
    padding:5px 10px;
    border-radius:999px;
    color:white;
    font-size:12px;
}

/* Better label styling */
label {
    color: white !important;
    font-weight: 600 !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown("""
<h1>DevStack AI</h1>
<p style="color:#94a3b8;">Generate developer project techstack blueprints using AI</p>
""", unsafe_allow_html=True)

# ---------- INPUT ----------
col1, col2, col3 = st.columns([3,1,1])

with col1:
    query = st.text_input(
        "Project Idea",
        placeholder="Describe your idea..."
    )

with col2:
    domain = st.selectbox(
        "Domain",
        ["Any","Web Dev","AIML","Data Scientist","Mobile Dev","App Dev"]
    )

with col3:
    level = st.selectbox(
        "Difficulty Level",
        ["Any","Beginner","Intermediate","Advanced"]
    )

generate = st.button("⚡ Generate")

# ---------- RESULTS ----------
if generate:
    if not query.strip():
        st.warning("Enter your idea first")
    else:
        results = hybrid_recommend(query, domain, level)

        st.markdown("## Recommended Blueprints")

        cols = st.columns(3)

        for i, (_, row) in enumerate(results.iterrows()):
            with cols[i % 3]:
                st.markdown(f"""
<div class="card">
<h3>#{i+1} {row['project_type']}</h3>

<div>
<span class="tag">{row['domain']}</span>
<span class="tag2">{row['level']}</span>
</div>

<div style="margin-top:10px;">
<b>⚙ Tech Stack:</b><br>
<span style="color:#cbd5e1;">{row['recommended_stack']}</span>
</div>

<div style="margin-top:10px;color:#94a3b8;">
Matches your idea: <i>{query}</i>
</div>

</div>
""", unsafe_allow_html=True)