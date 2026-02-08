import sys
from network_security.logging import logger

def error_message_detail(error, error_detail: sys):
    """
    Extracts detailed error information: 
    - Filename where the error occurred
    - Line number 
    - Error message string
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, line_number, str(error)
    )

    return error_message

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        :param error_message: error message in string format
        :param error_detail: sys module to get detailed traceback
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
    

if __name__=="__main__":
    try:
        # 1. Basic config so logs actually show up in the console
        logger.logging.basicConfig(level=logger.logging.INFO)
        
        # 2. Use logging.info() directly, or define logger first
        logger.logging.info("Enter try block") 
        
        result = 1/0
    except Exception as e:
        # This will now catch the ZeroDivisionError and print it beautifully
        raise NetworkSecurityException(e, sys)         