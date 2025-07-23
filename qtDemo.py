/**************/

12

5600t1e1s1t11178
5600t2e2s2t1178

def add_two_numbers(a, b, c=0):
    """这个函数接收两个参数并返回它们的和"""
    return a + b + c

if __name__ == "__main__":
    # 测试第一个函数
    num1 = 5
    num2 = 7
    print(f"{num1} + {num2} = {add_two_numbers(num1, num2)}")
    num3 = 10
    print(f"{num1} + {num2} + {num3}= {add_two_numbers(num1, num2, num3)}")