from validadorclave.modelo.validador import (
    ReglaValidacionGanimedes,
    ReglaValidacionCalisto,
    Validador
)


def validar_clave(clave: str, reglas_validacion: list):
    for regla_cls in reglas_validacion:
        validador = Validador(regla_cls())
        try:
            if validador.es_valida(clave):
                print(f"La clave es válida para {regla_cls.__name__}")
        except ValueError as e:
            print(f"Error: {regla_cls.__name__}: {str(e)}")


# Ejemplo de uso
if __name__ == "__main__":
    reglas = [ReglaValidacionGanimedes, ReglaValidacionCalisto]

    # Prueba con una clave inválida
    print("Validando clave inválida:")
    validar_clave("abc123", reglas)

    # Prueba con una clave válida para Ganimedes pero no para Calisto
    print("\nValidando clave válida para Ganimedes pero no para Calisto:")
    validar_clave("Abc123@xyz", reglas)

    # Prueba con una clave válida para Calisto pero no para Ganimedes
    print("\nValidando clave válida para Calisto pero no para Ganimedes:")
    validar_clave("cAliStO123", reglas)

    # Prueba con una clave válida para ambas
    print("\nValidando clave válida para ambas reglas:")
    validar_clave("cAliStO123@", reglas)