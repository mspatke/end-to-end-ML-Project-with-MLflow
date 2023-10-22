import os 
import pandas as pd
from mlProject import logger
from mlProject.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split


class DataTransformation:

    def __init__(self, config : DataTransformationConfig):
        self.config = config

    # we can do other types of transformation like PCA, scaler etc

    def train_test_split(self):

        data =pd.read_csv(self.config.data_path)

        train, test = train_test_split(data , test_size=0.20)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)

        logger.info("Data split into train set and test set")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
        print(data.shape)
