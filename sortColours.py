#Initialize three pointers: `red`, `white`, and `blue`.
#Set `red` to 0, `white` to 0, and `blue` to the length of the array minus 1.
#While `white` is less than or equal to `blue`:
#  If the value at `white` is 0:
#    Swap the values at `red` and `white`.
#    Increment `red` and `white`.
#  Else if the value at `white` is 1:
#    Increment `white`.
#  Else:
#    Swap the values at `white` and `blue`.
#    Decrement `blue`.

#function to sort the list
#get the length of the list
#loop through the list from the first item
#second loop running from the second item
#compare the first item with the seconf item and swap them

#For example: [45,10,63,40,50,80], the output will be [10,40,45,50,63,80]
#so for this case [2,1,0] for colours will be [0,1,2] which is [red, white, blue]

class Solution(object):
    def sortColors(self, nums):
        red = 0
        white = 0
        blue = len(nums) - 1
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
solution = Solution()
nums1 = [2,0,2,1,1,0]
solution.sortColors(nums1)
print(nums1)  
