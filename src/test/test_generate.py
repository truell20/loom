import os
from distributions.fileutil import tempdir
import loom.generate

CLEANUP_ON_ERROR = int(os.environ.get('CLEANUP_ON_ERROR', 1))

FEATURE_TYPES = loom.schema.FEATURE_TYPES.keys()
FEATURE_TYPES += ['mixed']


def test_generate():
    for feature_type in FEATURE_TYPES:
        yield _test_generate, feature_type


def _test_generate(feature_type):
    root = os.path.abspath(os.path.curdir)
    with tempdir(cleanup_on_error=CLEANUP_ON_ERROR):
        rows_out = os.path.abspath('rows.pbs.gz')
        model_out = os.path.abspath('model.pb.gz')
        groups_out = os.path.abspath('groups')
        os.chdir(root)
        loom.generate.generate(
            feature_type=feature_type,
            row_count=100,
            feature_count=100,
            density=0.5,
            rows_out=rows_out,
            model_out=model_out,
            groups_out=groups_out,
            debug=True,
            profile=None)
