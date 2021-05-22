import pytest

from ml_api.core.factory import read_json_file


@pytest.fixture
def values():
    data = read_json_file('valores.json')
    return data


@pytest.fixture(autouse=True)
def fixed_predict(monkeypatch):
    from ml_api.core.services import Predictor
    monkeypatch.setattr(Predictor, 'predict', lambda x, y: 20.0)