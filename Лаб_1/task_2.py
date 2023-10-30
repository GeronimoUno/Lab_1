# TODO Найдите количество книг, которое можно разместить на дискете

symb = 4
stroka = symb * 25
stranitca = stroka * 50
kniga = stranitca * 100
Volume_mb = 1.44
Volume_kb = 1.44 * 1024
Volume_b = Volume_kb * 1024
Count = int(Volume_b // kniga)
print("Количество книг, помещающихся на дискету:", Count)
