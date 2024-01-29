#!/usr/bin/python3
"""
module to export rest json to  file
"""
from json import dump
from requests import get
from sys import argv
from sys import exit


def export_json(id_user, name_user, tasks):
    ''' export rest api to json file '''
    filename = "{}.json".format(id_user)
    mytasks = []
    for task in tasks:
        title = task.get("title")
        status = str(task.get("completed"))
        # fill and format taks user
        mytasks.append({
                        "task": title,
                        "completed": status,
                        "username": name_user
                       })
    with open(filename, mode='w') as f:
        dump({"USER_ID": mytasks}, f)


if __name__ == "__main__":
    if len(argv) != 2 or not isinstance(int(argv[1]), int):
        exit(1)
    url = "https://jsonplaceholder.typicode.com"
    # search if user exists and get its name
    id_user = argv[1]
    api_user = "{}/users/{}".format(url, id_user)
    res = get(api_user)
    if res.status_code == 200:
        user_name = res.json().get("username")
        # search tasks of user
        api_tasks = "{}/todos".format(api_user)
        res = get(api_tasks)
        if res.status_code == 200:
            list_tasks = res.json()
            # export to csv
            export_json(id_user, user_name, list_tasks)
