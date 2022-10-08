t = int(input())
for tc in range(t):
    n = int(input())
    card = list(map(int, input().split()))
    # print(n, card)

    card_copy = []
    visited = []

    for i in range(len(card)):
        card_copy.append((i+1, card[i]))
    # print(card_copy[1][1])

    while len(card_copy) > 1:
        for j in range(len(card_copy)//2):

            if card_copy[j*2][1] == 1:
                if card_copy[j*2+1][1] == 1:
                    visited.append(card_copy[j*2])
                elif card_copy[j*2+1][1] == 2:
                    visited.append(card_copy[j*2+1])
                elif card_copy[j*2+1][1] == 3:
                    visited.append(card_copy[j*2])

            if card_copy[j*2][1] == 2:
                if card_copy[j*2+1][1] == 1:
                    visited.append(card_copy[j*2])
                elif card_copy[j*2+1][1] == 2:
                    visited.append(card_copy[j*2])
                elif card_copy[j*2+1][1] == 3:
                    visited.append(card_copy[j*2+1])

            if card_copy[j*2][1] == 3:
                if card_copy[j*2+1][1] == 1:
                    visited.append(card_copy[j*2+1])
                elif card_copy[j*2+1][1] == 2:
                    visited.append(card_copy[j*2])
                elif card_copy[j*2+1][1] == 3:
                    visited.append(card_copy[j*2])

        if len(card_copy) > (len(card_copy)//2)*2:
            visited.append(card_copy[-1])

        card_copy = visited[:]
        visited.clear()

    print(f'#{tc+1} {card_copy[0][0]}')