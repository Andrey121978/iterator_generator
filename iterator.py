class FlatIterator:

    def __init__(self, list_of_list):
        self.results = []
        self.list_of_list = list_of_list
        for i in self.list_of_list:
            self.results += i
        self.current_value = 0
        self.end = len(self.results)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_value < self.end:
            element = self.results[self.current_value]
            self.current_value += 1
        else:
            raise StopIteration
        return element


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
