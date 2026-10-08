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

# Ejercicio 3: Máximo con control de errores
# Casos con enteros y floats.
# Uso de pytest.raises para listas vacías.
@pytest.mark.parametrize(
    "nums, resultado_esperado",
    [
        ([1, 2, 3, 4, 5], 5),
        ([-1, -2, -3], -1),
        ([1.5, 2.71, 0.1, 2.70], 2.71),
        ([-3, 4.5, 0, -1.2], 4.5),
        ([-10, -20, -30], -10)
    ],
    ids=["enteros_positivos", 
         "enteros_negativos", 
         "numeros_float", 
         "mixto_enteros_y_floats",
         "elementos_negativos" 
    ],
)
def test_maximo_seguro(nums, resultado_esperado):
    """Verifica la función maximo_seguro con diferentes listas de números."""
    assert maximo_seguro(nums) == resultado_esperado

def test_maximo_seguro_lista_vacia():
    """ Verifica que maximo_seguro lance ValueError al recibir una lista vacía."""
    with pytest.raises(ValueError, match="lista vacía"):
        maximo_seguro([])

# Ejercicio 4: Contador Simple de palabras
# Texto vacío.
# Palabras repetidas.
# Comprobar que "Hola hola" devuelve {'hola': 2}.
def test_contar_palabras_texto_vacio():
    """Verifica que contar_palabras devuelva un diccionario vacío para un texto vacío."""
    assert contar_palabras("") == {}

def test_contar_palabras_insensible_a_mayusculas():
    """Verifica que contar_palabras trate las palabras de manera insensible a mayúsculas y minúsculas."""
    resultado = contar_palabras("Hola hola")
    assert resultado == {"hola": 2}

def test_contar_palabras_frase_compleja():
    """Verifica que contar_palabras cuente correctamente las palabras en una frase compleja."""
    texto = "Python es genial y probar código en Python es divertido"
    esperado = {
        "python": 2,
        "es": 2,
        "genial": 1,
        "y": 1,
        "probar":1,
        "código": 1,
        "en": 1,
        "divertido": 1,
    }
    assert contar_palabras(texto) == esperado