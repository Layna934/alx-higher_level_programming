#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    x = len(names)
    for name in range(0, x):
        if names[name][:2] != "__":
            print("{}".format(names[name]))
