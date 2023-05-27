import ipdb
def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
        return "The line is currently empty."
    else:
        length_str = f"The line is currently: "
        names_strings = []
        for i, name in enumerate(katz_deli):
            names_strings.append(f"{i+1}. {name}")
        name_str = " ".join(names_strings)
        print(length_str + name_str)
        # return length_str + name_str
    pass
def take_a_number(katz_deli, new_customer):
    katz_deli.append(new_customer)
    print(f"Welcome, {new_customer}. You are number {len(katz_deli)} in line.")
    # pass
def now_serving(katz_deli):
    print("Currently serving {}.".format(katz_deli.pop(0)) if len(katz_deli) > 0 else "There is nobody waiting to be served!")
    pass