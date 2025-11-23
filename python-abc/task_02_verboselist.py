#!/usr/bin/python3

class VerboseList(list):

    def append(self, item):
        super().append(item)
        print('Added {} to the list.'.format(item))

    def extend(self, iterable):
        len = len(self)
        super().extend(iterable)
        it_added = len(self) - len
        print("Extended the list with {} items.".format(it_added))

    def remove(self, value):
        super().remove(value)
        print("Removed {} from the list.".format(value))

    def pop(self, idx = -1):
        try:
            it = self[idx]
        except IndexError:
            raise
        super().pop(idx)
        print("Popped {} from the list.".format(it))