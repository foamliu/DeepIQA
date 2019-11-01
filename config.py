import torch

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')  # sets device for model and PyTorch tensors

im_size = 224
num_classes = 1

num_samples = 10073
num_train = 9073
num_valid = 1000
image_folder = 'data/photo'
anno_file = 'data/koniq10k_scores_and_distributions.csv'
data_file = 'data/data.pkl'


# Training parameters
num_workers = 4  # for data-loading
grad_clip = 5.  # clip gradients at an absolute value of
print_freq = 10  # print training/validation stats  every __ batches
checkpoint = None  # path to checkpoint, None if none
