import os
 
 
def get_file_list(root='.', prefix=''):
    files = os.listdir(root)
    
    for f in files:
        if os.path.isfile( os.path.join(root, f) ):
            print('F', f"{prefix}{f}")
        else:
            print('D', f"{prefix}{f}")
            get_file_list(os.path.join(root, f), prefix+"    ")
            
# 현재 폴더 절대 경로            
cur_path = os.getcwd()
print(cur_path)   

get_file_list(cur_path) 
# get_file_list()