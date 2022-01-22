def get_query(file, query):
    file = map(lambda x: x.strip(), file)
    result = ""
    query_parameters = query.split("|")
    for item in query_parameters:
        query_request = item.split(":")
        command = query_request[0]
        argument = query_request[1]
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


