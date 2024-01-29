#!/usr/bin/python3
"""
module to gather infos API
"""
from requests import get
from sys import argv
from sys import exit


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
        # init
        nb_tasks = 0
        nb_done_tasks = 0
        list_done_tasks = []
        if res.status_code == 200:
            list_tasks = res.json()
            nb_tasks = len(list_tasks)
            for item_dict in list_tasks:
                if item_dict.get("completed"):
                    nb_done_tasks = nb_done_tasks + 1
                    list_done_tasks.append(item_dict.get("title"))
        # formation the result
        print("Employee {} is done with tasks({}/{}):".format(user_name,
                                                              nb_done_tasks,
                                                              nb_tasks))
        # print the tasks done of user
        for item in list_done_tasks:
            print("\t {}".format(item))
