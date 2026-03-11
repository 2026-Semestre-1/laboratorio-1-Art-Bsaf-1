#NO MODIFICAR ESTE ARCHIVO

import Laboratorio01;
import pytest;

##################################################################
    
def test_lab_6():
    assert Laboratorio01.contadorDigitos(102039480, 0) == 3

def test_lab_7():
    assert Laboratorio01.contadorDigitos(132033483, 3) == 4

def test_lab_8():
    assert isinstance(Laboratorio01.contadorDigitos(132033483, 13), str) == isinstance("Error: El parámetro digito debe ser un valor menor a 10", str)

def test_lab_9():
    assert isinstance(Laboratorio01.contadorDigitos("132033483", 13), str) == isinstance("Error: El parámetro num debe ser de tipo entero", str)

def test_lab_10():
    assert isinstance(Laboratorio01.contadorDigitos(132033483, "13"), str) == isinstance("Error: El parámetro digito debe ser de tipo entero", str)

##################################################################

def test_lab_11():
    assert Laboratorio01.calculadora (1, 4, 8) == 12

def test_lab_12():
    assert Laboratorio01.calculadora (2, 4, 8) == -4
    
def test_lab_13():
    assert Laboratorio01.calculadora (3, 4, 8) == 32

def test_lab_14():
    assert Laboratorio01.calculadora (4, 10, 8) == 1

def test_lab_15():
    assert isinstance(Laboratorio01.calculadora (14, 4, 8), str) == isinstance("Error: El parámetro operacion debe ser un valor menor a 5", str)

##################################################################

def test_lab_16():
    assert Laboratorio01.sumatoria_V2(1, 5, 1, 0)  == 15
    
def test_lab_17():
    assert Laboratorio01.sumatoria_V2(1, 5, 1, 2)  == 9
    
def test_lab_18():
    assert Laboratorio01.sumatoria_V2(1, 5, 3, 2)  == 1
    
def test_lab_19():
    assert Laboratorio01.sumatoria_V2(10, 8, -1, 0)  == 27
    
def test_lab_20():
    assert isinstance(Laboratorio01.sumatoria_V2(10, 5, 3, 2), str)  == isinstance("Error: el parámetro inicio debe ser menor o igual a fin", str)

def test_lab_21():
    assert isinstance(Laboratorio01.sumatoria_V2(10, 15, -3, 2), str)  == isinstance("Error: El parámetro de fin debe ser menor o igual a inicio", str)

def test_lab_22():
    assert isinstance(Laboratorio01.sumatoria_V2("10", 15, -3, 2), str)  == isinstance("Error: Los parámetros deben ser enteros", str)

def test_lab_23():
    assert isinstance(Laboratorio01.sumatoria_V2(10, 15, 10, 2), str)  == isinstance("Error: El parámetro distancia debe estar en 1 a 9", str)
