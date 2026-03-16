import sys
import os
def get_error_details(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    lineno=exc_tb.tb_lineno
    return f"error occured in filename [{file_name}] at line [{lineno}] error [{str(error)}] "
class CustomException(Exception):
    def __init__(self,error,error_detail:sys):
        super().__init__(error)
        self.error=get_error_details(error,error_detail)
    def __str__(self):
        return self.error