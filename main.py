from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DatavalidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import  ModelTrainingPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

STAGE_NAME = "DATA INGESTION STAGE"

#logger.info("Welcome to our custom logging")

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\n")
except Exception as e:
    logger.exception(e)
    raise e
    


STAGE_NAME = "DATA VALIDATION STAGE"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DatavalidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "DATA TRANSFORMATION STAGE"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "MODEL TRAINING STAGE"

try:
    logger.info(f"\n\n>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e




STAGE_NAME = "MODEL EVALUATION STAGE"
try:
    logger.info(f"\n\n>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e