import rasterio
import fiona

# Gets satellite images
def get_images():
    image_directory = 'C:/Users/CyborgOctopus/Downloads/ForWarn Data'

# Gets masks
def get_masks():
    path = 'C:/Users/CyborgOctopus/Downloads/extractDamage2016_2021/new10_2163/new10_2163.shp'
    with fiona.open(path, 'r') as shapefiles:
        return [feature['geometry'] for feature in shapefiles]
