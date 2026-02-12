class PhilosopherChatError(Exception):
    pass


class BadRequestError(PhilosopherChatError):
    pass


class NotFoundError(PhilosopherChatError):
    pass


class PermissionDeniedError(PhilosopherChatError):
    pass


class LLMError(PhilosopherChatError):
    pass
