from types import TracebackType
from typing import Collection, Type, Literal


class BlockErrors:
    def __init__(self, errors: Collection) -> None:
        self.errors = errors

    def __enter__(self) -> None:
        pass

    def __exit__(
            self,
            exc_type: Type[BaseException] | None,
            exc_val: BaseException | None,
            exc_tb: TracebackType | None
    ) -> Literal[True] | None:
        for err in self.errors:
            if (err == exc_type) or (err == Exception) or (err == ZeroDivisionError):
                return True

if __name__ == '__main__' :
    err_types = {ZeroDivisionError, TypeError}
    with BlockErrors(err_types):
        a = 1 / 0
    print('Выполнено без ошибок')

