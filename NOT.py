# NOTゲートを関数で実装する
def NOT(x):
  x = np.array([x])   # 入力xの大きさ
  w = np.array([-0.5]) # 重みw
  b = 0.2

  temp = np.sum(w*x) + b

  if temp <= 0: # θ=-bなのでしきい値が0
      return 0
  else:
      return 1

# 関数の使用
print(NOT(0)) # 1
print(NOT(1)) # 0
