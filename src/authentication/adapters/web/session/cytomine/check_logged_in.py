from authentication.adapters.web.session.check_logged_in import (
    CheckLoggedInInterface,
)


class CheckLoggedInUseCaseImpl(CheckLoggedInInterface):
    def __init__(self, session_service: SessionService):
        self.session_service = session_service

    def execute(self, user_id: int) -> bool:
        # Verificar se o usuário está logado com base no ID do usuário
        return self.session_service.is_user_logged_in(user_id)
