# • Dla osób poniżej 4 roku życia wstęp jest bezpłatny.
# • Dla osób w wieku od 4 do 18 lat bilet kosztuje 10zł.
# • Dla osób powyżej 18 roku życia bilet kosztuje 20zł.

a = int(input("Wprowadź wiek klienta: "))
if a < 4:
    print("wstęp jest bezpłatny")
elif a <= 18:
    print("Cena biletu: 10zł")
else:
    print("Cena biletu: 20zł")