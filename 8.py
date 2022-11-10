count = 0
eq = True
with open("texxt1.txt", "r", encoding = "utf-8") as f1, open("texxt2.txt", "r", encoding = "utf-8") as f2:
      for a1, a2 in zip(f1, f2):
          count += 1
          if a1 != a2:
              eq = False
              break
print(f"Otli4iy net") if eq else print(f"Otli4aetsya stroka {count}")
