from fastapi import HTTPException, status


class DatabaseException(HTTPException):
    def __init__(
        self,
        detail: str = "Server Error...Something went wrong...Please try again later",
    ) -> None:
        super().__init__(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=detail,
        )


class BadRequestException(HTTPException):
    def __init__(self, detail: str = "Incorrect data") -> None:
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)
