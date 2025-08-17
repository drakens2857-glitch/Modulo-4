productos_disponibles = ["manzana", "durazno", "plátano", "fresa", "pera", "kiwi"]

productos_deseados = ["manzana", "kiwi", "pera", "melocoton"]

for producto in productos_deseados:
    disponible = producto in productos_disponibles
    estado = "disponible" if disponible else "no disponible"
    print(f"El producto '{producto}' está {estado}")
