import os
import functools
import testdata

DATASETS = [
    'dha',
    'wine',
    'religion',
    #'census',
    #'network',
]


def get_dataset(name):
    data_root = os.path.join(testdata.ROOT, name)
    samples = os.path.join(data_root, 'results', 'samples')
    return {
        'meta': os.path.join(data_root, 'dataset', 'meta.json'),
        'data': os.path.join(data_root, 'dataset', 'data.bin'),
        'mask': os.path.join(data_root, 'dataset', 'mask.bin'),
        'latent': os.path.join(samples, 'sample_000.json'),
        'predictor': os.path.join(samples, 'sample_000.predictor.json'),
    }


def for_each_dataset(fun):
    @functools.wraps(fun)
    def test_one(dataset):
        fun(**get_dataset(dataset))

    @functools.wraps(fun)
    def test_all():
        for dataset in DATASETS:
            yield test_one, dataset

    return test_all
