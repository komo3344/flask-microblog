win = 13031
lose = 20
result = (win/(win+lose))
count = 0
print(result)
while True:
    if result >= 0.999:
        break
    win = win + count
    count = count + 1
print(count)
