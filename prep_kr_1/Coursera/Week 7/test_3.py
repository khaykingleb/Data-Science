lst = list(map(int, input().split()))
st = set()

for element in lst:
    if element in st:
        print("YES")
    else:
        print("NO")
        st.add(element)
