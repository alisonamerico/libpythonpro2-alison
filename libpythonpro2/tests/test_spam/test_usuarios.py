from libpythonpro2.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Alison')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Alison'), Usuario(nome='Luciano')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
