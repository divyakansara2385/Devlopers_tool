import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("dataset/developer_dataset.csv")

# Clean text
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z ]', '', text)
    return text

# Weighted features (IMPORTANT)
df["combined"] = (
    df["domain"] * 3 + " " +
    df["project_type"] * 3 + " " +
    df["level"] * 2 + " " +
    df["recommended_stack"]
).apply(clean_text)

# Rule scoring
def rule_score(row, user_input, domain, level):
    score = 0
    text = user_input.lower()

    if domain != "Any" and row["domain"] == domain:
        score += 1

    if level != "Any" and row["level"] == level:
        score += 1

    if any(word in row["project_type"].lower() for word in text.split()):
        score += 1

    return score / 3


# Hybrid recommender
def hybrid_recommend(user_input, domain="Any", level="Any", top_n=3):

    filtered_df = df.copy()

    if domain != "Any":
        filtered_df = filtered_df[filtered_df["domain"] == domain]

    if level != "Any":
        filtered_df = filtered_df[filtered_df["level"] == level]

    if filtered_df.empty:
        return df.sample(top_n)

    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(filtered_df["combined"])

    user_vec = vectorizer.transform([clean_text(user_input)])
    sim_scores = cosine_similarity(user_vec, matrix).flatten()
    
    filtered_df = filtered_df.reset_index(drop=True)
    results = []
    for idx, (i, row) in enumerate(filtered_df.iterrows()):
        r_score = rule_score(row, user_input, domain, level)
        # use idx instead of i
        final_score = 0.7 * sim_scores[idx] + 0.3 * r_score
        results.append((i, final_score))

    results = sorted(results, key=lambda x: x[1], reverse=True)[:top_n]

    return filtered_df.loc[[i for i, _ in results]]