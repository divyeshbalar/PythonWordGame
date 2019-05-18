# import math;
# from array import *;
# import queue;
# import game;
#
# # x = int(input("Enter the nunmber"));
# # if x%2 == 0:
# #     print( x, " is even number");
# # else:
# #     print(x, " odd number");
# #
# #
# #
# # for i in range(2,int(math.sqrt(x)), 1):
# #     if x%i == 0:
# #         print("Not prime")
# #         break;
# # else:
# #     print("is prime number");
#
# # q = queue.Queue();
# # q.put(game.game("one"))
# # q.put(game.game("second"))
# # g = q.get(0)
# # g1 = q.get(1)
# # print(q.qsize())
# #g.claculateInitialTotal()
# print("----------------------------")
# arr = array('i', [1,2,3,4,5,50]);
# # you can not add other data typed values, 'i' is typeCode
# print(arr);
# print(arr.buffer_info())
# # this will returns the memory address and the size of the array
# print(arr.typecode)
# # will return the typeCode which is 'i' here and also got methods like append() remove() and reverse()
# print(arr[0:4]);
#
# newArr = array(arr.typecode, (a*a for a in arr[0:4]));
# print(newArr)
