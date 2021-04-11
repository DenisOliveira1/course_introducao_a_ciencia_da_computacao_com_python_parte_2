import ModuloBhaskara
import pytest

class TesteBhaskara:

    @pytest.fixture
    def b(self):
            return ModuloBhaskara.Bhaskara()#modulo.class = cria objeto

    def teste(self, b):
        assert b.calcula_raizes(1,0,0) == (1,0)

    def teste_duas_raizes(self, b):
        assert b.calcula_raizes(1,-5,6) == (2,3,2)

    def teste_zero_raizes(self, b):
        assert b.calcula_raizes(10,10,10) == (0)

    def teste_raizes_negativas(self, b):
        assert b.calcula_raizes(10,20,10) == (1,-1)

    @pytest.mark.parametrize("b,entrada , esperado",[
        (b,(1,0,0),(1,0))
        ])
    
    def teste_geral(self,b,entrada,esperado):
        assert b(self).calcula_raizes(entrada[0],entrada[1],entrada[2]) == esperado
