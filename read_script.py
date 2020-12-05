
import numpy as np

"""
reads dataset from pickle file
data stored in the form of a dict where data['id'] -> *seq*
the id is used to find the same protein represention in any of the models

if model is a language model ('elmo', 'unirep', 'compact'), *seq* will be the embedding
if model=raw *seq* will be the raw amino acid sequence (i.e "ATUGYA...")
if model=label *seq* will be the label for the sequence

split give that paticular split over the task data set
task identifies the dataset
for more information on each task see (https://arxiv.org/pdf/1906.08230.pdf (section 4.2))

PARAMS
    basepath: path to the data folder 
    model = ['elmo', 'unirep', 'compact', 'raw', 'label']
    split = ['train', 'valid', 'test']
    task = ['secondary_structure', 'remote_homology', 'stability', 'fluorescence']
"""
def read_dataset(model: str, task: str, split: str,  basepath='./data'):
    path_to_file = f'{basepath}/{model}/{task}/{task}_{split}.p'
    data = np.load(path_to_file, allow_pickle=True)
    
    return data