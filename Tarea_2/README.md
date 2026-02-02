# Ejemplo de Manejo de Excepciones y Monitoreo de Errores

## Descripción
Aplicación Python que demuestra el uso de manejo de excepciones, logging y monitoreo de errores con Sentry.

## Características
- División de números enteros con validación de entrada
- Captura de excepciones específicas (`ZeroDivisionError`, `ValueError`)
- Registro de errores en archivo local (`errores.log`)
- Integración con Sentry para monitoreo remoto
- Interfaz interactiva con opción de continuar o salir

## Requisitos
```bash
pip install sentry-sdk
```

## Uso
```bash
python Ejemplo.py
```

El programa solicita:
1. Numerador (número entero)
2. Denominador (número entero)
3. Muestra el resultado de la división
4. Pregunta si deseas continuar

## Configuración
- En caso de querer utilziar con Sentry:
Actualiza el DSN de Sentry en el código con tus credenciales reales:
```python
sentry_sdk.init(dsn="tu_dsn_aqui")
```

## Archivos Generados
- `errores.log` - Registro local de errores

## Errores Manejados
- **ZeroDivisionError**: No se puede dividir por cero
- **ValueError**: Entrada inválida (no es número entero)

## Conclusiones

A través de esta práctica, pudimos apreciar un ejemplo sencillo, pero efectivo, de cómo implementar mecanismos de tolerancia a fallas en Python. El uso combinado de manejo de excepciones, registro local de errores (logging) y monitoreo externo con Sentry nos permite detectar, reportar y recuperar fallos de manera rápida y eficaz, manteniendo el programa operativo y facilitando la depuración posterior.