num = [27, 4, 0, 2, 7]
print(num)
print("=" * 20)
num[2] = 3
print(num)
num.append(8)
num.sort(reverse = True)
print("=" * 20)
print(num)
num.remove(27)
num.insert(6, 13)
num.pop
print("=" * 20)
print(num)
print(f"Esta lista tem  {len(num)} elementos")
print("=" * 20)

valores = list()
valores.append(9)
valores.append("algo")

print(valores)
print("=" * 20)
for c, v in enumerate(valores):
     print(f"Posição {c}, valor: {v}")
