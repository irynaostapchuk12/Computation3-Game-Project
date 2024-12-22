progress_dict = {"level_1": False,
                 "level_2": False,
                 "level_3": False}

def store_progress(level):
    if level == "level_2":
        progress_dict["level_1"] = True

    elif level == "level_3":
        progress_dict["level_2"] = True

    elif level == "the_end":
        progress_dict["level_3"] = True