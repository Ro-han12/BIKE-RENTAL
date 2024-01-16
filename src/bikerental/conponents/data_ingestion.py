import os
import zipfile
import urllib.request as request
from bikerental import logger
from bikerental.utils.common import get_size
from bikerental.entity.config_entity import DataIngestionConfig
from pathlib import Path  # Import Path from pathlib

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} download! with the following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        # Check if the file exists
        if not os.path.exists(self.config.local_data_file):
            logger.error(f"Error: File '{self.config.local_data_file}' not found.")
            return

        # Check if the file is a ZIP file based on its extension
        if not self.config.local_data_file.lower().endswith('.zip'):
            logger.error(f"Error: File '{self.config.local_data_file}' is not a ZIP file.")
            return

        # Continue with your existing logic for handling the ZIP file
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
