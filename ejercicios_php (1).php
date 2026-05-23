<?php
// ============================================================
// PARTE 1 - Variables y operaciones básicas
// ============================================================


echo "  PARTE 1: Variables y operaciones básicas\n";


// Ejercicio 1: Calcular el perímetro de un rectángulo
$largo = 12;
$ancho = 7;
$perimetro = 2 * ($largo + $ancho);
echo "1. Perímetro del rectángulo (largo=$largo, ancho=$ancho): $perimetro\n";

// Ejercicio 2: Calcular el promedio de 4 números
$n1 = 15; $n2 = 33; $n3 = 47; $n4 = 25;
$promedio = ($n1 + $n2 + $n3 + $n4) / 4;
echo "2. Promedio de $n1, $n2, $n3, $n4: $promedio\n";

// Ejercicio 3: Convertir kilómetros a metros
$kilometros = 7.8;
$metros = $kilometros * 1000;
echo "3. $kilometros km = $metros metros\n";

// Ejercicio 4: Calcular el IVA (19%) de un producto
$precio = 85000;
$iva = $precio * 0.19;
$total = $precio + $iva;
echo "4. Producto: \$$precio | IVA (19%): \$$iva | Total: \$$total\n";

// Ejercicio 5: Elevar un número a la cuarta potencia
$base = 5;
$resultado = pow($base, 4);
echo "5. $base elevado a la cuarta potencia: $resultado\n";



// PARTE 2 - Condicionales (if, else, elseif)


echo "\n========================================\n";
echo "  PARTE 2: Condicionales (if, else, elseif)\n";
echo "========================================\n\n";

// Ejercicio 6: Verificar si un número es múltiplo de 2
$num = 37;
if ($num % 2 == 0) {
    echo "6. $num ES múltiplo de 2\n";
} else {
    echo "6. $num NO es múltiplo de 2\n";
}

// Ejercicio 7: Determinar si un número es mayor a 100
$num = 143;
if ($num > 100) {
    echo "7. $num es mayor a 100\n";
} else {
    echo "7. $num NO es mayor a 100\n";
}

// Ejercicio 8: Validar si una persona puede votar (>=18)
$edad = 21;
if ($edad >= 18) {
    echo "8. Con $edad años, la persona SÍ puede votar\n";
} else {
    echo "8. Con $edad años, la persona NO puede votar\n";
}

// Ejercicio 9: Comparar tres números y mostrar el menor
$a = 92; $b = 57; $c = 34;
if ($a <= $b && $a <= $c) {
    $menor = $a;
} elseif ($b <= $a && $b <= $c) {
    $menor = $b;
} else {
    $menor = $c;
}
echo "9. De los números $a, $b y $c, el menor es: $menor\n";

// Ejercicio 10: Verificar si un número es divisible entre 4
$num = 54;
if ($num % 4 == 0) {
    echo "10. $num ES divisible entre 4\n";
} else {
    echo "10. $num NO es divisible entre 4\n";
}


// PARTE 4 - Bucles FOR


echo "\n========================================\n";
echo "  PARTE 4: Bucles FOR\n";
echo "========================================\n\n";

// Ejercicio 16: Mostrar números del 5 al 50 de 5 en 5
echo "16. Números del 5 al 50 de 5 en 5:\n    ";
for ($i = 5; $i <= 50; $i += 5) {
    echo "$i ";
}
echo "\n";

// Ejercicio 17: Generar tabla de multiplicar del 7
$tabla = 7;
echo "17. Tabla de multiplicar del $tabla:\n";
for ($i = 1; $i <= 10; $i++) {
    $producto = $tabla * $i;
    echo "    $tabla x $i = $producto\n";
}

// Ejercicio 18: Sumar los números pares del 1 al 50
$sumaPares = 0;
for ($i = 2; $i <= 50; $i += 2) {
    $sumaPares += $i;
}
echo "18. Suma de números pares del 1 al 50: $sumaPares\n";

// Ejercicio 19: Mostrar los cuadrados de los números del 1 al 10
echo "19. Cuadrados del 1 al 10:\n    ";
for ($i = 1; $i <= 10; $i++) {
    $cuadrado = $i * $i;
    echo "{$i}^2=$cuadrado  ";
}
echo "\n";

// Ejercicio 20: Contar cuántos números son múltiplos de 3 entre 1 y 100
$contadorMult3 = 0;
for ($i = 1; $i <= 100; $i++) {
    if ($i % 3 == 0) {
        $contadorMult3++;
    }
}
echo "20. Cantidad de múltiplos de 3 entre 1 y 100: $contadorMult3\n";


// ============================================================
// PARTE 5 - Bucles WHILE
// ============================================================

echo "\n========================================\n";
echo "  PARTE 5: Bucles WHILE\n";
echo "========================================\n\n";

// Ejercicio 21: Mostrar números del 10 al 1
echo "21. Números del 10 al 1:\n    ";
$i = 10;
while ($i >= 1) {
    echo "$i ";
    $i--;
}
echo "\n";

// Ejercicio 22: Sumar números hasta llegar a 50
$suma = 0;
$num = 1;
echo "22. Sumar números hasta llegar a 50:\n";
while ($suma < 50) {
    $suma += $num;
    echo "    Sumando $num → acumulado = $suma\n";
    $num++;
}
echo "    Se llegó a $suma sumando hasta el número " . ($num - 1) . "\n";

// Ejercicio 23: Pedir números hasta ingresar uno negativo
$numerosSimulados = [9, 14, 6, 25, 3, -5];
$index = 0;
echo "23. Números ingresados hasta el negativo (simulado):\n";
while (true) {
    $n = $numerosSimulados[$index];
    if ($n < 0) {
        echo "    Se ingresó $n (negativo) → se detiene el ciclo\n";
        break;
    }
    echo "    Número ingresado: $n\n";
    $index++;
}

// Ejercicio 24: Contar números ingresados por el usuario
$numerosSimulados2 = [11, 3, 8, 22, 17, 5, -2];
$contador = 0;
$idx = 0;
while ($numerosSimulados2[$idx] >= 0) {
    $contador++;
    $idx++;
}
echo "24. Cantidad de números ingresados antes del negativo: $contador\n";

// Ejercicio 25: Mostrar números múltiplos de 4 hasta 100
echo "25. Múltiplos de 4 hasta 100:\n    ";
$i = 4;
while ($i <= 100) {
    echo "$i ";
    $i += 4;
}
echo "\n";
