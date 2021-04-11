import pytest
import Modulo
import ModuloContaTempos

class TestaOrdenador:

    @pytest.fixture
    def o(self):
        return Modulo.Ordenador()

    @pytest.fixture
    def l_quase(self):
        return ModuloContaTempos.ContaTempos().lista_quase_ordenada(100)

    @pytest.fixture
    def l_aleatoria(self):
        return ModuloContaTempos.ContaTempos().lista_aleatoria(100)

    def test_bolha_curta_aleatoria(self,o,l_aleatoria):
        o.bubbleSortCurta(l_aleatoria)
        assert o.corrige(l_aleatoria)

    def test_selecao_direta_aleatoria(self,o,l_aleatoria):
        o.selecao_direta(l_aleatoria)
        assert o.corrige(l_aleatoria)

    def test_bolha_curta_quase(self,o,l_quase):
        o.bubbleSortCurta(l_quase)
        assert o.corrige(l_quase)

    def test_selecao_direta_quase(self,o,l_quase):
        o.selecao_direta(l_quase)
        assert o.corrige(l_quase)
    
    
