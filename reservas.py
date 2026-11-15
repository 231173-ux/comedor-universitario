# reservas.py
# Sistema de Comedor Universitario - UNAMBA
# RF04: Reservar una ración en un turno y horario
# RF05: Controlar el aforo máximo por turno

from config import AFORO_MAXIMO, HORARIO_ALMUERZO

# Lista temporal para almacenar reservas
reservas = []


def registrar_reserva(codigo_estudiante, turno="almuerzo"):
    """
    Registra una reserva si existe disponibilidad.
    """

    # Verificar reservas existentes del turno
    total_reservas = sum(
        1 for reserva in reservas
        if reserva["turno"] == turno
    )

    # Validar aforo máximo
    if total_reservas >= AFORO_MAXIMO:
        return "ERROR: Aforo máximo alcanzado."

    # Verificar reserva duplicada
    for reserva in reservas:
        if (
            reserva["codigo"] == codigo_estudiante
            and reserva["turno"] == turno
        ):
            return "ERROR: El estudiante ya tiene una reserva."

    # Registrar reserva
    nueva_reserva = {
        "codigo": codigo_estudiante,
        "turno": turno,
        "horario": HORARIO_ALMUERZO,
        "estado": "CONFIRMADA"
    }

    reservas.append(nueva_reserva)

    return "Reserva registrada correctamente."


def mostrar_reservas():
    """Muestra las reservas registradas."""

    print("\n===== RESERVAS DEL COMEDOR =====")

    for reserva in reservas:
        print(f"Estudiante: {reserva['codigo']}")
        print(f"Turno: {reserva['turno']}")
        print(f"Horario: {reserva['horario']}")
        print(f"Estado: {reserva['estado']}")
        print("-" * 35)

    print(f"Total de reservas: {len(reservas)}")
    print(f"Aforo máximo: {AFORO_MAXIMO}")
    print(f"Cupos disponibles: {AFORO_MAXIMO - len(reservas)}")


if __name__ == "__main__":

    print("COMEDOR UNIVERSITARIO - UNAMBA")
    print("Módulo de Reservas")

    print(registrar_reserva("20260001"))
    print(registrar_reserva("20260002"))
    print(registrar_reserva("20260003"))

    mostrar_reservas()