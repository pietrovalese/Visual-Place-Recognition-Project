import os
import gdown
import shutil

os.makedirs("data", exist_ok=True)

URLS = {
    "tokyo_xs": "15QB3VNKj93027UAQWv7pzFQO1JDCdZj2",
    "sf_xs":    "1tQqEyt3go3vMh4fj_LZrRcahoTbzzH-y",
    "gsv_xs":   "1q7usSe9_5xV5zTfN-1In4DlmF5ReyU_A",
    "svox":     "16iuk8voW65GaywNUQlWAbDt6HZzAJ_t9",
}

for dataset_name, file_id in URLS.items():
    print(f"Downloading {dataset_name}")
    zip_filepath = f"data/{dataset_name}.zip"
    gdown.download(id=file_id, output=zip_filepath, quiet=False)
    shutil.unpack_archive(zip_filepath, extract_dir="data")
    os.remove(zip_filepath)