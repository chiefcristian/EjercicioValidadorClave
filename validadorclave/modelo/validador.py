from abc import ABC, abstractmethod


class ReglaValidacion(ABC):
    def __init__(self, longitud_esperada: int):
        self._longitud_esperada = longitud_esperada

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass

    def _validar_longitud(self, clave: str) -> bool:
        return len(clave) > self._longitud_esperada

    def _contiene_mayuscula(self, clave: str) -> bool:
        return any(c.isupper() for c in clave)

    def _contiene_minuscula(self, clave: str) -> bool:
        return any(c.islower() for c in clave)

    def _contiene_numero(self, clave: str) -> bool:
        return any(c.isdigit() for c in clave)


class ReglaValidacionGanimedes(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=8)

    def contiene_caracter_especial(self, clave: str) -> bool:
        caracteres_especiales = {'@', '_', '#', '$', '%'}
        return any(c in caracteres_especiales for c in clave)

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise ValueError("La clave debe tener una longitud de más de 8 caracteres")

        if not self._contiene_mayuscula(clave):
            raise ValueError("La clave debe tener al menos una letra mayúscula")

        if not self._contiene_minuscula(clave):
            raise ValueError("La clave debe tener al menos una letra minúscula")

        if not self._contiene_numero(clave):
            raise ValueError("La clave debe tener al menos un número")

        if not self.contiene_caracter_especial(clave):
            raise ValueError("La clave debe tener al menos un caracter especial (@, _, #, $, %)")

        return True


class ReglaValidacionCalisto(ReglaValidacion):
    def __init__(self):
        super().__init__(longitud_esperada=6)

    def contiene_calisto(self, clave: str) -> bool:
        # Buscar la palabra 'calisto' en cualquier combinación de mayúsculas/minúsculas
        lower_clave = clave.lower()
        if 'calisto' not in lower_clave:
            return False

        # Encontrar todas las ocurrencias de 'calisto' (case insensitive)
        start_idx = 0
        while True:
            idx = lower_clave.find('calisto', start_idx)
            if idx == -1:
                break

            # Extraer la versión exacta de la palabra
            palabra = clave[idx:idx + 7]

            # Contar mayúsculas
            mayusculas = sum(1 for c in palabra if c.isupper())

            # Verificar condiciones: al menos 2 mayúsculas pero no todas (7)
            if 2 <= mayusculas < 7:
                return True

            start_idx = idx + 1

        return False

    def es_valida(self, clave: str) -> bool:
        if not self._validar_longitud(clave):
            raise ValueError("La clave debe tener una longitud de más de 6 caracteres")

        if not self._contiene_numero(clave):
            raise ValueError("La clave debe tener al menos un número")

        if not self.contiene_calisto(clave):
            raise ValueError("La palabra calisto debe estar escrita con al menos dos letras en mayúscula")

        return True