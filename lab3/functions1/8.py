def spy_game(nums):
    cnt = 0
    num = sorted(nums)
    for i in num:
        if i == 0:
            cnt += 1
        elif i == 7 and cnt >= 2:
            return True
    return False
