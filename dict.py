# 创建一个空字典
fruits = {}
print(fruits)  # 输出: {}

# 向字典中添加键值对
fruits['apple'] = 3
fruits['banana'] = 5
print(fruits)  # 输出: {'apple': 3, 'banana': 5}

# 访问字典中的值
apple_count = fruits['apple']
print(apple_count)  # 输出: 3

# 更新字典中的值
fruits['apple'] = 4
print(fruits)  # 输出: {'apple': 4, 'banana': 5}

# 删除字典中的键值对
del fruits['banana']
print(fruits)  # 输出: {'apple': 4}

# 遍历字典
for fruit, count in fruits.items():
    print(f"Fruit: {fruit}, Count: {count}")
# 输出:
# Fruit: apple, Count: 4