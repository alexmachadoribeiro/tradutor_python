# instalar 'deep_translator' (pip install deep_translator)
# importa as bibliotecas
import os
from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source="auto", target="pt")

if __name__ == "__main__":
    while True:
        try:
            print("1 - Traduzir texto.")
            print("2 - Sair do programa.")

            opcao = input("Opção desejada: ")

            os.system("cls")

            match opcao:
                case "1":
                    texto_original = input("Digite o texto a ser traduzido: ")
                    texto_traduzido = tradutor.translate(texto_original)

                    print("\nTRADUÇÃO:\n")
                    print(f"{texto_traduzido}\n")
                    continue
                case "2":
                    break
                case _:
                    print("Opção inválida.")
                    continue
        except Exception as e:
            print(f"Não foi possível traduzir o texto. {e}.")
            continue