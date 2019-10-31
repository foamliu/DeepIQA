import os
import pickle
from subprocess import Popen, PIPE

from tqdm import tqdm

filename = 'data/photo.csv'

if __name__ == '__main__':
    with open(filename, 'r') as f:
        lines = f.readlines()

    samples = []
    for line in tqdm(lines[1:]):
        tokens = line.split(',')
        before_file = tokens[0].strip()
        after_file = tokens[1].strip()

        folder = 'data/photo'

        before_filename = before_file[before_file.rfind("/") + 1:]
        before_filename = os.path.join(folder, before_filename)
        if not os.path.isfile(before_filename):
            process = Popen(["wget", '-N', before_file, "-P", folder], stdout=PIPE)
            (output, err) = process.communicate()
            exit_code = process.wait()

        after_filename = after_file[after_file.rfind("/") + 1:]
        after_filename = os.path.join(folder, after_filename)
        if not os.path.isfile(after_filename):
            process = Popen(["wget", '-N', after_file, "-P", folder], stdout=PIPE)
            (output, err) = process.communicate()
            exit_code = process.wait()

        samples.append({'before_filename': before_filename, 'after_filename': after_filename})

        with open('data.pkl', 'wb') as f:
            pickle.dump(samples, f)
