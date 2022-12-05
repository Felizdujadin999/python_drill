for i in range(1, 21, 2):
    asterik = "*" * i
    print(asterik.center(30))

for i in range(21, 0, -2):
    asterik = "*" * i
    print(asterik.center(30))
print()

for i in range(1, 21, 2):
    asterik = "*" * i
    print(f"{asterik:<2}")
print()

for i in range(1, 21, 2):
    asterik = "*" * i
    print(f"{asterik:>21}")
print()
for i in range(21, 0, -2):
    asterik = "*" * i
    print(f"{asterik:<2}")
print()
for i in range(21, 0, -2):
    asterik = "*" * i
    print(f"{asterik:>21}")
