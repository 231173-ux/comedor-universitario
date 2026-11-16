# pagos.py
# Sistema de Comedor Universitario - UNAMBA
# RF06: Calcular tarifa y registrar pago
# RF07: Generar ticket con codigo QR

from datetime import datetime
from uuid import uuid4
import qrcode

from config import PRECIO_RACION


# Registro temporal de pagos
pagos = []


def calcular_tarifa(tipo_usuario):
    """
    Calcula la tarifa segun el tipo de beneficiario.
    """

    if tipo_usuario == "becario":
        return 0.00

    elif tipo_usuario == "no_becario":
        return PRECIO_RACION

    else:
        raise ValueError("Tipo de usuario no valido")


def registrar_pago(codigo_estudiante, tipo_usuario):
    """
    Registra un pago simulado y genera un ticket QR.
    """

    monto = calcular_tarifa(tipo_usuario)

    codigo_ticket = uuid4().hex[:12].upper()

    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    registro = {
        "codigo_estudiante": codigo_estudiante,
        "tipo_usuario": tipo_usuario,
        "monto": monto,
        "codigo_ticket": codigo_ticket,
        "fecha": fecha,
        "estado": "EXONERADO" if monto == 0 else "PAGO_SIMULADO"
    }

    pagos.append(registro)

    # Informacion del ticket
    contenido_qr = (
        f"COMEDOR UNIVERSITARIO UNAMBA\n"
        f"Ticket: {codigo_ticket}\n"
        f"Estudiante: {codigo_estudiante}\n"
        f"Fecha: {fecha}\n"
        f"Monto: S/ {monto:.2f}"
    )

    # Generar codigo QR
    imagen = qrcode.make(contenido_qr)

    nombre_archivo = f"ticket_{codigo_ticket}.png"

    imagen.save(nombre_archivo)

    print("\nPago registrado correctamente.")
    print(f"Estudiante: {codigo_estudiante}")
    print(f"Tipo: {tipo_usuario}")
    print(f"Monto: S/ {monto:.2f}")
    print(f"Ticket: {codigo_ticket}")
    print(f"Archivo QR: {nombre_archivo}")

    return registro


def mostrar_pagos():
    """Muestra los pagos registrados."""

    print("\n===== REPORTE DE PAGOS =====")

    for pago in pagos:
        print(
            f"Estudiante: {pago['codigo_estudiante']} | "
            f"Monto: S/ {pago['monto']:.2f} | "
            f"Estado: {pago['estado']}"
        )


if __name__ == "__main__":

    print("=" * 45)
    print("COMEDOR UNIVERSITARIO - UNAMBA")
    print("MODULO DE PAGOS Y TICKETS QR")
    print("=" * 45)

    registrar_pago("20260001", "becario")
    registrar_pago("20260002", "no_becario")

    mostrar_pagos()