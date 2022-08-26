t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    # print(arr)



    nums = set()
    for i in range(n):
        for j in range(i+1, n):
            num = arr[i] * arr[j]
            nums.add(num)
    # print(nums)


    ans = []

    for x in nums:
        y = x
        danjo = []
        while y != 0:
            danjo.append(y % 10)
            y = y // 10
        # print(danjo)

        if len(danjo) == 1:
            ans.append(x)

        else:
            for a in range(len(danjo)-1):
                # print(danjo[y], danjo[y+1])
                if danjo[a] < danjo[a+1]:
                    ans.append(-1)
                    break

            else:
                ans.append(x)

    print(f'#{tc+1} {max(ans)}')