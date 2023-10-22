

import os 
import pandas as pd
from mlProject import logger
from mlProject.entity.config_entity import DataValidationConfig


class DataValidation:

    """ This code performas data validation check on new data"""

    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_columns(self) -> bool:

        try:
            validation_status = None
            
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns) # get all column names from csv

            all_schema = self.config.all_schema # get all coulmn names from defined schema to verify

          
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    expected_data_type = all_schema[col] # get the data type of particular columns from schema
                    actual_data_type = data[col].dtype
                    if actual_data_type != expected_data_type:
                        validation_status = False
                        with open(self.config.STATUS_FILE,'w') as f:
                            f.write(f"Validation status: {validation_status}")
                    else:
                        validation_status = True
                        with open(self.config.STATUS_FILE,'w') as f:
                            f.write(f"Validation status: {validation_status}")
                        
                        
            
            return validation_status

        except Exception as e:
            logger.exception(e)
            raise e    
    
