import json
import collections
import sys
import os 


def write_json(res: list) -> None:
    """
    """
    res = []
    with open("file.json") as f:
        for line in f.readlines():
            val = json.loads(line)
            val = eval(val)
            res.append(val)
    f.close()
    print(res)
            


def read_json(path: str) -> list:
    """读取json文件.
    读取json 并对文件实现处理.
        
    
    Arg:
        
        
    Return:
        

    """


    res = []
    with open(path, "r") as f:
        for line in f.readlines():
            try:
                val = json.dumps(line.strip("\n"))
                print(val)
            except:
                continue
    f.close()
    
    return res 

if __name__ == "__main__":
    if len(sys.argv) == 1:
        msg = f"PATH ERROR:{sys.argv[0]} 缺少路径"
        print(msg)
        exit()
    path = sys.argv[1]
    res = read_json(path)
    write_json(res)






