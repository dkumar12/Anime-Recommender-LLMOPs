from src.data_loader import AnimieDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
load_dotenv()
from utils.logger import get_logger
logger= get_logger(__name__)
from utils.custom_exception import CustomException

def main():
    try:
        logger.info("Starting the build pipeline...")
        data_loader = AnimieDataLoader("data/anime_with_synopsis.csv","data/anime_updated.csv")
        processed_csv = data_loader.load_and_process()

        logger.info("data loaded and processed..")

        vector_builder = VectorStoreBuilder(processed_csv)
        vector_builder.build_and_save_vectorstore()
        logger.info("Vector store build completed successfully.")
        logger.info("Build pipeline completed successfully.")
    except Exception as e:
        logger.error(f"Build pipeline failed: {str(e)}")
        raise CustomException(f"Error during build pipeline execution: {e}")

if __name__ == "__main__":
    main()