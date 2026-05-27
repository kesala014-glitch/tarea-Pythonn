Menu_Perros_al_carbon=[
("Perro Caliente","Comida Rapida", 16000),
("Hamburguesa","Comida Rapida", 30000),
("Coca Cola","Bebida", 5000),                  
("Jugo de lulo ","Bebida", 4500),
("Granizado","Postre", 16500),
("Torta de chocolate","Postre", 9000)
]
    ##Definición de la lista de productos con el menú del restaurante "Perros al Carbón"
    
Objetivo_categoria="Comida Rapida"   
    ## DEFINICIÓN DE LA CATEGORÍA OBJETIVO PARA APLICAR LOS DESCUENTOS COMO LOS PIDIERON  EN LA ACTIVIDAD
Umbral=20000                         
    ## DEFINICIÓN DEL UMBRAL DE PRECIO PARA APLICAR EL DESCUENTO 
def Precio_final(producto, categoria_objetivo, umbral): 
    nombre = producto[0]
    categoria = producto[1]
    precio = producto[2]
    ## DEFINICIÓN DE LA FUNCIÓN PARA CALCULAR EL PRECIO FINAL DE UN PRODUCTO DADO SU NOMBRE, CATEGORÍA Y PRECIO.
    
    if categoria == categoria_objetivo:
        if precio > umbral:
            precio_final = precio - (precio * 0.15)  
     ## Si el producto pertenece a la categoría objetivo y su precio es mayor que el umbral, se aplica un descuento del 15%
        else:
            precio_final = precio
    else:
        precio_final = precio  
    ## Si el producto no pertenece a la categoría objetivo, no se aplica ningún descuento y el precio final es igual al precio original.
         
    return precio_final 
    ## La función devuelve el precio final del producto después de aplicar el descuento si lo ve necesario.

print("\n NOVEDADES DE PRECIOS Y PROMOCIONES EN PERROS AL CARBON ")
print(f"{'Producto':<20} | {'Precio Base':<12} | {'Precio Final':<12}") 
    ## Impresión del encabezado de la tabla con formato de alineación para los nombres de los productos, precios base y precios finales.
print("-" * 50)

for elemento in Menu_Perros_al_carbon:
    nombre_prod = elemento[0]        
    precio_base_prod = elemento[2]   
    
    resultado_final = Precio_final(elemento, Objetivo_categoria, Umbral) 
    ## Calculo del precio final aplicando la función de descuento según la categoría y el umbral definido.
    
    print(f"{nombre_prod:<20} | ${precio_base_prod:<11,.0f} | ${resultado_final:<11,.0f}") 
    ## Impresión del resultado final y alineación para una presentación clara de los precios base y finales de cada producto en el menú.