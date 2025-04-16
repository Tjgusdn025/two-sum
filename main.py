from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_map = {}  # 숫자 → 인덱스를 저장할 해시맵

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i