import os
import os.path
import json

def get_size(dirpath='.'):
    tot_size = 0
    content = dict()

    for file_name in os.listdir(dirpath):
        file_name = os.path.join(dirpath, file_name)

        if os.path.isfile(file_name):
            size = os.stat(file_name).st_size
            content[file_name] = size
            tot_size += size
        
    content['total'] = tot_size    
    return json.dumps(content, indent=4)


