#!/usr/bin/python3

class VerboseList(list):

    def append(self, item):
        super().append(item)
        print('Added {} to the list.'.format(item))

    def extend(self, iterable):
        lenght = len(self)
        super().extend(iterable)
        it_added = len(self) - lenght
        print("Extended the list with {} items.".format(it_added))

    def remove(self, value):
        super().remove(value)
        print("Removed {} from the list.".format(value))

    def pop(self, index = -1):
        try:
            it = self[index]
        except IndexError:
            raise
        super().pop(index)
        print("Popped {} from the list.".format(it))