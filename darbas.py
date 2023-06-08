# Užduotį atliko: ???,  kl. ???

# UŽDUOTIS 01: #################################################################
'''
Parašykite programą, kuri gautų iš vartotojo sveikąjį skaičių
ir atvaizduotų jį trupmeninės dalies skaitmenimis (t.y.,
"skaičiais po kablelio") be reikšmės apvalinimo ir po suapvalinimo.
Naudodamiesi tik duotais kintamaisiais atlikite veiksmus
kurių pagalba būtų gaunamas toks dialogo su programa pvz.:
Įveskite 4-ženklį skaičių: 4561

\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
\	0.4561	\	0.46	\
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

Užduoties sąlygos:
    programa turi pasileisti be klaidos pranešimų, t.y., "veikti";
    šio failo pavadinimas turi likti nepakitęs,
        pvz., užduočiai "UŽDUOTIS 01" - "UZDUOTIS01.py";    
    duoti kintamieji (išskyrus kintamuosius: v, t) tūri likti nepakitę;
    naudokite tik duotuosius kintamuosius, t.y., naujų nekurkite;

    "lentelės" atspausdinimas turi būti atliekamas viena print() funkcija;
    "lentelėje" neturi būti naudojamų tarpo (" ") simbolių;
    skaičiaus apvalinimui naudokite simbolių eilučių metodą format().
'''
###############################################################################

#import UZDUOTIS01_TEST

# =======================

# Duoti kintamieji

m = "Įveskite 4-ženklį skaičių: "
s = "\\"
v = None
t = ""

# -----------------------

# Skaičiaus įvedimas ir apdorojimas
skaicius = int(input(m))

t = skaicius / 10000
print(t)

t = round(t, 4)
print(s)

t = round(t, 2)
print(t)

