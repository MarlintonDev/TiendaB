from colorama import Fore, Style, init
from Inventario import Inventario, buscar_producto_por_Producto

init(autoreset=True)

def mostrar_pantalla_venta():
    # TODO ESTO ahora está dentro de la función (mira la sangría/espacios)
    print("\n" + Fore.YELLOW + Style.BRIGHT + "================== MÓDULO DE VENTA ==================")
    print(Fore.YELLOW + "-----------------------------------------------------")

    try:
        # 1. Pedimos el Nombre del producto
        Producto_art = input(f"{Fore.WHITE}Ingrese el Nombre del producto: {Fore.CYAN}")
        
        # 2. Buscamos el producto en el inventario
        prod_encontrado = buscar_producto_por_Producto(Producto_art)

        if prod_encontrado:
            # Extraemos los datos (usando las mayúsculas correctas de tu Inventario)
            nombre = prod_encontrado["Producto"]
            precio = prod_encontrado["Precio"]
            stock_actual = prod_encontrado["Stock"]

            print(f"{Fore.GREEN}Producto seleccionado: {Fore.WHITE}{nombre}")
            print(f"{Fore.GREEN}Precio unitario:     {Fore.WHITE}${precio}")
            print(f"{Fore.GREEN}Stock disponible:    {Fore.WHITE}{stock_actual}")

            # 3. Pedimos la cantidad
            cantidad = int(input(f"{Fore.YELLOW}Cantidad a vender:   {Fore.WHITE}"))

            if cantidad <= stock_actual:
                total = precio * cantidad
                
                # --- DISEÑO DEL RECIBO ---
                print("\n" + Fore.GREEN + "================ RECIBO DE VENTA ================")
                print(f"{'PRODUCTO':<20} | {'PRECIO':>10} | {'CANT':>5}")
                print("-" * 43)
                print(f"{nombre:<20} | {f'${precio:,.0f}':>10} | {cantidad:>5}")
                print("-" * 43)
                # Tu gran mejora: el $ junto al total
                print(f"{Style.BRIGHT}{'TOTAL A PAGAR:':<20} | {f'${total:,.0f}':>16}")
                print(Fore.GREEN + "=================================================")
                
                # Actualizar el stock en memoria
                prod_encontrado["Stock"] -= cantidad
                print(f"{Fore.MAGENTA}Stock actualizado: {prod_encontrado['Stock']} unidades.")
                
            else:
                print(Fore.RED + f"\n[!] Error: Solo hay {stock_actual} unidades disponibles.")
        else:
            print(Fore.RED + "\n[!] Error: El producto ingresado no existe en el inventario.")

    except ValueError:
        print(Fore.RED + "\n[!] Error: Ingresa solo números en la cantidad.")
    except Exception as e:
        print(Fore.RED + f"\n[!] Ocurrió un error inesperado: {e}")
        
#mostrar_pantalla_venta()        