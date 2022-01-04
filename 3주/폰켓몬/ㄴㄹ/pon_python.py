def solution(nums):
    pon=set(nums)
    
    if len(pon)>=len(nums)//2:
        return len(nums)//2
    else:
        return len(pon)
