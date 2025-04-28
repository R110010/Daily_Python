# Binary Search
# Use binary search to find a given number from a sorted array.
class Search_array:
    def __init__(self,data):
        self.data = data

    def binary_search(self,target):
        left, right = 0, len(self.data)-1
        while left <= right:
            mid = (left + right) //2
            if self.data[mid]== target:
                return mid
            elif self.data[mid]<target:
                left = mid +1
            else:
                right = mid -1
        return False
    
arr = [2,4,5,13,17,22,35,46,59,80,93]
sa = Search_array(arr)
res = sa.binary_search(200)
print(f"Search result found at index {res}.")