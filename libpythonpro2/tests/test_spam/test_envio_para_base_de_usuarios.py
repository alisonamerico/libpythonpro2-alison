from libpythonpro2.spam.enviador_de_email import Enviador
from libpythonpro2.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'alison@python.pro.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
