# input of each component
import os

from dataclasses import dataclass
from src.entity.config_entity import DataIngestionConfig
from src.logger import logging
from src.exception import FinanceException

@dataclass
class DataIngestionArtifact:
    feature_store_file_path: str #PARQUET file location
    metadata_file_path: str # metadata file location
    download_dir:str # donload data location
