from colorama import Fore, Back, Style, init
init(autoreset=True)

Inventario = [
    {"Id": 1, "Producto": "Arroz", "Precio": 2500, "Stock": 10,},
    {"Id": 2, "Producto": "Azúcar", "Precio": 3000, "Stock": 50,},
    {"Id": 3, "Producto": "Sal", "Precio": 1500, "Stock": 8,},
    {"Id": 4, "Producto": "Aceite", "Precio": 5000, "Stock": 5,},
    {"Id": 5, "Producto": "Papa", "Precio": 2000, "Stock": 15,},
    {"Id": 6, "Producto": "Tomate", "Precio": 3500, "Stock": 4,},
    {"Id": 7, "Producto": "Cebolla", "Precio": 1800, "Stock": 5,},
    {"Id": 8, "Producto": "Café", "Precio": 8000, "Stock": 4,},
    {"Id": 9, "Producto": "Chocolate", "Precio": 6000, "Stock": 3,},
    {"Id": 0, "Producto": "Leche", "Precio": 4000, "Stock": 6,},
    
    ]

Inventario.sort(key= lambda x: x["Producto"])

def mostrar_inventario():
    print(f"\n{Fore.CYAN}{Style.BRIGHT}================ INVENTARIO ACTUAL ================")
    
    header = f"{'ID':<5} | {'PRODUCTO':<15} | {'PRECIO':<10} | {'STOCK':<8}"
    print(Fore.YELLOW + header)
    print(Fore.YELLOW + "-" * len(header))

    for p in Inventario:
        print(f"{str(p['Id']):<5} | {p['Producto']:<15} | ${str(p['Precio']):<9} | {str(p['Stock']):<8}")

    print(f"{Fore.CYAN}===================================================\n")

# En Inventario.py

def buscar_producto_por_Producto(Producto_buscado):
    # Recorremos el inventario
    for producto in Inventario:
        if producto['Producto'].lower() == Producto_buscado.lower():
            return producto  # Devolvemos el diccionario completo del producto
    return None  # Si no lo encuentra, devuelve "Nada"

#mostrar_inventario()  # Llamamos a la función para mostrar el inventario al iniciar el programa