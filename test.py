Evropa = [["Slovenija","link_slovenija"],["Avstrija","link_avstrija"],["Italija","link_italija"]]
geslo = "Slovenija"
def test(geslo,celina):
    for i,sez in enumerate(celina):
        if geslo in sez:
            x = 1+i
        else:
            continue
    return x