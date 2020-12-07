
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


"""
converts the dict to an array
pass labels too to ensure X and y are alinged 
avgr is a function which applies a transform across the embedding
"""
def dict_2_arr(data_dict, labels, avgr=lambda x: np.mean(x, axis=0)):
    
    emb_shape = list(data_dict.values())[0].shape
    number_of_embeddings = len(data_dict) 

    X = np.zeros((number_of_embeddings, emb_shape[-1]))
    y = np.zeros(number_of_embeddings)
    
    i = 0

    # iter over sorted keys in labels to ensure proteins
    # from different models are indexed the same
    keys = list(labels.keys())
    keys.sort()
    for key in keys :
        if key == 'd1smyc_':
            continue
        X[i] = avgr(data_dict[key])
        y[i] = labels[key]
        i += 1
        
    return X, y

