from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainer
from mlProject import logger
from pathlib import Path

# write pipeline code here 


STAGE_NAME = 'Model Training Stage'

class ModelTrainingPipeline:

    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(model_trainer_config)
            model_trainer_config.train()

        except Exception as e:
            raise e

  
if __name__ == '__main__':
     
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<<<")
    except Exception as e:
         logger.exception(e)
    