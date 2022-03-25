'''
*
* *
* * *
* * * *
'''
# for i in range(1, 5):
#     print('* ' * i)

'''
* * * *
* * *
* *
*
'''
# for i in range(4, 0, -1):
#     print('* ' * i)

'''
      * 
    * * 
  * * * 
* * * * 
'''
# for item in range(1, 5):
#     print(f"{'* ' * item :>10}")

'''
* * * * 
  * * * 
    * * 
      * 
'''
# for i in range(4, 0, -1):
#     print(f"{'* ' * i:>8}")

'''
   *    
  * *   
 * * *  
* * * * 
'''
# for i in range(1, 5):
#     print(f"{'* ' * i:^8}")

'''
* * * * 
 * * *  
  * *   
   *  
'''
# for i in range(4, 0, -1):
#     print(f"{'* ' * i:^8}

'''
   *    
  * *   
 * * *  
* * * * 
 * * *  
  * *   
   *    
   '''
# for i in range(1, 5):
#     print(f"{'* ' * i:^8}")
# for i in range(3, 0, -1):
#     print(f"{'* ' * i:^8}")

'''
1 
1 2 
1 2 3 
1 2 3 4 
'''
# for i in range(1, 5):
#     for j in range(1, i+1):
#         print(j, end=' ')
#     print()
#or
# ref = ''
# for i in range(1, 5):
#     ref += str(i) + ' '
#     print(ref)

'''
        1 
      1 2 
    1 2 3 
  1 2 3 4 
  '''
# ref = ''
# for i in range(1, 5):
#     ref += str(i) + ' '
#     print(f"{ref :>10}")

'''
    1     
   1 2    
  1 2 3   
 1 2 3 4  
'''
# ref = ''
# for i in range(1, 5):
#     ref += str(i) + ' '
#     print(f"{ref :^10}")

''' * 
    * * 
    * 
    * * * 
    * 
    * * * * 
    * 
    * * * * * '''

# for i in range(1, 6):
#     print('*')
#     print('* ' * i)

'''
a
a b 
a b c 
a b c d 
'''
new = ''
# for item in range(ord('a'), ord('e')):
#     new += chr(item) + '  '
#     print(new)

# for item in 'abcd':
#     new += item + ' '
#     print(new)
'''
A
A B
A B C
A B C D
'''

'''
A
A
A
A B
A
A B C
A 
A B C D 
'''
# res = ''
# for item in range(ord('A'), ord('E')):
#     print('A')
#     res += chr(item) + ' '
#     print(res)


