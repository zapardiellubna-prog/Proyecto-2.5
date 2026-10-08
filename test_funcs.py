import pytest

# Ejercicio 1: Sumatoria de no negativos
# Asserts con listas vacías, solo negativos, mixtas y solo positivos.
# Parametrizar al menos 5 casos con @pytest.mark.parametrize.
@pytest.mark.parametrize("nums,resultado_esperado", [
    ([1, 2, 3, 4, 5], 15),
    ([0, 1, 2, 3], 6),
    ([-1, -2, -3], 0),
    ([], 0),
    ([-2, 5, -1, 0, 3], 8)
],
ids= ["Todos positivos", "Incluye cero", "Todos negativos", "Lista vacía", "Lista mixta"])
def test_sumatoria_positivos(nums, resultado_esperado):
    assert sumatoria_positivos(nums) == resultado_esperado

# Ejercicio 2: Palíndromo básico
# Parametrizar al menos 8 casos con ids descriptivos.
# Incluir casos positivos y negativos.
@pytest.mark.parametrize("cadena,resultado_esperado", [
    ("reconocer", True),
    ("Anita lava la tina", True),
    ("hola", False),
    ("A ma ma", True),
    ("", True),
    ("a", True),
    ("Hola mundo", False),
    ("12321", True),
],
ids= ["palabra_simple_positiva",
        "frase_con_mayusculas_y_espacios",
        "palabra_simple_negativa",
        "frase_corta_positiva",
        "cadena_vacia",
        "caracter_unico",
        "frase_comun_negativa",
        "secuencia_numerica_palindroma"])
def test_es_palindromo(cadena, resultado_esperado):
    """Verifica la detección de palíndromos en cadenas válidas y no válidas."""
    assert es_palindromo(cadena) == resultado_esperado