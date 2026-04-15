# 🚀 DevStack AI – Smart Developer Project Recommender

## 🌟 Overview

DevStack AI is a **hybrid recommendation system** designed to help developers choose the right project ideas and tech stacks based on their interests, skill level, and domain.

Instead of randomly using any techstack for projects, this system intelligently suggests **personalized project blueprints** using a combination of:

* 📊 Content-based filtering (TF-IDF + cosine similarity)
* ⚙️ Rule-based filtering (domain, level, keyword matching)

It’s built as a **fast, interactive web app using Streamlit**, making it simple, visual, and user-friendly.

---

## 🎯 Problem Statement

Many developers—especially beginners—struggle with:

* ❓ Selecting an appropriate tech stack
* ❓ Matching projects with their skill level

DevStack AI solves this by acting like a **smart assistant** that recommends structured techstack ideas instantly.

---

## 🧠 How It Works

### 🔹 1. User Input

User provides:

* Project idea (text input)
* Domain (e.g., Web Dev, AIML)
* Skill level (Beginner / Intermediate / Advanced)

---

### 🔹 2. Data Processing

Dataset contains:

* Domain
* Level
* Project Type
* Recommended Tech Stack

These are combined into a single feature for analysis.

---

### 🔹 3. Content-Based Filtering

* Converts text into vectors using **TF-IDF**
* Measures similarity using **cosine similarity**
* Finds projects closest to user idea

---

### 🔹 4. Rule-Based Filtering

Applies logical scoring:

*  Domain match
*  Level match
*  Keyword match

---

### 🔹 5. Hybrid Scoring

Final score is calculated as:

```
Final Score = 0.7 × Similarity + 0.3 × Rule Score
```

This ensures both:

* Semantic understanding (AI)
* Logical filtering (rules)

---

## 💻 Tech Stack

* 🐍 Python
* 📊 Pandas
* 🤖 Scikit-learn
* 🎨 Streamlit

---

## 📁 Project Structure

```
DevStack-AI/
│
├── app.py                # Streamlit UI
├── recommender.py        # Hybrid recommendation logic
├── requirements.txt      # Dependencies
│
└── dataset/
    └── developer_dataset.csv
```

---

## ⚡ Features

* 🔍 Smart project recommendations
* 🎯 Domain & skill-based filtering
* ⚡ Real-time suggestions
* 🎨 Clean UI with interactive cards
* 🧠 Hybrid recommendation engine

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the app

```bash
streamlit run app.py
```

---

## 📸 Example Output

User Input:

```
"I want to build an AI chatbot"
```

Output:

* 🤖 Domain: AIML
* 📌 Project: AI Chatbot
* ⚙️ Tech Stack: Python, FastAPI, LangChain
* 💡 Explanation: Matches your idea and skill level

---

## 💡 What I Learned

* How recommendation systems work
* Combining ML with rule-based logic
* Feature engineering using text data
* Building interactive apps with Streamlit


## 👩‍💻 Author

**Divya Kansara**  **Resham Patel**

---


