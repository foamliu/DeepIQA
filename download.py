import pickle
from subprocess import Popen, PIPE

filename = 'data/photo.csv'

if __name__ == '__main__':
    with open(filename, 'r') as f:
        lines = f.readlines()

    samples = []
    for i, line in enumerate(lines[1:]):
        tokens = line.split(',')
        before_file = tokens[0].strip()
        after_file = tokens[1].strip()

        folder = 'data/photo'
        process = Popen(["wget", '-N', before_file, "-P", folder], stdout=PIPE)
        (output, err) = process.communicate()
        exit_code = process.wait()
        before_filename = before_file[before_file.rfind("/") + 1:]

        process = Popen(["wget", '-N', after_file, "-P", folder], stdout=PIPE)
        (output, err) = process.communicate()
        exit_code = process.wait()
        after_filename = after_file[after_file.rfind("/") + 1:]

        samples.append({'before_filename': before_filename, 'after_filename': after_filename})

        with open('data.pkl', 'wb') as f:
            pickle.dump(samples, f)
