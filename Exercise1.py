class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        

    def __iter__(self):
        self.new_list = []        
        # Сразу переводим в плоский список
        for index in range(len(self.list_of_list)):
            for item in self.list_of_list[index]:
                self.new_list.append(item)
        self.num_next = -1
        
        return self


    def __next__(self):

        self.num_next += 1
        if self.num_next == len(self.new_list):
            raise StopIteration
        
        return self.new_list[self.num_next]



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
