S, P = map(int, input().split())
DNA = input()
DNA_PASSWORD = list(map(int, input().split()))

NEW_PASSWORD = [0] * 4
answer = 0

for i in range(P):
    char = DNA[i]
    if char == 'A':
        NEW_PASSWORD[0] += 1
    elif char == 'C':
        NEW_PASSWORD[1] += 1
    elif char == 'G':
        NEW_PASSWORD[2] += 1
    elif char == 'T':
        NEW_PASSWORD[3] += 1

valid_password = True
for j in range(4):
    if NEW_PASSWORD[j] < DNA_PASSWORD[j]:
        valid_password = False
        break

if valid_password:
    answer += 1

for i in range(1, S - P + 1):
    prev_char = DNA[i - 1]
    if prev_char == 'A':
        NEW_PASSWORD[0] -= 1
    elif prev_char == 'C':
        NEW_PASSWORD[1] -= 1
    elif prev_char == 'G':
        NEW_PASSWORD[2] -= 1
    elif prev_char == 'T':
        NEW_PASSWORD[3] -= 1

    new_char = DNA[i + P - 1]
    if new_char == 'A':
        NEW_PASSWORD[0] += 1
    elif new_char == 'C':
        NEW_PASSWORD[1] += 1
    elif new_char == 'G':
        NEW_PASSWORD[2] += 1
    elif new_char == 'T':
        NEW_PASSWORD[3] += 1

    valid_password = True
    for j in range(4):
        if NEW_PASSWORD[j] < DNA_PASSWORD[j]:
            valid_password = False
            break

    if valid_password:
        answer += 1

print(answer)