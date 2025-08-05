# ORゲートを関数で実装する
def OR(x1, x2):
   x = np.array([x1, x2])   # 入力xの大きさ
   w = np.array([0.5, 0.5]) # 重みw
   b = -0.2

   temp = np.sum(w*x) + b   #x1*w1+x2*w2+bができる

   if temp <= 0: # θ=-bなのでしきい値が0
       return 0
   else:
       return 1
     
# 関数の使用
print(OR(0, 0)) # 0
print(OR(0, 1)) # 1
print(OR(1, 0)) # 1
print(OR(1, 1)) # 1
