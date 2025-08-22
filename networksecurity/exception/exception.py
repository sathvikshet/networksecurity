import sys
from networksecurity.logging import logger
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        self.error_message=error_message
        _,_,exc_tb=error_detail.exc_info()
        self.file_name=exc_tb.tb_frame.f_code.co_filename
        self.line_no=exc_tb.tb_lineno
    def __str__(self):
        return "Error occured in script name [{0}] at line number [{1}] error message [{2}]".format(
            self.file_name,
            self.line_no,
            str(self.error_message)
        )
    
if __name__=="__main__":
    try:
        logger.logging.info("Logging has started")
        a=1/0
        print("this will not be printed")
    except Exception as e:
        raise CustomException(e,sys)    