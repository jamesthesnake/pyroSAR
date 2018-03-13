import pyroSAR
import pytest
import os

testdir = os.getenv('TESTDATA_DIR', 'pyroSAR/tests/data/')

testcases = [
    #SAFE
    {'path': os.path.join('ci_testing/tests/data/', 'S1A_IW_GRDH_1SDV_20150222T170750_20150222T170815_004739_005DD8_3768.zip'),
     'acquisition_mode': 'IW',
     'compression': 'zip',
     'corners': {'ymax': 52.183979, 'ymin': 50.295261, 'xmin': 8.017178, 'xmax': 12.0268},
     'lines': 16685,
     'outname': 'S1A__IW___A_20150222T170750',
     'orbit': 'A',
     'polarizations': ['VV', 'VH'],
     'product': 'GRD',
     'samples': 25368,
     'sensor': 'S1A',
     'spacing': (10.0, 9.998647),
     'start': '20150222T170750',
     'stop': '20150222T170815'
     }
]


@pytest.fixture
def scene(case):
    case['pyro'] = pyroSAR.identify(case['path'])
    return case


@pytest.mark.parametrize('case', testcases)
class Test_Metadata():
    def test_attributes(self, scene):
        assert scene['pyro'].acquisition_mode == scene['acquisition_mode']
        assert scene['pyro'].compression == scene['compression']
        assert scene['pyro'].getCorners() == scene['corners']
        assert scene['pyro'].lines == scene['lines']
        assert scene['pyro'].outname_base() == scene['outname']
        assert scene['pyro'].orbit == scene['orbit']
        assert scene['pyro'].polarizations == scene['polarizations']
        assert scene['pyro'].product == scene['product']
        assert scene['pyro'].samples == scene['samples']
        assert scene['pyro'].start == scene['start']
        assert scene['pyro'].stop == scene['stop']
        assert scene['pyro'].sensor == scene['sensor']
        assert scene['pyro'].spacing == scene['spacing']
        assert scene['pyro'].is_processed('data/') is False


def test_identify_fail():
    with pytest.raises(IOError):
        pyroSAR.identify(os.path.join(testdir, 'foobar'))


def test_export2dict():
    pass
