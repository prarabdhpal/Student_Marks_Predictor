import sys
from src.logger import logging

def error_message_detail(error, error_detail=sys.exc_info()):
    """Formats a detailed error message with file name and line number."""
    _, _, exc_tb = error_detail
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = (
        f"Error occurred in Python script name [{file_name}] "
        f"line number [{line_number}] error message[{error}]"
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error, error_detail=sys.exc_info()):
        """Initializes the exception with a detailed error message."""
        super().__init__(str(error))
        self.error_message = error_message_detail(error, error_detail)

    def __str__(self):
        """Returns the detailed error message."""
        return self.error_message