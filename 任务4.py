#1、请循环遍历出所有的key
# dict = {"k1":"v1","k2":"v2","k3":"v3"}
# for w in dict.keys():
#     print(w)
#2、请循环遍历出所有的value
# dict = {"k1":"v1","k2":"v2","k3":"v3"}
# for y  in dict.values():
#     print(y)
# 3、请在字典中增加一个键值对,"k4":"v4"
# dict = {"k1":"v1","k2":"v2","k3":"v3"}
# dict["k4"]="v4"
# print(dict)
# 用水果名称做key，金额做value，创建一个字典
# info={
#     "苹果":32.8,
#     "香蕉":22,
#     "葡萄":15.5}
# 小明，小刚去超市里购买水果
# 小明购买了苹果，草莓，香蕉，小刚购买了葡萄，橘子，樱桃，请从下面的描述的字典中，计算每个人花费的金额，并写入到money字段里。
# 以姓名做key，value仍然是字典
# our={
#     "苹果":12.3,
#     "草莓":4.5,
#     "香蕉":6.3,
#     "葡萄":5.8,
#     "橘子":6.4,
#     "樱桃":15.8}
# info={"小明":{"our":{
#     "苹果":12.3,
#     "草莓":4.5,
#     "香蕉":6.3,},
# "money":10086},
#     "小刚": {"our": {
#         "葡萄": 5.8,
#         "橘子": 6.4,
#         "樱桃": 15.8},
#         "money": 10086}}
# 有以下公司员工信息，将数据转换为字典方式（姓名作为键，其他作为值,张三:{xxx:xxx,xx:xxx}）
# names = {"刘备":["56","男","106","IBM", 500 ,"50"],
#          "大乔":["19", "女", "230", "微软", 501, "60"],
#          "小乔":["19", "女", "210", "Oracle", 600, "60"],
#          "张飞":["45", "男", "230", "Tencent", 700, "10"] }
# 编写一个函数，传入一个列表，并统计每个数字出现的次数。返回字典数据：{21:3,56:9,10:3}
# numbers_our=[21,56,10]
# def count_list_element(array):
#     result_return = {}
#     for i in array:
#         if result_return.__contains__(i):
#             result_return[i] = result_return[i] + 1
#         else:
#             result_return[i] = 1
#     return result_return
#
#
# result = count_list_element(numbers_our)
# print(result)
#
