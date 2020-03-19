class test:
    count = 0

    def count_add(self, i):

        test.count = i + 1

for i in range(0,10):
    t1 = test()
    t1.count_add(i)
    print(test.count)

