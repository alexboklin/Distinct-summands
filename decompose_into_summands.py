sum = int(input())

components = set()
i = 0
current = 0

while sum - current != 0:
    i += 1
    components.add(i)
    if  sum - (current + i) in components:
        components.remove(i)
        continue
    else:
        current += i
        
print(len(components))
print(" ".join(map(str, components)))
