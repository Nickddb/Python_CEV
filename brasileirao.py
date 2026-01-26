print("\033[4mBRASILEIRÃO TOP 20\033[m")
brasileirao = 'Atlético-MG', 'Botafogo', 'Athletico-PR', 'Chapecoense', 'Coritiba', 'Flamengo', 'Vasco', 'Cruzeiro', 'Bahia', 'EC Vitória', 'Fluminense', 'Grêmio', 'Mirassol', 'Bragantino', 'Remo', 'Santos', 'São Paulo', 'Corinthians', 'Internacional', 'Palmeiras'.strip()
chapecoense = brasileirao.index('Chapecoense') + 1
print("5 primeiros: \033[2;35m", brasileirao[0:5], "\033[m")
print("Últimos 4 colocados: \033[1;34m", brasileirao[-4:], "\033[m")
print("Posição do Chapecoense: ", chapecoense)
print(f"Times em ordem alfabética: {sorted(brasileirao)}")