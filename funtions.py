def get_query(file, query):
    file = map(lambda x: x.strip(), file)
    result = ""
    request_dict = make_dictionary(query)
    print(request_dict)

    for command, argument in request_dict.items():
        if command == "filter":
            result = list(filter(lambda x, txt=argument: argument in x, file))
        elif command == "map":
            result = list(map(lambda x, index=argument: x.split(" ")[index], file))
        elif command == "unique":
            result = set(file)
        elif command == "sort":
            if argument == "asc":
                result = sorted(file, reverse=False)
            elif argument == "desc":
                result = sorted(file, reverse=True)
        elif command == "limit":
            obj = int(argument)
            result = list(file)[:obj]

    return result


def make_dictionary(parameter):
    dictionary = {}
    parameters = parameter.split("|")
    for item in parameters:
        query_request = item.split(":")
        dictionary[query_request[0]] = query_request[1]
    return dictionary


