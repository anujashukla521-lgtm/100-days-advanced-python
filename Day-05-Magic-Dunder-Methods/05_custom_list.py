class MyList:
    def __init__(self, lists):
        self.lists = lists

    def __getitem__(self, key):
        return self.lists[key]

numbers = MyList([10,20,30,40])
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])