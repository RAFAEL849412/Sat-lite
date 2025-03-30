# mymodule.py - Configuração de satélite

# Constantes
B1950 = 2433282.4235  # Época B1950 em dias Julianos
T0 = 2451545.0        # Época J2000 em dias Julianos
pi = 3.141592653589793

def calcular_periodo_orbital(semieixo_maior, massa_central=5.972e24):
    """
    Calcula o período orbital usando a terceira lei de Kepler.
    semieixo_maior: raio médio da órbita em metros
    massa_central: massa do corpo central em kg (padrão: Terra)
    """
    G = 6.67430e-11  # Constante gravitacional em m^3 kg^-1 s^-2
    return 2 * pi * ((semieixo_maior ** 3 / (G * massa_central)) ** 0.5)

# Exemplo de configuração
if __name__ == "__main__":
    semieixo = 7.0e6  # Exemplo de semieixo maior em metros (cerca de 7000 km)
    periodo = calcular_periodo_orbital(semieixo)
    print(f"Período orbital: {periodo:.2f} segundos")

