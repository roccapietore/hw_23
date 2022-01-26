import re
from typing import List, Iterable, Optional


def get_query(data_list: List[str], query: str) -> Optional[List[str]]:
    file: Iterable[str] = map(lambda x: x.strip(), data_list)
    result: Optional[List[str]] = []
    request_dict = make_dictionary(query)

    for command, argument in request_dict.items():
        if not result:
            data = file
        else:
            data = result
        result = run_command(command, argument, data)
    return result


def make_dictionary(parameter: str) -> dict:
    dictionary = {}
    for item in parameter.split("|"):
        command, argument = item.split(":")
        dictionary[command] = argument
    return dictionary


def run_command(command: str, argument: str, file: Iterable) -> List[str]:
    if command == "filter":
        return list(filter(lambda x, txt=argument: argument in x, file))
    elif command == "map":
        return list(map(lambda x, index=argument: x.split(" ")[index], file))
    elif command == "unique":
        return list(set(file))
    elif command == "sort":
        if argument == "asc":
            return sorted(file, reverse=False)
        elif argument == "desc":
            return sorted(file, reverse=True)
    elif command == "limit":
        obj = int(argument)
        return list(file)[:obj]
    elif command == "regex":
        regex = re.compile(argument)
        return list(filter(lambda x: regex.findall(x),  file))

