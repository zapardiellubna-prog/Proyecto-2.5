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

# Ejercicio 5: Filtrado de aprobados
# Parametrizar 4 casos distintos.
# Verificar que se mantiene el orden original.
@pytest.mark.parametrize("pares, esperado", 
    [
        ([("Alice", 6.0), ("Bob", 4.0), ("Charlie", 7.0)], ["Alice", "Charlie"]),
        ([("David", 5.0), ("Eve", 5.0)], ["David", "Eve"]),
        ([("Frank", 4.0), ("Grace", 3.0)], []),
        ([], []),
    ],
    ids= ["lista_mixta", "todos_aprobados", "ninguno_aprobado", "lista_vacia"]
)
def test_filtrar_aprobados(pares, esperado):
    assert filtrar_aprobados(pares) == esperado

def test_filtrar_aprobados_orden():
    """Verifica que filtrar_aprobados mantenga el orden original"""
    pares = [("Alice", 6.0), ("Bob", 4.0), ("Charlie", 7.0), ("David", 5.0)]
    esperado = ["Alice", "Charlie", "David"]
    assert filtrar_aprobados(pares) == esperado

# Testing Ejercicio 6: Normalizar Email
# Casos válidos e inválidos.
# Comprobar normalización a minúsculas.
@pytest.mark.parametrize(
    "email, resultado_esperado",
    [
        ("alice@ejemplo.com", ("alice", "ejemplo.com")),
        ("BOB@EJEMPLO.COM", ("bob", "ejemplo.com")),
        ("charlie@subdominio.EJEMPLO.COM", ("charlie", "subdominio.ejemplo.com")),
        ("Alice@ejemplo.com", ("alice", "ejemplo.com"))
    ],
    ids=["email_normal", "email_con_mayusculas", "email_con_dominio_subdominio", "capitalizacion_mixta"]
)
def test_normalizar_email(email, resultado_esperado):
    """Comprueba la normalización a minúsculas en correos electrónicos válidos."""
    assert normalizar_email(email) == resultado_esperado
@pytest.mark.parametrize(
    "email_invalido",
    [
        "sin_arroba.com",
        "usuario@@dominio.com",
        "usuario@dominio@otro.com",
        "",
    ],
    ids=[
        "falta_arroba",
        "arroba_doble_consecutiva",
        "multiples_arrobas_separadas",
        "cadena_vacia",
    ],
)
def test_normalizar_email_invalido(email_invalido):
    """Valida la generación de ValueError cuando la estructura del email no es adecuada."""
    with pytest.raises(ValueError, match="email inválido"):
        normalizar_email(email_invalido)

# Testing Ejercicio 7: Factorial iterativo con control de errores
# Casos (0,1), (1,1), (5,120).
# Comprobar excepción para valores negativos.
@pytest.mark.parametrize(
    "num, resultado_esperado",
    [
        (0,1),
        (1,1),
        (5,120)
    ],
    ids=[
        "factorial_0",
        "factorial_1",
        "factorial_5"
    ],
)
def test_factorial_valido(num, resultado_esperado):
    """ Verifica el cálculo correcto del factorial para valores válidos."""
    assert factorial(num) == resultado_esperado
def test_factorial_negativo():
    """ Verifica que la función factorial lance ValueError al recibir un número negativo. """
    with pytest.raises(ValueError, match="n negativo"):
        factorial(-1)