from ninja import NinjaAPI

from .schemas import Input
from .services import Predictor
from .models_ml import models

api = NinjaAPI()


@api.get('/')
def home_api(request):
    return {'hello': 'world'}


@api.post('/')
def predict_api(request, data: Input):
    predictor = Predictor(models['boston_housing'])
    predicted = predictor.predict(data.values.dict())
    return {'predict': predicted}
