import pytest
import archivos

def test_cargar_matriz_desde_archivo():
    ruta = "../tests/matriztest.txt"
    result = archivos.cargar_matriz_desde_archivo(ruta)
    assert result == [[-3.0, -2.0, -5.0, 0.0, 0.0, 0.0, 0.0],
                      [1.0, 2.0, 1.0, 1.0, 0.0, 0.0, 430.0],
                      [3.0, 0.0, 2.0, 0.0, 1.0, 0.0, 460.0],
                      [1.0, 4.0, 0.0, 0.0, 0.0, 1.0, 420.0]]

def test_listar_archivos_txt():
    ruta = "../tests/listadotest"
    result = archivos.listar_archivos_txt(ruta)
    assert result == ['test1.txt', 'test2.txt']
    
test_cargar_matriz_desde_archivo()