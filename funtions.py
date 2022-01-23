def get_query(data_list, query):

    file = map(lambda x: x.strip(), data_list)
    result = []
    request_dict = make_dictionary(query)
    print(request_dict)

    for command, argument in request_dict.items():
        result = run_command(command, argument, file)
        print(result)
    return result


def make_dictionary(parameter):
    dictionary = {}
    for item in parameter.split("|"):
        command, argument = item.split(":")
        dictionary[command] = argument
    return dictionary


def run_command(command, argument, file):
    if command == "filter":
        return list(filter(lambda x, txt=argument: argument in x, file))
    elif command == "map":
        return list(map(lambda x, index=argument: x.split(" ")[index], file))
    elif command == "unique":
        return set(file)
    elif command == "sort":
        if argument == "asc":
            return sorted(file, reverse=False)
        elif argument == "desc":
            return sorted(file, reverse=True)
    elif command == "limit":
        obj = int(argument)
        return list(file)[:obj]
