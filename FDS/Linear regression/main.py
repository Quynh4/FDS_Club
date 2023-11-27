import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('Advertising.csv')
x = data.values[:, 2] #lấy tất cả các hàng của cột radio
y = data.values[:, 4] #cột sale
plt.scatter(x,y, marker='o')
#plt.show()

def predict(new_radio,m, b):
    return weight*new_radio + bias

def cost_function(x,y, m, b):
    n = len(x)
    sum_error = 0
    for i in range(n):
        sum_error += (y[i] - (m*x[i]+b))**2
    return  sum_error/n

def update_weight(x, y, m,b, learning_rate ):
    n= len(x)
    m_tempt = 0.0
    b_tempt = 0.0
    for i in range(n):
        m_tempt += -2*x[i]*(y[i] - (m*x[i]+b))
        b_tempt += -2*(y[i] - (m*x[i]+b))
    m -= (m_tempt/n)*learning_rate
    b -=(b/n)*learning_rate
    return  m,b

def train(x, y, m,b, learning_rate, iter):
    cos_his = []
    for i in range(iter):
        m, b = update_weight(x, y, m,b, learning_rate)
        cost = cost_function(x,y, m, b)
        cos_his.append(cost)

    return m,b, cos_his

m,b, cost= train(x,y, 0.03, 0.0014, 0.001, 30)
print("ket qua:")
print(m)
print(b)
print(cost)

print('gia tri du doan:')
print(predict(19, m,b))

solanlap = [i for i in range(30)]
plt.plot(solanlap, cost)
plt.show()