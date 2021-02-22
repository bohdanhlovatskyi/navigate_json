'''
A module for parsing an json object (file) obtained using the Twitter API (or some other).

Contains a function to provide access to various parts of the json object.
For example, ask the user to enter the dictionary key whose meaning he wants to view.
'''

import json
from typing import List, Dict, Union

def get_json() -> Union[List, Dict, None]:
    '''
    Gets file name from user
    '''

    file_name = input('What is the name of your file?\n').rstrip()
    try:
        with open(file_name) as user_file:
            json_obj = json.load(user_file)
        return json_obj
    except FileNotFoundError:
        print('There is no such file in your current working directory.\nExiting... ')
        return None

def redirect(data: Union[Dict, List]):
    '''
    Provide access to various parts of the json object. Is used to navigate file from up to down
    '''

    # when user access dict (object), allows him to choose what key he want to look up
    if isinstance(data, dict):
        value_to_redirect = input(f'Specify one of keys: {list(data.keys())}\n').strip()
        if value_to_redirect not in 'bbbbhe' and value_to_redirect not in list(data.keys()):
            return False

    # list of dicts (objects)
    elif isinstance(data, list) and all([isinstance(elm, dict) for elm in data]):
        print(f'There is a list of objects, each object contains such keys, \
specify what key will help you to identify the object you want: \n{list(data[0].keys())}\n')
        key = input('Choose a key, which will help you to specify, whar object you want.\n')
        if key in 'bbbbbbbhe':
            return key
        if key not in list(data[0].keys()):
            return False
        key_values_from_objs = [obj[key] for obj in data]
        value_from_chosen_obj = input(f'Choose object from {key_values_from_objs}\n').strip()
        if value_from_chosen_obj in 'bbbbbbhe':
            return value_from_chosen_obj
        if value_from_chosen_obj not in key_values_from_objs:
            return False
        for obj in data:
            if obj[key] == value_from_chosen_obj:
                value_to_redirect = data.index(obj) + 1
                break

    else:
        print(f'Here is your data: {data}\n')
        print('You reached the bottom of your file\n')
        # reminds user of his abilities
        value_to_redirect = input(
            'If you want to go back, print: "b" for num of times, \
you want to go back, otherwise: "e", or press Enter\n')
        if not value_to_redirect:
            value_to_redirect = "e"

    return value_to_redirect


def go_back(json_object, path, how_far_):
    '''
    Allows user to move back
    '''

    path = path[:(-how_far_)]
    for elm in path:
        try:
            json_object = json_object[elm]
        except TypeError:
            json_object = json_object[int(elm)]

    return json_object


if __name__ == '__main__':
    data = get_json()
    if data:
        data_to_redirect = data
        user_path = []
        while True:
            # gets key of dict or so on from user
            redirect_value = redirect(data_to_redirect)
            if not redirect_value:
                continue
            elif isinstance(redirect_value, int):
                redirect_value -= 1
            elif redirect_value in 'e':
                break
            elif redirect_value in 'bbbbb':
                how_far = len(redirect_value.strip())
                data_to_redirect = go_back(data, user_path, how_far)
                user_path = user_path[:(-how_far)]
                continue
            elif redirect_value == 'h':
                data_to_redirect = data
                continue
            user_path.append(redirect_value)
            data_to_redirect = data_to_redirect[redirect_value]
