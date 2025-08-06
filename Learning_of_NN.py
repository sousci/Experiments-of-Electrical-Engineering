import numpy as np
alpha = 0.01 # 学習率

N = 5 # 訓練データの数
M = 3  # テストデータの数

w = np.array([0.1, 0.1, 0.1]) # 重みパラメータの初期化

# 訓練データ
train = np.array([[3, 2, 1],
                  [2, 1, 0],
                  [4, 1, 0],
                  [5, 2, 1],
                  [5, 1, 1]])
# テストデータ
test = np.array([[1, 1],
              [3, 1],
              [6, 2]])

print("初期重み：[w0]={w0}, [w1]={w1}, [w2]={w2}".format(w0 = round(w[0],5), w1 = round(w[1],5), w2 = round(w[2],5)))
for epoc in range(10):
    for i in range(N): #訓練データで重みの更新
        # 出力の大きさ
        y = -1*w[0] + train[i][0]*w[1] + train[i][1]*w[2]
        # 誤差
        E = train[i][2] - np.where(y >= 0, 1, 0) # 出力を活性化関数に入れて計算
        # 重みの更新
        w[0] += alpha*E*-1
        w[1] += alpha*E*train[i][0]
        w[2] += alpha*E*train[i][1]
    print("{count}回目：[w0]={w0}, [w1]={w1}, [w2]={w2}".format(count = epoc+1, w0 = round(w[0],5), w1 = round(w[1],5), w2 = round(w[2],5)))

# テストデータを入力した結果を表示
for i in range(M):
    print(np.where(-1*w[0] + test[i][0]*w[1] + test[i][1]*w[2]>=0, 1, 0))
