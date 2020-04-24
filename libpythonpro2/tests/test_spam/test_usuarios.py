from libpythonpro2.spam.db import Conexao
from libpythonpro2.spam.modelos import Usuario


def test_salvar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuario = Usuario(nome='Alison')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()


def test_listar_usuarios():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuarios = [Usuario(nome='Alison'), Usuario(nome='Luciano')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()
