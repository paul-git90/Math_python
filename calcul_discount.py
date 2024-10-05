'''
calcul discount
'''


def aplica_discount(pret_initial, procent_discount):

    # Calculează valoarea discountului

    print(f'pret initial = {pret_initial}')
    print(f'procent discount = {procent_discount}%')

    valoare_discount = pret_initial * (procent_discount / 100)  # pret cu discount = pret produs * (discount / 100)

    print(f'rezultat valoare_discount = {valoare_discount}')

    # Calculează prețul final după aplicarea discountului

    pret_final = pret_initial - valoare_discount  # din valoarea pretului initial se scade discountul rezultat

    print(f'rezultat pret final = {pret_final}')

    return pret_final

# Exemplu de utilizare

pret_initial = 34900  # de exemplu, 34900 de Euro
procent_discount = 30  # de exemplu, 30%

print('---' * 10)

pret_final = aplica_discount(pret_initial, procent_discount)  # var pret_final = aplica_discount => functia definita

print(f"Prețul inițial: {pret_initial} Euro")
print(f"Procentul de discount: {procent_discount}%")
print(f"Prețul final după aplicarea discountului: {pret_final} Euro")
