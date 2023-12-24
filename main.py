from CatvsDogClassifier.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from CatvsDogClassifier.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline
from CatvsDogClassifier import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started..!")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare base Model"
try:
    logger.info(f"********************")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<\n\nx===========x")

except Exception as e:
    logger.exception(e)
    raise e