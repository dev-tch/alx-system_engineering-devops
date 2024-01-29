#!/usr/bin/python3
"""
module to gather infos API
"""
from requests import get
from sys import argv
from sys import exit


def quote(value):
    '''add double quotes to value of variable'''
    return '"' + value + '"'


def export_csv(id_user, name_user, tasks):
    ''' export rest api to csv '''
    filename = "{}.csv".format(id_user)
    with open(filename, 'w') as f:
        for task in tasks:
            title = quote(task.get("title"))
            status = quote(str(task.get("completed")))
            idy = quote(id_user)
            name = quote(name_user)
            line = "{},{},{}{}\n".format(idy, name, status, title)
            f.write(line)


if __name__ == "__main__":
    if len(argv) != 2 or not isinstance(int(argv[1]), int):
        exit(1)
    url = "https://jsonplaceholder.typicode.com"
    # search if user exists and get its name
    id_user = argv[1]
    api_user = "{}/users/{}".format(url, id_user)
    res = get(api_user)
    if res.status_code == 200:
        user_name = res.json().get("name")
        # search tasks of user
        api_tasks = "{}/todos".format(api_user)
        res = get(api_tasks)
        if res.status_code == 200:
            list_tasks = res.json()
            # export to csv
            export_csv(id_user, user_name, list_tasks)
