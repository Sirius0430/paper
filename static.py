# 一些常数
import numpy as np

# Deprecated
# buildingP = np.array([0.01, 0.02, 0.03, 0.04, 0.90])  # 想去某个建筑的意愿 正式启用时需要修改
# buildingLocation = [[100, 100], [100, 900], [700, 300], [500, 500]]
# # 两个建筑物之间的道路，road[起始点][终点]
# road = [[[],[],[],[],[]],
#     [[],[], [(100, 100), (100, 900)], [(100, 100), (500, 100), (500, 300), (700, 300)],[(100, 100), (500, 100), (500, 500)]],
#     [[],[(100, 900), (100, 100)], [], [(100, 900), (500, 900), (500, 300), (700, 300)],[(100, 900), (500, 900), (500, 500)]],
#     [[],[(700, 300), (500, 300), (500, 100), (100, 100)], [(700, 300), (500, 300), (500, 900), (100, 900)], [],[(700, 300), (500, 300), (500, 500)]],
#     [[],[(500, 500), (500, 100), (100, 100)], [(500, 500), (500, 900), (100, 900)], [(500, 500), (500, 300), (700, 300)],[]]
# ]

# Now Using
# popDistribution = np.load("data/PopDistribution.npy")  # 人口分布密度，用于随机生成用户
speed = [1, 5, 15]  # 行人，自行车，汽车 m/s,实际中一格=10m，需要除10(或规定10s记录一次）
speedPoss = []  #选择速度的可能性
oriPoss = [0.2, 0.2, 0.2, 0.2, 0.2]  # 选择前进方向时的可能性
time = 30  # 每次迭代的间隔时间（单位s）
mapSize = 1000  # 地图大小
userNum = 1000  # 用户数量

interval = 300  # 找人的间隔（单位s）
bluetoothDistance = 500  # 蓝牙连接距离
userPerIter = 7  # 每轮循环的验证人数

test = 0
