# Simple django-ninja ML API

This is an example of Machine Learning API based on Boston Housing Dataset available in `tensorflow.keras` package

The goal of machine learning model is to predict house pricing based on some variables:

* CRIM     per capita crime rate by town
* ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
* INDUS    proportion of non-retail business acres per town
* CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
* NOX      nitric oxides concentration (parts per 10 million)
* RM       average number of rooms per dwelling
* AGE      proportion of owner-occupied units built prior to 1940
* DIS      weighted distances to five Boston employment centres
* RAD      index of accessibility to radial highways
* TAX      full-value property-tax rate per $10,000
* PTRATIO  pupil-teacher ratio by town
* B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
* LSTAT    % lower status of the population
  
The target is:

* MEDV     Median value of owner-occupied homes in $1000's

## The model

The machine learning model was trained using 2 `Dense layers` with 64 units each, that implements `relu` as activation 
function. As output, we have a single unit `Dense Layer`, responsible to give us the predicted result

## The API

This API exposes the routes `GET /api/` and `POST /api/`

API docs (powered by OpenAPI) can be accessed through `http://yourdomain/api/docs`

<img src="https://raw.githubusercontent.com/virb30/machine_learning_api/master/images/ml_api_docs.bmp" alt="api docs sample"/>



# Usage

Clone this project

Setup:

```
cd myproject
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Heroku Deploy (failing):

```
PRJ=myapp && \
git init && \
git add . && \
git commit -m 'Initial import' && \
heroku create $PRJ && \
heroku config:set DEBUG=True SECRET_KEY=`cat .env | grep SECRET_KEY | cut -d = -f 2` && \
git push heroku master
```

## Other models

To use another model download the new trained model `.h5` file and put it into `core/assets` folder
(or any folder your preference)

Register the new model into `core/models_ml.py` dictionary and use it in Predictor class `Predictor(models['new_model_key''])`

# TODO

- [ ] Solve the compiled `slug size is too large` problem on heroku deploy