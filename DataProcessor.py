import numpy as np
import pandas as pd


class DataProcessor:

    def __init__(self) -> None:
        pass

    @staticmethod
    def load_data(filename: str, delimeter: str, labels: list):
        '''
        Used to load the data from a .csv file into a pandas DataFrame.

        @params
        - filename: (str) -> name of the .csv file containing all the data  
        - delimeter: (str) -> character(s) by which the data entries are seperated
        - labels: (list) -> labels for the columns in the DataFrame

        @returns
        - (pd.DataFrame) -> DataFrame containing data for the Neural Network
        '''
        return pd.read_csv(filename, sep=delimeter, names=labels)

    @staticmethod
    def split_dataset(dataset: pd.DataFrame, split_ratio: float):
        '''
        Used to generate split datasets from a given datasets based of a given split ratio.

        @params
        - dataset: (pd.DataFrame) -> original dataset to be split
        - split_ratio: (float) -> ratio of data which the second split set should receive

        @returns
        - split_set1, split_set2: (tuple[pd.DataFrame, pd.DataFrame]) -> new training and validation datasets 

        Note:

        split_ratio is the size for the validation set, i.e. if the ratio is 0.2, then the 
        ratio going to the training set is 0.8 (80%) and the validation set will 0.2 (20%) 
        of the data.
        '''
        # get training set size
        n = dataset.shape[0]
        
        # copy and shuffle training set
        temp_set = dataset.copy()

        # split data into respective ratios
        mid_index = int(n * (1 - split_ratio))
        split_set1 = temp_set[0: mid_index][:] #excludes mid index
        split_set2 = temp_set[int(n * (1 - split_ratio)):][:]

        return split_set1, split_set2

    @staticmethod
    def shuffle_dataset(dataset: pd.DataFrame):
        '''
        Shuffles the entries of given dataset.

        @params
        - dataset: (pd.DataFrame) -> dataset to be shuffles

        @returns
        - (pd.DataFrame) -> shuffled version of the given dataset

        '''
        copy_set = dataset
        return copy_set.sample(frac=1, random_state=42).reset_index(drop=True)

    @staticmethod
    def normilize_dataset(dataset: pd.DataFrame):
        '''
        [Description]

        @params

        @returns
        '''
        temp_set = dataset.copy()
        scale_feature = lambda feature: (feature - feature.min()) / (feature.max() - feature.min())
        norm_set = temp_set[:].apply(scale_feature, axis=1)

        return norm_set
    
    @staticmethod
    def select_select_minibatch(dataset: pd.DataFrame):
        '''
        [Description]

        @params

        @returns
        '''
        pass #To be added
