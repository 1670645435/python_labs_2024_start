# 创建一个空列表
fruits = []
print(fruits)  # 输出: []

# 添加元素
fruits.append("苹果")
fruits.append("香蕉")
fruits.append("橙子")
print(fruits)  # 输出: ['苹果', '香蕉', '橙子']

# 访问列表中的水果
first_fruit = fruits[0]
second_fruit = fruits[1]
print(first_fruit)  # 输出: 苹果
print(second_fruit)  # 输出: 香蕉

# 修改列表中的水果
fruits[0] = "草莓"
print(fruits)  # 输出: ['草莓', '香蕉', '橙子']

# 遍历列表中的水果
for fruit in fruits:
    print("遍历" + fruit)