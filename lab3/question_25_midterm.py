__author__ = 'pather'


def double(x):
    d = 0
    d = x + x
    return d


def triple_double(x):
    t = 0.0
    t = double(x) + double(x) + double(x)
    return t


def main():
    results = 0.0
    results = double(triple_double(1.0))
    print(results)


# Outputs 12.0
main()