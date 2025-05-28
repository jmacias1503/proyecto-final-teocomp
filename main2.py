import sys
import graphviz
import time
import os

class MaquinaTuring:
    def __init__(this, archivo_sextupla):
        this.estados = []
        this.alfabeto_entrada = []
        this.alfabeto_cinta = []
        this.estado_inicial = None
        this.estados_aceptacion = set()
        this.transiciones = {}  # Formato : (estado_actual simbolo_leido simbolo_escribir direccion_cabezal)
        this.blanco = 'B'
        this.nombre_archivo = archivo_sextupla
        this._sextupla(archivo_sextupla)

    def _sextupla(this, archivo_sextupla):
        with open(archivo_sextupla, 'r') as archivo:
            this.alfabeto_entrada = archivo.readline().strip().split()
            this.alfabeto_cinta = archivo.readline().strip().split()
            this.estados = archivo.readline().strip().split()
            this.estado_inicial = archivo.readline().strip()
            linea_aceptacion = archivo.readline().strip()
            this.estados_aceptacion = set(linea_aceptacion.split())
            for linea in archivo:
                partes = linea.strip().split()
                if not partes:
                    continue
                actual, simbolo_leido, simbolo_escribir, direccion, siguiente = partes
                this.transiciones[(actual, simbolo_leido)] = (simbolo_escribir, direccion, siguiente)

    #def dibujar_grafo(this):
    #    dot = graphviz.Digraph(comment='Maquina de Turing')
    #    dot.attr(rankdir='LR')
    #    
    #    # Add states
    #    for estado in this.estados:
    #        if estado in this.estados_aceptacion:
    #            dot.node(estado, shape='doublecircle')
    #        else:
    #            dot.node(estado)
    #    
    #    # Add transitions
    #    for (actual, simbolo), (escribir, direccion, siguiente) in this.transiciones.items():
    #        label = f"{simbolo}/{escribir},{direccion}"
    #        dot.edge(actual, siguiente, label=label)
    #    
    #    dot.node('start', shape='point')
    #    dot.edge('start', this.estado_inicial)
    #    
    #    dot.render(f'grafo_{this.nombre_archivo}', format='png', cleanup=True)
    #    print(f"Grafo generado como 'grafo_{this.nombre_archivo}.png'")

    def mostrar_cinta(this, cinta, cabeza, estado):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Estado actual: {estado}")
        print("Cinta:")
        for i, simbolo in enumerate(cinta):
            if i == cabeza:
                print(f"[{simbolo}]", end=' ')
            else:
                print(simbolo, end=' ')
        print("\n" + "-"*50)

    def simular(this, cadena_entrada, pasos_maximos=10000):
        cinta = list(cadena_entrada)
        cinta = cinta + [this.blanco]
        cabeza = 0
        estado_actual = this.estado_inicial
        pasos = 0

        this.mostrar_cinta(cinta, cabeza, estado_actual)
        time.sleep(0.5)

        while pasos < pasos_maximos:
            pasos += 1
            cinta_anterior = cinta.copy()
            simbolo = cinta[cabeza]
            clave = (estado_actual, simbolo)
            if clave not in this.transiciones:
                break  
            simbolo_escribir, direccion, siguiente_estado = this.transiciones[clave]
            cinta[cabeza] = simbolo_escribir
            if direccion == 'R':
                cabeza += 1
            elif direccion == 'L':
                cabeza -= 1
            estado_actual = siguiente_estado

            this.mostrar_cinta(cinta, cabeza, estado_actual)
            print(f"Transicion: {clave} -> {this.transiciones[clave]}")
            time.sleep(0.5)

            if estado_actual in this.estados_aceptacion:
                return True, ''.join(cinta).strip(this.blanco)
        return False, ''.join(cinta).strip(this.blanco)

if __name__ == '__main__':
    print("Selecciona el caso que quieres validar:")
    print("1. MT palindromos")
    print("2. MT expresion aritmetica postfijo")
    print("3. MT expresion aritmetica prefijo")
    print("4. MT expresion aritmetica infijo")
    opcion = input("Ingresa el numero de opcion: ").strip()

    archivo_nombre = ""
    if opcion == "1":
        archivo_nombre = "MT1.txt"
    elif opcion == "2":
        archivo_nombre = "MT2.txt"
    elif opcion == "3":
        archivo_nombre = "MT3.txt"
    elif opcion == "4":
        archivo_nombre = "MT4.txt"
    else:
        print("Opcion no valida.")
        exit()

    mt = MaquinaTuring(archivo_nombre)
    print("\nGenerando grafo de la maquina...")
    #mt.dibujar_grafo()
    
    palabra = input('Ingresa la palabra o expresion a validar: ').strip()
    aceptada, cinta_final = mt.simular(palabra)
    if aceptada:
        print(f"La entrada '{palabra}' es ACEPTADA.\nCinta final: {cinta_final}")
    else:
        print(f"La entrada '{palabra}' NO es aceptada.\nCinta final: {cinta_final}")
