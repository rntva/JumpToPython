import numpy as np

def softmax(a) :
    c = np.max(a)
    exp_a = np.exp(a - c)
    # exp_a = np.exp(a) # 이렇게만 하면 softmax 함수 실행시 runtime어쩌고 워닝이 뜨고 nan(not a number)으로 나온다.
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

a = np.array([1010, 1000, 990])
print(softmax(a))

c = np.max(a)
print(a - c)

print(softmax(a - c))

a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y)
print(np.sum(y))