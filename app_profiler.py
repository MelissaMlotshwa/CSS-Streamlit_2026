import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Topic Modelling with LDA | Twitter Data",
    layout="wide"
)

# ===============================
# TITLE & INTRO
# ===============================
st.title("Topic Modelling using LDA with Twitter Data")

st.markdown("""
This application provides an **interactive overview** of a topic modelling analysis
conducted on Twitter data using **Latent Dirichlet Allocation (LDA)**.

It summarises the full workflow implemented in the accompanying Jupyter notebook,
from preprocessing to interpretation.
""")

# ===============================
# SIDEBAR NAVIGATION
# ===============================
st.sidebar.title("Navigation Guide")
st.sidebar.markdown("""
- 📌 Research Context  
- 🧹 NLP Methodology  
- 📊 Key Results  
- 🔍 Interactive Topic Visualisation  
- 🧠 Topic Interpretation  
- 📈 Model Evaluation  
- 📬 Contact Information  
""")

# ===============================
# RESEARCHER OVERVIEW
# ===============================
st.header("Researcher Overview")

name = "Melissa K Mlotshwa"
field = "Business and Financial Analytics"
institution = "University of the Free State"

st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg",
    caption="Visual metaphor for topic structures (Pixabay)",
    use_column_width=True
)

# ===============================
# RESEARCH CONTEXT
# ===============================
st.header("Research Context")

st.markdown("""
Social media platforms such as Twitter generate large volumes of unstructured text data.
This project applies **topic modelling** to uncover latent themes in public discourse.

**Research objectives:**
- Identify dominant discussion themes
- Explore relationships between keywords
- Understand topic prevalence within the corpus
""")

# ===============================
# METHODOLOGY OVERVIEW
# ===============================
st.header("Methodology Overview")

st.markdown("""
The notebook follows a standard **Natural Language Processing (NLP) pipeline**:
""")

st.markdown("""
🧹 **Text Preprocessing**
- Tokenisation
- Stopword removal
- Lemmatization

📊 **Vectorisation**
- Bag-of-Words representation
- Document–Term Matrix using `CountVectorizer`

🧠 **Topic Modelling**
- Latent Dirichlet Allocation (LDA)
- Optimal topic number selection

📈 **Evaluation & Interpretation**
- Topic coherence and perplexity
- Interactive visualisation using pyLDAvis
""")

st.info("This Streamlit app summarises these steps without recomputing the model.")

# ===============================
# KEY RESULTS SUMMARY
# ===============================
st.header("Key Findings")

st.markdown("""
- The LDA model identified **distinct latent topics** within Twitter discussions
- Topics varied in prevalence, indicating unequal representation in the corpus
- Keyword overlap revealed thematic proximity between certain topics
- The results demonstrate LDA’s usefulness for exploratory text analysis
""")

# ===============================
# INTERACTIVE LDA VISUALISATION
# ===============================
st.header("Interactive Topic Modelling (LDA)")

st.markdown("""
The interactive visualisation below allows you to:
- Explore topic distances
- Examine keyword relevance
- Adjust the λ parameter for interpretation
""")

st.warning("""
💡 **How to read this visualisation**
- Larger circles = more prevalent topics
- Distance between circles = topic similarity
- Adjust λ to balance frequency vs exclusivity
""")

with st.expander("🔍 View Interactive Topic Model"):
    try:
        with open("lda_vis.html", "r", encoding="utf-8") as f:
            lda_html = f.read()

        components.html(
            lda_html,
            height=800,
            scrolling=True
        )
    except FileNotFoundError:
        st.error(
            "LDA visualization file not found. "
            "Ensure `lda_vis.html` exists in the repository."
        )

# ===============================
# TOPIC INTERPRETATION
# ===============================
st.header("Topic Interpretation Guide")

topic_choice = st.selectbox(
    "Select a topic to explore",
    [
        "Topic 1 – Economic Impact",
        "Topic 2 – Public Health Discourse",
        "Topic 3 – Social & Behavioural Trends",
        "Topic 4 – Policy & Governance"
    ]
)

if topic_choice == "Topic 1 – Economic Impact":
    st.markdown("""
    This topic is dominated by terms related to:
    - Economic growth
    - Financial impact
    - Market and cost dynamics
    """)

elif topic_choice == "Topic 2 – Public Health Discourse":
    st.markdown("""
    This topic reflects discussions around:
    - Health systems
    - Community health outcomes
    - Program implementation
    """)

elif topic_choice == "Topic 3 – Social & Behavioural Trends":
    st.markdown("""
    This topic captures:
    - Organisational processes
    - Social practices
    - Behavioural patterns
    """)

elif topic_choice == "Topic 4 – Policy & Governance":
    st.markdown("""
    This topic is associated with:
    - Policy frameworks
    - Governance structures
    - Institutional responses
    """)

# ===============================
# MODEL EVALUATION
# ===============================
st.header("Model Evaluation")

st.markdown("""
The notebook evaluated model quality using:

- **Topic Coherence**  
  Measures interpretability and semantic consistency

- **Perplexity**  
  Measures model generalisation to unseen data

A balance between these metrics was used to select the optimal number of topics.
""")

# ===============================
# OPTIONAL: PUBLICATIONS UPLOAD
# ===============================
st.header("Related Publications (Optional)")

uploaded_file = st.file_uploader("Upload a CSV of publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

# ===============================
# CONCLUSION
# ===============================
st.header("Conclusion")

st.markdown("""
This application serves as a **research companion dashboard** to the original notebook.

It transforms technical outputs into:
- Interpretable visuals
- Structured explanations
- Interactive exploration tools

Such dashboards are valuable for communicating NLP research to both technical
and non-technical audiences.
""")

# ===============================
# CONTACT INFORMATION
# ===============================
st.header("Contact Information")

email = "2021276346@ufs4life.ac.za"
st.write(f"You can reach **{name}** at {email}.")


