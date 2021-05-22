import requests
import argparse
from ml_api.core.factory import read_json_file

BASE_URL = 'http://127.0.0.1:8000/'


def predict(data):
    url = f'{BASE_URL}api/'
    response = requests.post(url, data=data)
    return response.json()


def build_parser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = True

    sp_predict = subparsers.add_parser('predict')
    sp_predict.add_argument('json')

    return parser


if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()

    data = read_json_file(args.json)

    print(predict(data))
