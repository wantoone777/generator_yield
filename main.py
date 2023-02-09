

def get_even(list_of_nums):
    c = 0
    while c < len(list_of_nums):
        iter_value = list_of_nums[c]
        if iter_value % 2 == 0:
            yield (iter_value, c)
            print(iter_value, 'was') # optional. Shows previous value. First iteration do not get there.
        c += 1


def get_even2(list_of_nums):
    for i in list_of_nums:
        if i % 2 == 0:
            yield i
        
# def test_gen():
#     if True:
#         yield True


# test_g = test_gen()
# print(test_g.__next__()) works only one iteration [yiled True] once


L = [2, 3, 4, 7, 7, 13, 8, 10] # len - 8


# print("Before filter: " + str(L))


# print("Only even: ", end="")

# for i in get_even(L):
#     print(i, end=" ")


gen = get_even(L)
counter = 0
try:    
    print(gen.__next__()[0])
except:
    print('Stop Iteration :(')
    counter += 1
    if counter > 3:
        print('Fatal')
try:    
    print(gen.__next__()[0])
except:
    print('Stop Iteration :(')
    counter += 1
    if counter > 3:
        print('Fatal')
try:    
    print(gen.__next__()[0])
except:
    print('Stop Iteration :(')
    counter += 1
    if counter > 3:
        print('Fatal')
try:    
    print(gen.__next__()[0])
except:
    print('Stop Iteration :(')
    counter += 1
    if counter > 3:
        print('Fatal')
try:    
    print(gen.__next__()[0])
except:
    print('Stop Iteration :(')
    counter += 1
    if counter > 3:
        print('Fatal')
try:    
    print(gen.__next__()[0])
except:
    print('Stop Iteration :(')
    counter += 1
    if counter > 3:
        print('Fatal')
try:    
    print(gen.__next__()[0])
except:
    print('Stop Iteration :(')
    counter += 1
    if counter > 3:
        print('Fatal')
try:    
    print(gen.__next__()[0])
except:
    print('Stop Iteration :(')
    counter += 1
    if counter > 3:
        print('Fatal')
try:    
    print(gen.__next__()[0])
except:
    print('Stop Iteration :(')
    counter += 1
    if counter > 3:
        print('Fatal')
try:    
    print(gen.__next__()[0])
except:
    print('Stop Iteration :(')
    counter += 1
    if counter > 3:
        print('Fatal')
print(counter)
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
