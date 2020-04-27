
import pytest

from libpythonpro2.spam.enviador_de_email import Enviador
from libpythonpro2.spam.main import EnviadorDeSpam
from libpythonpro2.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Alison', email='alison@python.pro.br'),
            Usuario(nome='Luciano', email='luciano@python.pro.br')
        ],
        [
            Usuario(nome='Alison', email='alison@python.pro.br')
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'alison@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Alison', email='alison@python.pro.br')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luciano@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert enviador.parametros_de_envio == (
        'luciano@python.pro.br',
        'alison@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
