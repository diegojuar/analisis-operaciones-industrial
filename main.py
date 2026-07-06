def calcular_oee(disponibilidad, rendimiento, calidad):
    """
    Calcula la Eficiencia General de los Equipos (OEE).
    Los valores deben ingresarse en porcentaje (ej. 90 para 90%).
    """
    oee = (disponibilidad / 100) * (rendimiento / 100) * (calidad / 100) * 100
    return round(oee, 2)

def main():
    print("==================================================")
    print("📊 SISTEMA DE ANÁLISIS DE PRODUCTIVIDAD INDUSRIAL 📊")
    print("==================================================")
    
    # Datos simulados de una línea de producción
    disp = 85.0  # % de tiempo que la máquina estuvo corriendo
    rend = 90.0  # % de la velocidad máxima de la máquina
    cal = 98.0   # % de productos que salieron sin defectos
    
    resultado = calcular_oee(disp, rend, cal)
    
    print(f"-> Disponibilidad: {disp}%")
    print(f"-> Rendimiento:    {rend}%")
    print(f"-> Calidad:        {cal}%")
    print("--------------------------------------------------")
    print(f"🏆 El OEE estimado de la línea es: {resultado}%")
    print("==================================================")

if __name__ == "__main__":
    main()
