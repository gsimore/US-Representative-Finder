import datetime
import json
import os

import pandas
import config

ACTIVE_DATE = datetime.date(2019, 1, 1)
DATA_PATH = os.path.join(config.BASE_DIR, 'data')
LEGISLATORS_FILE_PATH = os.path.join(DATA_PATH, 'legislators.json')
ZIPCODE_DISTRICTS_FILE_PATH = os.path.join(DATA_PATH, 'zipcode-districts.json')


class ZipcodeNotFound(Exception):
    # Raise this when a zipcode is not indexed in the dataset.
    pass

class DistrictNotFound(Exception):
    # Raise this when a state and district is not indexed in the legislators dataset.
    pass


def get_states_and_districts(zipcode):
    """
    Looks up the state and district for the given zipcode inside the
    zipcode-districts.json data file.
    :param zipcode: int, a US Zipcode
    :return: list of tuples of states and districts
    """
    df = pandas.read_json(ZIPCODE_DISTRICTS_FILE_PATH, dtype={'zcta': 'str'})
    df = df.set_index('zcta')
    try:
        data = df.loc[zipcode]
    except KeyError:
        raise ZipcodeNotFound

    state = data['state_abbr']
    district = data['cd']
    # Sometimes a zipcode is associated to more than one district.
    if type(data) == pandas.Series:
        return [(state, district)]
    else:
        return list(zip(state.tolist(), district.tolist()))


def get_representatives_df():
    """
    Load the legislators json file into a pandas DataFrame, then perform
    some data cleaning including filtering to representatives, setting the index,
    and filtering down to only current terms based on the current date.

    :return: pandas.DataFrame
    """
    with open(LEGISLATORS_FILE_PATH) as f:
        data = json.loads(f.read())

    df = pandas.json_normalize(data, "terms", ['id', ['name', 'official_full'], 'bio'])

    df = df.set_index(['state', 'district'])

    # Filter to representatives only.
    df = df[(df['type'] == 'rep')]

    # Convert 'start' and 'end' columns to dates
    df[['start', 'end']] = df[['start', 'end']].apply(lambda x: pandas.to_datetime(x).dt.date)
    # Filter to current terms.
    df = df[(df['start'] <= ACTIVE_DATE) & (df['end'] >= ACTIVE_DATE)]

    return df


def get_representative(df, state, district):
    """
    Looks up the US Representative for the given state and district.
    :param state: str,
    :param district: int
    :return:
    """
    try:
        rep_data = df.loc[state, district]
    except KeyError:
        raise DistrictNotFound

    return rep_data


def lookup_representatives(zipcode):
    states_districts = get_states_and_districts(zipcode)
    reps = []
    df = get_representatives_df()
    for state, district in states_districts:
        data = get_representative(df, state, district)
        reps.append({
            'state': state,
            'district': district,
            'name': data['name.official_full'],
            'phone': data['phone'],
            'address': data['address'],
            'url': data['url'],
        })
    return reps
