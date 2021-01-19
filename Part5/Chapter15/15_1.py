class MyOpen:

    def __init__(self,file_name):
        '''initial'''
        self.file_name = file_name
        self.file_handler = None
        return
    def __enter__(self):
        print("enter:",self.file_name)
        self.file_handler = open(self.file_name,"r")
        return self.file_handler
    def __exit__(self,exc_type,exc_val,exc_tb):
        print('exit:',exc_type,exc_val,exc_tb)
        if self.file_handler:
            self.file_handler.close()
        return True

with MyOpen("15_1.py") as file_in:
    for i in file_in.readlines():
        print(i)
    for line in file_in:
        pass
