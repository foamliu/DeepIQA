import json
import os

from config import image_folder, train_ratio

if __name__ == "__main__":
    dirs = [d for d in os.listdir(image_folder) if os.path.isdir(os.path.join(image_folder, d))]

    train = []
    valid = []

    for d in dirs:
        dir_path = os.path.join(image_folder, d)

        files = [f for f in os.listdir(dir_path) if f.endswith('.jpg')]
        num_files = len(files)
        num_train = int(num_files * train_ratio)

        for i, file in enumerate(files):
            img_path = os.path.join(dir_path, file).replace('\\', '/')
            if i <= num_train:
                train.append({'img_path': img_path, 'label': int(d)})
            else:
                valid.append({'img_path': img_path, 'label': int(d)})

    with open('train.json', 'w') as file:
        json.dump(train, file, indent=4)

    with open('valid.json', 'w') as file:
        json.dump(valid, file, indent=4)
