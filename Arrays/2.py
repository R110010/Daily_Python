# use binary search in a rotated array.
# arr = [46,59,80,93,2,4,5,13,17,22,35]
class Search_array:
    def __init__(self,data):
        self.data= data
    def binary_search(self,target):
        left, right = 0, len(self.data)-1
        while left <= right:
            mid = (left+right)//2
            if self.data[mid]==target:
                return mid
            if self.data[left]<self.data[mid]:
                if self.data[left]<=target< self.data[mid]:
                    right = mid -1
                else:
                    left = mid +1
            else:
                if self.data[mid]< target <= self.data[right]:
                    left = mid +1
                else:
                    right = mid -1
        return False

arr = [46,59,80,93,2,4,5,13,17,22,35]
ss = Search_array(arr)
res = ss.binary_search(17)
print(res)
