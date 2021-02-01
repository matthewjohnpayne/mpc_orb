def interpret(arg):
    """
    convenience func to interpret input arg as some kind of json-related input
    returns dict
    """
    
    # try to interpret input as a json-filepath
    if isinstance(arg, str) and os.path.isfile(arg):
        try:
            with open(arg) as f:
                json_dict       = json.load(f)
                input_filepath  = arg
        except Exception as e:
            pass
    
    # if its a dictionary, use that
    elif isinstance(arg, dict):
        json_dict       = arg
        input_filepath  = None
    # no other options yet implemented
    else:
        raise  Exception("Input {arg}\nis of type {type(arg)} and cannot be interpreted as json-dict")
    
    # return the contents of the json file in dict form
    return json_dict,input_filepath

