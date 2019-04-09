from random import choice

def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = choice(nums)
   l_nums = [n for n in nums if n < q]
 
   e_nums = [q] * nums.count(q)
   b_nums = [n for n in nums if n > q]
   return quicksort(l_nums) + e_nums + quicksort(b_nums)

Array = []
nums = []
Array = input('Введите массив: ')
for s in Array.split():
    nums.append(int(s))

nums = quicksort(nums)
print(nums)

    

            
