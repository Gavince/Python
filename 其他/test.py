
import argparse
# 创建解析步骤
parser = argparse.ArgumentParser(description='Process some integers.')

# 添加参数步骤
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers')
# 解析参数步骤  
args = parser.parse_args()
print(args.accumulate(args.integers))
