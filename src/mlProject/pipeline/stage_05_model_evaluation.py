from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvalaution
from mlProject import logger
from pathlib import Path

# write pipeline code here 


STAGE_NAME = 'Model Evaluation Stage'

class ModelEvaluationPipeline:

    def __init__(self):
        pass

    def main(self):
        # config = ConfigurationManager()
        # model_evaluation_config = config.get_model_evaluation_config()
        # model_evaluation_config = ModelEvalaution(config = model_evaluation_config)
        # model_evaluation_config.log_into_mlflow()

        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvalaution(config = model_evaluation_config)
            model_evaluation_config.log_into_mlflow()
        except Exception as e:
            raise e
  
if __name__ == '__main__':
     
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
    