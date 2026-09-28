import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommendation System", page_icon=":sparkles:", layout="wide")
load_dotenv()  # Load environment variables from .env file

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()
st.title("Anime Recommendation System")

query = st.text_input("Enter your anime preferences:")

if query:
    with st.spinner("Generating recommendations..."):
        response = pipeline.recommend(query)
        st.markdown("### Recommendations:")
        st.write(response)