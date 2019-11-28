"""
编写一个Point2D的用例，从命令行接受一个整数N。在单位正方形中生成N个随机点，然后计算两点之间的最近距离
absl库的用法参见：https://blog.csdn.net/chr1991/article/details/94492128
"""
from absl import app, flags
import random
FLAGS = flags.FLAGS
flags.DEFINE_integer('N', None, 'a number')
# 指定必须输入的参数
flags.mark_flag_as_required("N")
class Point2D():
    def __init__(self, N):
        self.N = N
        self.point = []
    
    def generate_random_point(self):
        for i in range(self.N):
            self.point.append([random.random(), random.random()])
    def compute_distance(self, point_a, point_b):
        return ((point_a[0] - point_b[0])**2 + (point_a[1] - point_b[1])**2)**0.5
        
    def out_min_distance(self):
        self.generate_random_point()
        min_distance = 1e10
        for i in range(self.N):
            for j in range(i+1, self.N):
                distance = self.compute_distance(self.point[i], self.point[j])
                if distance < min_distance:
                    min_distance = distance
        return min_distance

def main(argv):
    del argv
    ss = Point2D(FLAGS.N)
    print(ss.out_min_distance())

if __name__ == "__main__":
    app.run(main)

"""
命令行运行：
python 1.2.1.py --N=5

"""