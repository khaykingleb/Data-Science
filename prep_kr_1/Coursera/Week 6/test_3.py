n = int(input())
vil = list(map(int, input().split()))
# Здесь создали 3-е поле для номера бомбоубежища
for i in range(n):
    vil[i] = [vil[i], i + 1, 0]
vil.sort()

m = int(input())
bomb = list(map(int, input().split()))
for i in range(m):
    bomb[i] = [bomb[i], i + 1]
bomb.sort()

# Точка нахождения нужного бомбоубежища
idx = 0
for i in range(n):
    # Чтобы минимум был точно больше любого найденного
    dist = 10e9
    for j in range(idx, m):
        tmp_dist = abs(vil[i][0] - bomb[j][0])
    # Либо обновляем минимум и номер бомбоубежища
        if tmp_dist < dist:
            idx = j
            dist = tmp_dist
            vil[i][2] = bomb[j][1]
    # Либо заканчиваем цикл
        else:
            break

vil.sort(key=lambda x: x[1])
for v in vil:
    print(v[2], end=" ")
