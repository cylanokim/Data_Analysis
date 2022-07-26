import pandas as pd 
import matplotlib.pyplot as plt 
import random
import simpy
import numpy as np


NUM_EMPLOYEES = 10

AVG_SUPPORT_TIME = 5
CUSTOMER_INTERVAL = 1
SIM_TIME = 60
customers_handled = 0 

class StarBux:
    def __init__(self, env, num_employees, support_time):
        self.env = env 
        self.staff = simpy.Resource(env, num_employees)
        self.support_time = support_time 

    def support(self, customer):
        service_time = max(1, np.random.normal(self.support_time, 2))
        # service_time = 5 
        yield self.env.timeout(service_time)
        print(f'{self.env.now} : 손님 {customer} 커피 완료')

def customer(env, name, starbux):
    global customers_handled 
    print(f'{env.now} : 손님 {name} 카페 도착')
    with starbux.staff.request() as request:
        yield request 
        print(f'{env.now} : 손님 {name} 주문 완료')
        yield env.process(starbux.support(name))
        print(f'{env.now} : 손님 {name} 카페 떠남') 
        customers_handled += 1

def setup(env, num_employees, support_time, customer_interval): 
    starbux = StarBux(env, num_employees, support_time)
    i = 0 

    while True:
        # 손님이은 평균 2분에 한 명씩 온다는 것으로 모델 수정
        # yield env.timeout(random.randint(customer_interval-1, customer_interval+1)) 
        yield env.timeout(0.5) 
        i += 1 
        env.process(customer(env, i, starbux))

print('Starbucks_Example-01_upgraded') 
env = simpy.Environment()
env.process(setup(env,  NUM_EMPLOYEES, AVG_SUPPORT_TIME, CUSTOMER_INTERVAL)) 
env.run(until=SIM_TIME) 
print('Customers handled: ' + str(customers_handled))
