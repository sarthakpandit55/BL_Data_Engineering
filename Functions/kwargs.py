def describe_outfit(name, **clothing_items):

    """
    this function is describing the outfit of a clothing item.
    Input: name (positional argument), clothing_items (keyword argument)
    output: description of the outfit of a clothing item
    """

    if not clothing_items:
        return f"{name} is currently wearing nothing special."
    else:
        description = []
        for key, value in clothing_items.items():
            description.append(f"{key}: {value}")
        string = ", and ".join(description)
        return f"{name} is wearing a {string}"

print(describe_outfit("Sarthak", shirt="blue linen", pant="Black cotton"))
