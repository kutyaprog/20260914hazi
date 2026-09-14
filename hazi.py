import math as matek
"""
#1
nev = str(input("Neved: "))
ev = int(input("Születési éved: "))
print(f"Kedves {nev}! {ev} évben szüledtél!")
kor = 2026-ev
print(f"Kedves {nev}! {kor} éves vagy!")

#1 Újra...

a = int(input("Elso szam: "))
b = int(input("Masodik szam: "))
print(f"A két szám összege: {a+b}")
print(f"A két szám különbsége: {a-b}")

#2
szam = float(input("Kérlek adj meg egy valós számot: "))
print(f"A szám tízszerese: {szam*10}")

#3
tav = float(input("Kérlek add meg a megtett távolságot (km): ")) #lehetne akár int is
ido = float(input("Kérlek add meg az időt (óra): "))
# V=s/t vagyis tav/ido Hell yeah i'm not stuupid
magicfizika = tav/ido #ez mintha nem kellett volna lol
print(f"Az átlagsebesség: {tav/ido} km/h")

#4
alap = float(input("Kérlek add meg a háromszög alapját (m): ")) #lehetne akár int is
magassag = float(input("Kérlek add meg a magasságot (m): ")) #lehetne akár int is
print(f"A háromszög területe: {alap*magassag/2} négyzetméter")
#T=(a*ma)/2

#5
tetszoleges_egeszszam = int(input("adj meg egytetszőleges egész számot:  "))
print(f"{tetszoleges_egeszszam*2}")

#6
egesz_szam = int(input("egész szám: "))
print(f"{egesz_szam**2} a négyzet {egesz_szam**3} a köb")

#7
fok = float(input("Kérj be egy hőmérsékletet Celsius fokban és számold ki, hogy hány Fahrenheit foknak felel meg a beírt érték: "))
print(f"{fok*9/5+32} = Celsius * 9/5 + 32")

#8
al8ap = float(input("alap: "))
kitevo = int(input("kitevő: "))
print(f"{al8ap**kitevo}")

#9
ahhhhh = int(input("szam1: "))
bhhhhh = int(input("szam2: "))
print(f"{ahhhhh*2+bhhhhh/2}")

#10
gdfhdf = float(input("Kérj be egy pozitív lebegőpontos számot (távolság kilométerben)"))
hgfdhj = float(input("egy pozitív lebegőpontosszámot (fogyasztás literben/km)"))
print(f"{gdfhdf*hgfdhj}")

#11
oradij = float(input("be egy pozitív lebegőpontos számot (óradíj): "))
munkaora = int(input("egy pozitív egész számot (munkaórákszáma): "))
print(f"{oradij*munkaora}")

#12
radius = float(input("Kérjen be egy kör sugarát: "))
print(f"kerület: {2*radius*matek.pi} terület: {matek.pi*radius**2}")

#13
eletkor = int(input("Kérj be egy pozitív egész számot (életkor): ")) #unused
atlnapi= float(input("egy pozitív lebegőpontos számot (átlagos napialvásszükséglet): "))
print(f"{atlnapi*30} havi átlag alvás idő")

#14
lepes = int(input("Kérj be egy pozitív egész számot (átlagos napi lépésszám)"))
print(f"{lepes*7} heti átlag")
atlnapilepeshetente = int(input("egy pozitív egész számot (átlagos napi lépések száma egy héten átlagolva): "))
print(f"{atlnapilepeshetente*1}") #I have no clue what does this feladat want from me már alapból átlagolva van vagy IDK ehhez nem vagyok eléggé kiképezve

#15

nevet = str(input("Kérj be egy nevet: "))
stuff = str(input("hogy mit szeretne megvenni -mire gyűjt: "))
ar = int(input("ára: "))
zsp = int(input("Kérj be egy pozitív egész számot (heti zsebpénz): "))
kiadas = int(input("egy pozitív egész számot (heti kiadás): "))
print(f"{nevet} {stuff} {matek.ceil(ar / (zsp-kiadas))}")

#16

magassagnak = float(input("magasságod(m): "))
testsuly = float(input("Súly (kg): "))
print(f"BMI {testsuly/magassag**2}")

#17
alomsuly = float(input("Célsúly"))
print(f"első hét végére: {testsuly-(testsuly-alomsuly/3)} \n második hét végére: {testsuly-(testsuly-alomsuly/3*2)} \n harmadik hét végére {testsuly-(testsuly-alomsuly)}")
"""

"""
első hét testsuly-(testsuly-alomsuly/3)
második hét testsuly-2*(testsuly-alomsuly/3)
harmadik hét alomsuly
"""

#18

keret = int(input("keret normál ára:"))
lencse = int(input("lencse normál ára:"))
year_curr = int(input("Jelenlegi év :"))
birth_year = int(input("születési év :"))

print(f"Ön a szemüvegkeret árából, ami {keret} Ft, {year_curr-birth_year}% kedvezményt kap! \n A szemüveglencse ára: {lencse} Ft \n ---------------------------- \n Szemüveg vételára : {round(keret*(1-((year_curr-birth_year)/100))+lencse)}")







