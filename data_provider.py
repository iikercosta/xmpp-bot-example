import os
import zipfile
from typing import List

import requests


DATA_URL = 'https://opendata.euskadi.eus/contenidos/ds_informes_estudios/covid_19_2020/opendata/situacion-epidemiologica.zip'
DATA_FILE = 'csv-dir/01.csv'

NEW_CASES_CODE = 6
DEATHS_CODE = 15
HOSPITALIZED_CODE = 17
UCI_CODE = 18


def get_csv_files() -> None:
    response = requests.get(DATA_URL)

    with open('data.zip', 'wb') as fd:
        fd.write(response.content)

    with zipfile.ZipFile('data.zip', 'r') as zd:
        zd.extractall('csv-dir')

    os.remove('data.zip')

    for d in os.listdir('csv-dir'):
        if d != '01.csv':
            os.remove(f'csv-dir/{d}')


def get_last_fields() -> List[str]:
    with open(DATA_FILE, 'rb') as fd:
        for line in fd:
            pass
    return line.decode('ISO-8859-1').strip().split(';')


def get_new_cases_last_24_hours() -> int:
    return int(get_last_fields()[NEW_CASES_CODE])


def get_deaths_last_24_hours() -> int:
    return int(get_last_fields()[DEATHS_CODE])


def get_hospitalized() -> int:
    return int(get_last_fields()[HOSPITALIZED_CODE])


def get_ucied() -> int:
    return int(get_last_fields()[UCI_CODE])


def get_data() -> str:
    get_csv_files()
    ret = f'Casos totales: {get_new_cases_last_24_hours()}\n'
    ret+= f'Fallecidos totales: {get_deaths_last_24_hours()}\n'
    ret+=f'Hospitalizados: {get_hospitalized()}\n'
    ret+=f'Ingresados en UCI: {get_ucied()}'

    return ret

