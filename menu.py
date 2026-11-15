# menu.py
# Sistema de Comedor Universitario - UNAMBA
# Requerimiento RF03: Publicar el menú diario y semanal

from datetime import date
from config import PRECIO_RACION, HORARIO_ALMUERZO


def obtener_menu_dia():
    """Devuelve el menú del día."""

    menu = {
        "fecha": date.today().isoformat(),
        "entrada": "Sopa de verduras",
        "segundo": "Pollo con arroz",
        "bebida": "Refresco de cebada",
        "precio": PRECIO_RACION,
        "horario": HORARIO_ALMUERZO
    }

    return menu


def mostrar_menu():
    """Muestra el menú del comedor universitario."""

    menu = obtener_menu_dia()

    print("=" * 45)
    print("COMEDOR UNIVERSITARIO - UNAMBA")
    print("=" * 45)

    print(f"Fecha: {menu['fecha']}")
    print(f"Entrada: {menu['entrada']}")
    print(f"Segundo: {menu['segundo']}")
    print(f"Bebida: {menu['bebida']}")
    print(f"Precio: S/ {menu['precio']:.2f}")
    print(f"Horario: {menu['horario']}")

    print("=" * 45)


if __name__ == "__main__":
    mostrar_menu()