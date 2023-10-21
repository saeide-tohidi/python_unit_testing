def counter(name):
    if name.isalpha():
        return len(name)
    else:
        raise Exception("it should be string")


print(counter("Jak"))
