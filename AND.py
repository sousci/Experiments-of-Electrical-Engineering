# ANDゲートを関数で実装する
def AND(x1, x2):
   x = np.array([x1, x2])   # 入力xの大きさ
   w = np.array([0.5, 0.5]) # 重みw
   b = -0.7 # θで言えば0.7

   temp = np.sum(w*x) + b   #x1*w1+x2*w2+bができる

   if temp <= 0: # θ=-bなのでしきい値が0
       return 0
   else:
       return 1

# 関数の使用
print(AND(0, 0)) # 0
print(AND(0, 1)) # 0
print(AND(1, 0)) # 0
print(AND(1, 1)) # 1
