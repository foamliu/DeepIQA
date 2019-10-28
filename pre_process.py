import json

from config import num_train, anno_file

if __name__ == "__main__":
    with open(anno_file, 'r') as f:
        lines = f.readlines()

    train = []
    valid = []

    for i, line in enumerate(lines[1:]):
        tokens = line.split(',')
        image_name = tokens[0].strip().replace('"', '')
        MOS = float(tokens[7].strip())

        if i < num_train:
            train.append({'image_name': image_name, 'label': MOS})
        else:
            valid.append({'image_name': image_name, 'label': MOS})

    print('num_train: ' + str(len(train)))
    print('num_valid: ' + str(len(valid)))

    with open('train.json', 'w') as file:
        json.dump(train, file, indent=4)

    with open('valid.json', 'w') as file:
        json.dump(valid, file, indent=4)
