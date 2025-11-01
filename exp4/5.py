"""
5、实验题目：创建子类
如下现有一个保险政策类InsurancePolicy。
class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item
1）创建子类：交通险VehicleInsurance，构造方法中通过super将保额存储到实例变量中，同时用实例变量vehicle_Name存储交通工具的名字。创建一个实例方法get_rate（），返回回报率：保额*0.001
2）创建子类：家庭险HomeInsurance。构造方法中通过super将保额存储到实例变量中，同时用实例变量member_number存储家庭成员的人数。创建一个实例方法get_rate（），返回回报率：保额*0.00005
"""


class InsurancePolicy:
    def __init__(self, price_of_item):
        self.price_of_insured_item = price_of_item


class VehicleInsurance(InsurancePolicy):
    def __init__(self, price_of_item, vehicle_name):
        super().__init__(price_of_item)
        self.vehicle_name = vehicle_name

    def get_rate(self):
        return self.price_of_insured_item * 0.001


class HomeInsurance(InsurancePolicy):
    def __init__(self, price_of_item, member_number):
        super().__init__(price_of_item)
        self.member_number = member_number

    def get_rate(self):
        return self.price_of_insured_item * 0.00005


def test():
    # 测试交通险
    vehicles = [
        VehicleInsurance(150000, "Toyota Camry"),
        VehicleInsurance(800000, "BMW X5"),
        VehicleInsurance(50000, "Honda Motorcycle"),
    ]

    for i, vehicle in enumerate(vehicles, 1):
        rate = vehicle.get_rate()
        print(
            f"测试{i}: {vehicle.vehicle_name} - 保额:{vehicle.price_of_insured_item}, 回报率:{rate}"
        )

    # 测试家庭险
    homes = [
        HomeInsurance(300000, 3),
        HomeInsurance(1000000, 6),
        HomeInsurance(150000, 1),
    ]

    for i, home in enumerate(homes, 1):
        rate = home.get_rate()
        print(
            f"测试{i}: {home.member_number}人家庭 - 保额:{home.price_of_insured_item}, 回报率:{rate}"
        )


# 运行测试
test()
