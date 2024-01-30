#!/usr/bin/python3
"""
module to export rest json to  file
"""
from json import dump
from requests import get


def export_json(url, tasks):
    ''' export rest api to json file '''
    filename = "todo_all_employees.json"
    _dict = {}
    for task in tasks:
        title = task.get("title")
        status = task.get("completed")
        id_user = task.get("userId")
        api_user = "{}/users/{}".format(url, id_user)
        res = get(api_user)
        if res.status_code == 200:
            name_user = res.json().get("username")
        else:
            name_user = ""
        item = {
                "username": name_user,
                "task": title,
                "completed": status
               }
        if not _dict:
            _dict = {id_user: [item]}
        else:
            exist = _dict.get(id_user, None)
            if exist is None:
                _dict[id_user] = [item]
            else:
                _dict[id_user].append(item)
    with open(filename, mode='w') as f:
        dump(_dict, f)


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    api_tasks = "{}/todos".format(url)
    res = get(api_tasks)
    if res.status_code == 200:
        all_tasks = res.json()
        export_json(url, all_tasks)
