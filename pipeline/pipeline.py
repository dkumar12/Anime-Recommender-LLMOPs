from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger= get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self,persist_dir:str="chroma_db"):
        try:
            logger.info("Initializing the Anime Recommendation Pipeline...")
            vector_builder = VectorStoreBuilder(csv_path="", persist_dir=persist_dir)
            retriever = vector_builder.load_vectorstore().as_retriever()

            self.recommender = AnimeRecommender(retriever=retriever, api_key=GROQ_API_KEY, model_name=MODEL_NAME)
            logger.info("Pipeline initialized successfully.")

        except Exception as e:
            logger.error(f"failed to initialize the pipeline: {str(e)}")
            raise CustomException(f"Error during pipeline initialization: {e}")

    def recommend(self,query:str):
        try:
            logger.info(f"Generating recommendations for query: {query}")
            recommendations = self.recommender.get_recommendations(query)
            logger.info("Recommendations generated successfully.")
            return recommendations
        except Exception as e:
            logger.error(f"Failed to generate recommendations: {str(e)}")
            raise CustomException(f"Error during recommendation generation: {e}")

