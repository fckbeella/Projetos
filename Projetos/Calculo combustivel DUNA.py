aviões = {
    "Diamond Da62": {"MaxFuel": 596, "FuelPerHour": 99.16, "Range": 1283},
    "Cub Crafters Xcub": {"MaxFuel": 276, "FuelPerHour": 59.63, "Range": 695,},
    "Cessna 172": {"MaxFuel": 336, "FuelPerHour": 46.90, "Range": 640,},
    "Cessna 152": {"MaxFuel": 156, "FuelPerHour": 40.20, "Range": 415,},
    "Cessna CJ4": {"MaxFuel": 5762, "FuelPerHour": 1159.10, "Range": 2165,},
    "TBM 930": {"MaxFuel": 1956, "FuelPerHour": 361, "Range": 1784,},
}
def calcular_combustivel(modelo, distancia):
        max_fuel = aviões[modelo]["MaxFuel"]
        fuel_per_hour = aviões[modelo]["FuelPerHour"]
        combmin = (distancia/max_fuel)*fuel_per_hour
        return combmin

def main():
    while True:
        print('=' * 50)
        print("Calculadora de Combustível para Aviões".center(50))
        print('=' * 50)
        print("1 - Calcular quantidade mínima de combustível")
        print("2 - Sair")
        print('=' * 50)
        escolha = input("Escolha uma opção: ")
        print('=' * 50)
        if escolha == "1":
            modelo = input("Informe o modelo do avião: ").title()
            distancia = float(input("Informe a distância desejada (milhas): "))
            if modelo not in aviões:
                print(f"O modelo de avião '{modelo}' não está na lista.")
                max_fuel = float(input("Informe a capacidade máxima de combustível do avião (libras): "))
                fuel_per_hour = float(input("Informe o consumo de combustível por hora do avião (libras/hora): "))
                range_aviao = float(input("Informe o range máximo do avião (milhas): "))
                aviões[modelo] = {"MaxFuel": max_fuel, "FuelPerHour": fuel_per_hour, "Range": range_aviao}
                print(f"Modelo '{modelo}' adicionado à lista de aviões.")
            elif distancia > aviões[modelo]["Range"]:
                print(f'A distancia deseja não é compatível com o modelo {modelo}.')
            else:
                print(f'A quantidade minima de combustivel: {calcular_combustivel(modelo, distancia):.2f} libras')
        elif escolha == "2":
            break
        else:
            print("Opção inválida. Tente novamente.")

main()
