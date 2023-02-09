

def get_even(list_of_nums):
    c = 0
    while c < len(list_of_nums):
        iter_value = list_of_nums[c]
        if iter_value % 2 == 0:
            yield (iter_value, c)
        c += 1


def get_even2(list_of_nums):
    for i in list_of_nums:
        if i % 2 == 0:
            yield i
        


L = [2, 3, 4, 7, 7, 13, 8, 10] # len - 8


# print("Before filter: " + str(L))


# print("Only even: ", end="")

# for i in get_even(L):
#     print(i, end=" ")


gen = get_even(L)

print(gen.__next__()[0])
print(gen.__next__()[0])


# while True:
#     try:
#         res = gen.__next__()
#         print(res)
#     except:
#         print('Stop Iteration')
#         break


# for i in range(10):
    # if i % 2 == 0:
        # print('I is:', i)

# rang = range(10)
# while True:
# print(rang)
