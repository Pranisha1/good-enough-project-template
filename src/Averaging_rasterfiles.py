import os
import rasterio
import pcraster as pc
import glob
import numpy as np
from osgeo import gdal


# Precipitation fall (without fraction)
# set the directory containing raster files
dir_path = "C:/Users/Pokhr002/OneDrive - Universiteit Utrecht/02Data/Selected results/Precipitation"
# Define the list of file extensions to exclude
exclude_extensions = [".tss", ".csv", ".aux", ".map"]

# Get a list of all raster files in the folder
raster_files = glob.glob(dir_path + "/*")

# Open the first raster to get metadata
# Get metadata from one of the input files
with rasterio.open(raster_files[1]) as src:
    meta = src.meta

# Initialize a numpy array to hold the sum of all the rasters
raster_sum = np.zeros((meta["height"], meta["width"]), dtype=np.float64)

# Loop through the raster files and add each one to the sum
for file in raster_files:
    with rasterio.open(file) as src:
        # Read the data from the raster file
        data = src.read(1, out_shape=(meta["height"], meta["width"]))
        # Add the data to the sum
        raster_sum += data

# Calculate the average
raster_avg = raster_sum / len(raster_files)

# Write output file
with rasterio.open(
    "C:/Users/Pokhr002/OneDrive - Universiteit Utrecht/02Data/Selected results/Figures/Average_precipitation1.tif",
    "w",
    **meta,
    PCRASTER_VALUESCALE="VS_SCALAR"
) as dst:
    dst.write(raster_avg.astype(rasterio.float32), 1)


# snow fall
# set the directory containing raster files
dir_path = (
    "C:/Users/Pokhr002/OneDrive - Universiteit Utrecht/02Data/Selected results/Snow"
)
# Define the list of file extensions to exclude
exclude_extensions = [".tss", ".csv", ".aux", ".map"]

# Get a list of all raster files in the folder
raster_files = glob.glob(dir_path + "/*")

# Open the first raster to get metadata
# Get metadata from one of the input files
with rasterio.open(raster_files[1]) as src:
    meta = src.meta

# Initialize a numpy array to hold the sum of all the rasters
raster_sum = np.zeros((meta["height"], meta["width"]), dtype=np.float64)

# Loop through the raster files and add each one to the sum
for file in raster_files:
    with rasterio.open(file) as src:
        # Read the data from the raster file
        data = src.read(1, out_shape=(meta["height"], meta["width"]))
        # Add the data to the sum
        raster_sum += data

# Calculate the average
raster_avg = raster_sum / len(raster_files)

# Write output file
with rasterio.open(
    "C:/Users/Pokhr002/OneDrive - Universiteit Utrecht/02Data/Selected results/Figures/Average_snowfall.tif",
    "w",
    **meta,
    PCRASTER_VALUESCALE="VS_SCALAR"
) as dst:
    dst.write(raster_avg.astype(rasterio.float32), 1)


# Rainfall
# set the directory containing raster files
dir_path = (
    "C:/Users/Pokhr002/OneDrive - Universiteit Utrecht/02Data/Selected results/Rain"
)
# Define the list of file extensions to exclude
exclude_extensions = [".tss", ".csv", ".aux", ".map"]

# Get a list of all raster files in the folder
raster_files = glob.glob(dir_path + "/*")

# Open the first raster to get metadata
# Get metadata from one of the input files
with rasterio.open(raster_files[1]) as src:
    meta = src.meta

# Initialize a numpy array to hold the sum of all the rasters
raster_sum = np.zeros((meta["height"], meta["width"]), dtype=np.float64)

# Loop through the raster files and add each one to the sum
for file in raster_files:
    with rasterio.open(file) as src:
        # Read the data from the raster file
        data = src.read(1, out_shape=(meta["height"], meta["width"]))
        # Add the data to the sum
        raster_sum += data

# Calculate the average
raster_avg = raster_sum / len(raster_files)

# Write output file
with rasterio.open(
    "C:/Users/Pokhr002/OneDrive - Universiteit Utrecht/02Data/Selected results/Rasterfiles/Average_Rainfall.tif",
    "w",
    **meta,
    PCRASTER_VALUESCALE="VS_SCALAR"
) as dst:
    dst.write(raster_avg.astype(rasterio.float32), 1)


# Total Runoff
# set the directory containing raster files
dir_path = "C:/Users/Pokhr002/OneDrive - Universiteit Utrecht/02Data/Selected results/Total_runoff"
# Define the list of file extensions to exclude
exclude_extensions = [".tss", ".csv", ".aux", ".map"]

# Get a list of all raster files in the folder
raster_files = glob.glob(dir_path + "/*")

# Open the first raster to get metadata
# Get metadata from one of the input files
with rasterio.open(raster_files[1]) as src:
    meta = src.meta

# Initialize a numpy array to hold the sum of all the rasters
raster_sum = np.zeros((meta["height"], meta["width"]), dtype=np.float64)

# Loop through the raster files and add each one to the sum
for file in raster_files:
    with rasterio.open(file) as src:
        # Read the data from the raster file
        data = src.read(1, out_shape=(meta["height"], meta["width"]))
        # Add the data to the sum
        raster_sum += data

# Calculate the average
raster_avg = raster_sum / len(raster_files)

# Write output file
with rasterio.open(
    "C:/Users/Pokhr002/OneDrive - Universiteit Utrecht/02Data/Selected results/Rasterfiles/Average_Total_runoff.tif",
    "w",
    **meta,
    PCRASTER_VALUESCALE="VS_SCALAR"
) as dst:
    dst.write(raster_avg.astype(rasterio.float32), 1)


# Rainfall Runoff
# set the directory containing raster files
dir_path = "C:/Users/Pokhr002/OneDrive - Universiteit Utrecht/02Data/Selected results/Rain_runoff"
# Define the list of file extensions to exclude
exclude_extensions = [".tss", ".csv", ".aux", ".map"]

# Get a list of all raster files in the folder
raster_files = glob.glob(dir_path + "/*")

# Open the first raster to get metadata
# Get metadata from one of the input files
with rasterio.open(raster_files[1]) as src:
    meta = src.meta

# Initialize a numpy array to hold the sum of all the rasters
raster_sum = np.zeros((meta["height"], meta["width"]), dtype=np.float64)

# Loop through the raster files and add each one to the sum
for file in raster_files:
    with rasterio.open(file) as src:
        # Read the data from the raster file
        data = src.read(1, out_shape=(meta["height"], meta["width"]))
        # Add the data to the sum
        raster_sum += data

# Calculate the average
raster_avg = raster_sum / len(raster_files)

# Write output file
with rasterio.open(
    "C:/Users/Pokhr002/OneDrive - Universiteit Utrecht/02Data/Selected results/Rasterfiles/Average_Rainfall_runoff.tif",
    "w",
    **meta,
    PCRASTER_VALUESCALE="VS_SCALAR"
) as dst:
    dst.write(raster_avg.astype(rasterio.float32), 1)
