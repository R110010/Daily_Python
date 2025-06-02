# binary search
class Search_array:
    def __init__(self,data):
        self.data = data

    def binary_search(self,target):
        left, right = 0, len(self.data)-1
        while left <= right:
            mid = (left + right) //2
            if self.data[mid]==target:
                return mid
            elif mid < target:
                left = mid +1
            else:
                right = mid -1
        return False
    
arr = [2,5,3,7,9,45,67,12]
bs = Search_array(arr)
res = bs.binary_search(6)
print(res)