import sys
import os
import logging
from datetime import datetime


def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = (
        "Error occured in python script name [{0}] "
        "line number [{1}] error message[{2}]"
    ).format(file_name, exc_tb.tb_lineno, str(error))

    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message


def setup_exception_logging():
    """Create exception folder and setup logging for exceptions."""
    exc_folder = os.path.join(os.getcwd(), "exceptions")
    os.makedirs(exc_folder, exist_ok=True)

    exc_file = (
        f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}_exception.log"
    )
    exc_file_path = os.path.join(exc_folder, exc_file)

    log_format = (
        "[ %(asctime)s ] %(lineno)d %(name)s - "
        "%(levelname)s - %(message)s"
    )
    logging.basicConfig(
        filename=exc_file_path,
        format=log_format,
        level=logging.ERROR,
    )

    return exc_folder, exc_file_path


if __name__ == "__main__":
    exc_folder, exc_file_path = setup_exception_logging()
    print(f"Exception Folder: {exc_folder}")
    print(f"Exception File Path: {exc_file_path}")

    try:
        print("Testing exception handling with 1/0...")
        result = 1 / 0
    except ZeroDivisionError as e:
        try:
            raise CustomException(str(e), sys) from e
        except CustomException as ce:
            logging.error(str(ce))
            print(f"Exception caught: {ce}")
            print(f"Exception logged to: {exc_file_path}")

