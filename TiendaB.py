import os  # Importante para limpiar la pantalla
from colorama import Fore, Style, init
from Inventario import mostrar_inventario
from Venta import mostrar_pantalla_venta

init(autoreset=True)

def limpiar_pantalla():
    # Limpia la consola según el sistema operativo (Windows o Linux/Mac)
    os.system('cls' if os.name == 'nt' else 'clear')

# --- BUCLE PRINCIPAL ---
while True:
    limpiar_pantalla()
    print("\n" * 2)
    print(Fore.GREEN + "========================================")
    print(Fore.GREEN + "================= " + Fore.WHITE + "Menú" + Fore.GREEN + " =================")
    print(Fore.GREEN + "========================================")
    print(Style.RESET_ALL)
    print("""
            1. Vender
            2. Stock
            0. Salir
          """)

    try:
        Opcion = int(input("    Ingrese un número de la lista: "))
        
        if Opcion == 1:
            limpiar_pantalla()
            mostrar_pantalla_venta()
            # Esta pausa es CLAVE para que no se borre el recibo de inmediato
            input(f"\n{Fore.YELLOW}Presione ENTER para volver al menú...")

        elif Opcion == 2:
            limpiar_pantalla()
            mostrar_inventario()
            input(f"\n{Fore.YELLOW}Presione ENTER para volver al menú...")

        elif Opcion == 0:
            print("\n" + Fore.RED + "================= Salir ================")
            print("\n    Gracias por usar el sistema, TiendaB.\n    ¡Vuelva pronto!")
            print(Fore.RED + "========================================")
            break # Rompe el ciclo y cierra el programa

        else:
            print(Fore.RED + "\n[!] Opción no válida. Intente de nuevo.")
            import time; time.sleep(2) # Espera 2 segundos antes de repetir

    except ValueError:
        print(Fore.RED + "\n[!] Error: Por favor, ingrese un número válido.")
        import time; time.sleep(2)
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n[!] Saliendo por interrupción de teclado...")
        break