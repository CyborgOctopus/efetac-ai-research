import os
from torch.utils.data import Dataset
import rasterio


class RasterioDataset(Dataset):
    """Defines a dataset for reading rasterio objects"""

    def __init__(self, path, required_extension='.tif'):
        super().__init__()
        self.path = path
        self.required_extension = required_extension
        self.rasters = []
        self.get_rasters()

    def __len__(self):
        return len(self.rasters)

    def __getitem__(self, index):
        return self.rasters[index].read(1)

    def get_rasters(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file[-3] == self.required_extension:
                    self.rasters.append(rasterio.open(file))
