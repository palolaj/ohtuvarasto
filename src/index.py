from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print(f"Mehuvarasto: {mehua}") 
    print(f"Olutvarasto: {olutta}")

    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

    mehua.lisaa_varastoon(50.7)
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")


if __name__ == "__main__":
    main()
