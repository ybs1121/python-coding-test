def solution(nums):
    answer = 0
    max_kind = len(nums) // 2
    not_duplicate_nums = set(nums)
    if len(not_duplicate_nums) < max_kind:
        
        return len(not_duplicate_nums)
    else:
        return max_kind