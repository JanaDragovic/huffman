import math
import sys

# funkcija za unos simbola i njihovih verovatnoca
# simboli i kodovi se cuvaju kao recnici u formatu { 'simbol': verovatnoca }


# funkcija za unos simbola i njihove gustine raspodele verovatnoce 
def unos_gustine_raspodele_verovatnoce():
    raspodela = {}
    n = int(input("Unesite broj simbola: "))

    for i in range(1, n + 1):
        simbol = input(f"Unesite simbol {i}: ")
        verovatnoca = float(input(f"Unesite verovatnocu pojavljivanja simbola {simbol}: "))
        raspodela[simbol] = verovatnoca

# provera da li je zadovoljen uslov da je ukupna verovatnoca jednaka 1
    ukupna_verovatnoca = sum(raspodela.values())
    if ukupna_verovatnoca != 1.0:
        print("Verovatnoce nisu jednake 1")
        sys.exit()
    return raspodela



def hafmen(p):

    # proveravamo da li su uneta samo dva simbola
    # ako jesu, proizvoljno im dajemo vrednosti 0 i 1
    if len(p) == 2:
        return dict(zip(p.keys(), ['0', '1']))

    # Spajamo dva simbola sa najnizim verovatnocama pojavljivanja
    p_prim = p.copy()
    a1, a2 = lowest_prob_pair(p)
    p1, p2 = p_prim.pop(a1), p_prim.pop(a2)
    p_prim[a1 + a2] = p1 + p2

    # rekurzivno pozivamo funkciju i vrsimo kodiranje na osnovu 
    # nove gustine raspodele funkcije verovatnoce 
    
    c = hafmen(p_prim)
    ca1a2 = c.pop(a1 + a2)
    c[a1], c[a2] = ca1a2 + '0', ca1a2 + '1'

    return c

# funkcija koja vraca par simbola sa najnizim verovatnocama 
def lowest_prob_pair(p):
    # u recniku moraju postojati minimum dva simbola
    assert len(p) >= 2  

    sortirani_p = sorted(p.items(), key=lambda x: x[1])
    return sortirani_p[0][0], sortirani_p[1][0]

# trazimo unos od korisnika
unos = unos_gustine_raspodele_verovatnoce()

# Funkcija za odredjivanje da li su kodovi prefiksi jedni drugih
def prefix(code1, code2):
    return code1.startswith(code2) or code2.startswith(code1)


# Racunanje entropije
def racunanje_entropije(raspodela_verovatnoce):
    entropija = 0.0

    for verovatnoca in raspodela_verovatnoce.values():
        entropija -= verovatnoca * (math.log(verovatnoca,2) if verovatnoca > 0 else 0)

    return entropija


# Hafmenov kod 
hafmenov_kod = hafmen(unos)
print("Hafmenov kod:", hafmenov_kod)

# Entropija
entropija = racunanje_entropije(unos)
print("Entropija:", entropija)


# provera da li je kod trenutan prolazenjem kroz izlazni recnik
# provera se vrsi tako sto se ispituje da li su neki od kodova u prefiksnoj vezi

simboli = list(hafmenov_kod.keys())
for i in range(len(simboli)):
    for j in range(i + 1, len(simboli)):
        simbol_i, simbol_j = simboli[i], simboli[j]
        if prefix(hafmenov_kod[simbol_i], hafmenov_kod[simbol_j]) or prefix(hafmenov_kod[simbol_j], hafmenov_kod[simbol_i]):
            print(f"Generisani Hafmenov kodovi {hafmenov_kod[simbol_i]} i {hafmenov_kod[simbol_j]} su prefiksi jedni drugih.")
        
print("Kod je trenutan")

