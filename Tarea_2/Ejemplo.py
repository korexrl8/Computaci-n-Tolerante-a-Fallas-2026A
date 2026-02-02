import sentry_sdk
import logging

logging.basicConfig(
    filename="errores.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# DSN de ejemplo
sentry_sdk.init(
    dsn="https://examplePublicKey@o0.ingest.sentry.io/0",
    traces_sample_rate=1.0
)

def dividir(a, b):
    return a / b

def main():

    while True:
        try:
            x = int(input("Ingresa el numerador: "))
            y = int(input("Ingresa el denominador: "))
            resultado = int(dividir(x, y))
            print("Resultado: ", resultado)

        except Exception as e:
            if isinstance(e, ZeroDivisionError):
                print("Error: No se puede dividir por cero.")
                logging.error("Error detectado", exc_info=e)

            elif isinstance(e, ValueError):
                print("Error: Entrada inválida. Por favor ingresa números enteros.")
                logging.error("Error detectado", exc_info=e)

            # Registro con Sentry
            sentry_sdk.capture_exception(e)

        finally:
            while True:
                salir = input("¿Deseas continuar? (s/n): ").lower()
                if salir in ("s", "n"):
                    break
                else:
                    print("Entrada no válida. Escribe solo 's' o 'n'.")
            if salir == "n":
                break

print("Programa finalizado correctamente.")

if __name__ == "__main__":
    main()