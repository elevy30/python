from pprint import pprint as pp

store = []


def sort_by_last_letter(strings):
    def last_letter(s):
        return s[-1]

    store.append(last_letter)
    pp(last_letter)
    return sorted(strings, key=last_letter)
