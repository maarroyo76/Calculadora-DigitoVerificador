# 👨‍💻 Calculadora de Dígito Verificador (RUN)

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python&logoColor=white)

Una aplicación sencilla en Python para calcular el dígito verificador de un RUN chileno a partir de sus primeros 8 dígitos.

## ✨ Características
- 🔢 Menú interactivo en la consola.
- ✅ Validación de formato del RUN (8 dígitos numéricos).
- 📊 Cálculo del dígito verificador utilizando la suma ponderada.
- ⚠️ Manejo de errores para entradas inválidas.

## 💡 Requisitos
- Python 3.7 o superior.

## 🔄 Uso
1. Ejecuta el archivo principal:

```bash
python main.py
```

2. Sigue las instrucciones en el menú:
   - ① Ingresar un RUN de 8 dígitos para calcular su dígito verificador.
   - ② Salir del programa.

## 🗂️ Estructura del Proyecto
- `main.py`: Archivo principal que muestra el menú y gestiona el flujo de la aplicación.
- `calculo_dv.py`: Contiene las funciones para validar el RUN y calcular el dígito verificador.

## 💡 Ejemplo de Uso

```bash
========================================
CALCULADORA DE DÍGITO VERIFICADOR (RUN)
========================================
1. Calcular dígito verificador
2. Salir
========================================
Seleccione una opción (1-2): 1
Ingrese los primeros 8 dígitos del RUN: 12345678

✅ Resultado: El dígito verificador de 12345678 es: 5
```

## 📚 Licencia
Este proyecto es de uso libre para fines educativos.

