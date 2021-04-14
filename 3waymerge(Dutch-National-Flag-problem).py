class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = nums
        runner = 0
        beforezero = 0
        aftertwo = len(arr)-1
        for i in arr:
            if arr[runner] == 1:
                runner += 1
                continue
            elif arr[runner] == 0:
                arr[beforezero], arr[runner] = arr[runner],  arr[beforezero]
                beforezero += 1
                runner += 1
                continue
            else:
                arr[aftertwo], arr[runner] = arr[runner],  arr[aftertwo]
                aftertwo -= 1
                # runner += 1
                continue
        print(arr)

