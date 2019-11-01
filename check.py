import pickle
from config import data_file, image_folder
from tqdm import tqdm
import cv2 as cv
import os

if __name__ == "__main__":
    with open(data_file, 'rb') as f:
        samples = pickle.load(f)

    for sample in tqdm(samples):
        before = sample['before']
        fullpath = os.path.join(image_folder, before)
        img = cv.imread(fullpath)
        assert(img is not None)

        after = sample['after']
        fullpath = os.path.join(image_folder, before)
        img = cv.imread(fullpath)
        assert (img is not None)

