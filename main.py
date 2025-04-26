from calculo_dv import calcular_digito_verificador

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n" + "="*40)
    print("CALCULADORA DE DÍGITO VERIFICADOR (RUN)")
    print("="*40)
    print("1. Calcular dígito verificador")
    print("2. Salir")
    print("="*40)

def main():
    """Función principal con bucle y manejo de errores"""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-2): ")
        
        try:
            if opcion == "1":
                run = input("Ingrese los primeros 8 dígitos del RUN: ")
                dv = calcular_digito_verificador(run)
                
                if dv is None:
                    print("\n⚠️ Error: El RUN debe contener exactamente 8 dígitos numéricos")
                else:
                    print(f"\n✅ Resultado: El dígito verificador de {run} es: {dv}")
            
            elif opcion == "2":
                print("\n¡Hasta luego! 👋")
                break
            
            else:
                print("\n⚠️ Error: Opción no válida. Intente nuevamente.")
                
        except ValueError:
            print("\n⚠️ Error inesperado: Asegúrese de ingresar datos válidos")
        except Exception as e:
            print(f"\n⚠️ Error inesperado: {str(e)}")

if __name__ == "__main__":
    main()