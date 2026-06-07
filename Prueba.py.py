"""
RECOMENDADOR ALGORÍTMICO DE CAFÉ - SMARTROAST
Descripción: Sistema modular que, mediante la descomposición de problemas, 
guía al usuario en la elección de su café ideal basado en preferencias.
"""

# ─────────────────────────────────────────────
#  VARIABLES GLOBALES (Opciones de validación)
# ─────────────────────────────────────────────

temperatura = ""
opc_temperatura = ["caliente", "fria"]
base = ""
opc_base = ["helado", "instantaneo"]
alcohol = ""
opc_alcohol = ["si", "no"]
tipo_alcohol = ""
opc_tipo_alcohol = ["whisky", "ron"]
agregado = ""
opc_agregado = ["si", "no"]
tipo_agregado = ""
opc_tipo_agregado = ["leche", "chocolate", "crema"]
balance = ""
opc_balance = ["1", "2", "3", "4"]
intensidad = ""
opc_intensidad = ["1", "2", "3", "4"]

# ─────────────────────────────────────────────
#  UTILIDADES
# ─────────────────────────────────────────────

def pedir_opcion(pregunta, opciones_validas):
    """
    Función de validación: Solicita un dato, lo normaliza y 
    comprueba que pertenezca al conjunto de opciones válidas.
    """
    while True:
        respuesta = input(f"{pregunta}: ").strip().lower()
        if respuesta in opciones_validas:
            return respuesta
        print(f"Error: Opción no válida. Opciones: {' / '.join(opciones_validas)}")

def mostrar_recomendacion(cafe):
    """Muestra el resultado final del proceso algorítmico."""
    print(f"\n[!] Tu café ideal es: {cafe.upper()}\n")

# ─────────────────────────────────────────────
#  LÓGICA DE RAMAS (Descomposición de Problemas)
# ─────────────────────────────────────────────

def preguntar_gusto_agregado():
    """Determina el café según el insumo adicional (leche, chocolate, crema)."""
    tipo = pedir_opcion("¿Cuál es tu gusto favorito? (leche/chocolate/crema)", opc_tipo_agregado)

    if tipo == "leche":
        mostrar_recomendacion("Café con Leche")
    elif tipo == "chocolate":
        mostrar_recomendacion("Bombón")
    elif tipo == "crema":
        mostrar_recomendacion("Vienés")

def preguntar_agregado():
    """Bifurca el flujo según si el usuario desea un agregado o un café simple."""
    respuesta = pedir_opcion("¿Querés agregado? (si/no)", opc_agregado)
    if respuesta == "si":
        preguntar_gusto_agregado()
    else:
        mostrar_recomendacion("Café solo")

def preguntar_tipo_alcohol():
    """Determina la bebida según el destilado de preferencia."""
    tipo = pedir_opcion("¿Qué tipo de alcohol preferís? (whisky/ron)", opc_tipo_alcohol)
    if tipo == "whisky":
        mostrar_recomendacion("Café Irlandés")
    else:
        mostrar_recomendacion("Carajillo")

def rama_caliente():
    """Punto de entrada para el hilo de bebidas calientes."""
    alcohol = pedir_opcion("¿Querés que tu café incluya alcohol? (si/no)", opc_alcohol)
    if alcohol == "si":
        preguntar_tipo_alcohol()
    else:
        preguntar_agregado()

def rama_fria():
    """Punto de entrada para el hilo de bebidas frías o tipo postres."""
    base = pedir_opcion("¿Cómo preferís la base? (helado/instantaneo)", opc_base)
    if base == "helado":
        mostrar_recomendacion("Azteca")
    else:
        mostrar_recomendacion("Frappé")

# ─────────────────────────────────────────────
#  MENÚ PRINCIPAL
# ─────────────────────────────────────────────

def main():
    """
    Flujo principal: Controla el ciclo de vida del sistema, 
    iniciando por la selección de temperatura.
    """
    print("╔══════════════════════════════════════════╗")
    print("║  Bienvenidos al Recomendador SMARTROAST  ║")
    print("╚══════════════════════════════════════════╝")
    
    activo = True
    while activo:
        input("\nPresione Enter para solicitar una recomendación personalizada...")
        
        temp = pedir_opcion("¿Buscás una bebida caliente o fría?", opc_temperatura)
        
        if temp == "caliente":
            rama_caliente()
        else:
            rama_fria()
            
        continuar = input("¿Desea realizar otra recomendación? (Si/No): ").lower()
        if continuar != 'si':
            activo = False
            print("Gracias por utilizar el Recomendador de SmartRoast.")

if __name__ == "__main__":
    main()