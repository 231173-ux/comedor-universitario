# reportes.py
# Sistema de Comedor Universitario - UNAMBA
# RF11: Generar reportes diarios
# Responsable: master
# Version: v5.0

from datetime import date

from config import NOMBRE_COMEDOR


def generar_reporte_diario(
    reservas,
    pagos,
    asistentes,
    raciones_preparadas
):
    """
    Genera un reporte diario del comedor.

    Parametros:
    - reservas: lista de reservas registradas.
    - pagos: lista de pagos registrados.
    - asistentes: lista de estudiantes atendidos.
    - raciones_preparadas: cantidad preparada.
    """

    total_reservas = len(reservas)

    total_asistencias = len(asistentes)

    # En este ejemplo, cada asistente recibe una racion.
    raciones_servidas = total_asistencias

    # Calcular ingresos por pagos simulados.
    ingresos = sum(
        pago["monto"]
        for pago in pagos
        if pago["estado"] == "PAGO_SIMULADO"
    )

    # Validar los datos del reporte.
    if raciones_preparadas < raciones_servidas:
        raise ValueError(
            "Las raciones servidas superan las preparadas."
        )

    # Calcular raciones no servidas.
    # Se utilizan como indicador simplificado de merma.
    merma = raciones_preparadas - raciones_servidas

    reporte = {
        "fecha": date.today().isoformat(),
        "total_reservas": total_reservas,
        "raciones_servidas": raciones_servidas,
        "ingresos": ingresos,
        "asistencias": total_asistencias,
        "merma": merma
    }

    return reporte


def mostrar_reporte(reporte):
    """
    Muestra el reporte diario en consola.
    """

    print("=" * 50)
    print(NOMBRE_COMEDOR)
    print("REPORTE DIARIO - RF11")
    print("=" * 50)

    print(f"Fecha: {reporte['fecha']}")

    print("-" * 50)

    print(
        f"Reservas registradas: "
        f"{reporte['total_reservas']}"
    )

    print(
        f"Raciones servidas: "
        f"{reporte['raciones_servidas']}"
    )

    print(
        f"Ingresos del dia: "
        f"S/ {reporte['ingresos']:.2f}"
    )

    print(
        f"Asistencia de estudiantes: "
        f"{reporte['asistencias']}"
    )

    print(
        f"Raciones no servidas (merma estimada): "
        f"{reporte['merma']}"
    )

    print("=" * 50)
    print("Reporte generado correctamente.")


if __name__ == "__main__":

    # Datos de prueba: reservas registradas
    reservas = [
        {"codigo": "20260001"},
        {"codigo": "20260002"},
        {"codigo": "20260003"}
    ]

    # Datos de prueba: pagos realizados
    pagos = [
        {
            "codigo": "20260001",
            "monto": 0.00,
            "estado": "EXONERADO"
        },
        {
            "codigo": "20260002",
            "monto": 4.00,
            "estado": "PAGO_SIMULADO"
        }
    ]

    # Estudiantes que recibieron su racion
    asistentes = [
        "20260001",
        "20260002"
    ]

    # Total de raciones preparadas
    raciones_preparadas = 3

    reporte = generar_reporte_diario(
        reservas,
        pagos,
        asistentes,
        raciones_preparadas
    )

    mostrar_reporte(reporte)