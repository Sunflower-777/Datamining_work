import numpy as np
import cvxpy as cp

"""
taskNum(int): タスクの数
period(int): 費やす日数
difficukty(list): 精神的ハードル的なタスク遂行難易度てきな急かされた時とそうでない時の辛さを入れる
workTime(list): タスク1コマにつきどのくらい時間をかけるか(h)
timePerDate(list): 1日に費やせる時間(h)
deadLine(list): 締め切りをperiodに対応させて、費やすコマ数で入力。コマ数は自力で考えてくれ
"""
def optTask(taskNum, period, difficulty, workTime, timePerDate, deadLine):
  x = cp.Variable(taskNum*2*period, integer=True)
  # 問題
  c = np.array(difficulty*period).T

  # 作業にかけられる時間
  perOne = workTime + [0]*taskNum
  perNull = [0]*taskNum*2

  T = []
  counter = 0
  for dd in range(period):
    t = []
    for d in range(period):
      if d == counter:
        t += perOne
      else:
        t += perNull
    T.append(t)
    counter += 1
  G1 = np.array(T)
  h1 = np.array(timePerDate).T
  print("G1: ", G1)
  print("h1: ", h1)

  W = []
  for i in range(period):
    dayly = []
    
    taskCount = 0
    for _ in range(taskNum):
      day = 0
      daylyOne = []
      for d in range(period):
        # 当日のタスク
        one = []
        if d == i:
          for j in range(taskNum*2):
            if j % (taskNum*2) == taskCount:
              one += [-1]
            elif j % taskNum == taskCount:
              one += [1]
            else:
              one += [0]
          one.reverse()
          daylyOne += one
        # 前日のタスク分
        elif i != 0 and d == i-1:
          for j in range(taskNum*2):
            if j % (taskNum*2) == taskCount:
              one += [1]
            else:
              one += [0]
          one.reverse()
          daylyOne += one
        else:
          one += [0]*(taskNum*2)
          daylyOne += one
        
        day += 1
      taskCount += 1
      dayly.append(daylyOne)
    dayly.reverse()
    W += dayly

  G2 = np.array(W)
  h2 = np.array(deadLine).T
  print("G2: ", G2)
  print("h2: ", h2)

  G3 = np.eye(taskNum*2*period)
  h3 = np.zeros(taskNum*2*period).T


  obj = cp.Minimize(c.T*x)
  cons = [G1*x<=h1, G2*x>=h2, G3*x>=h3]

  P = cp.Problem(obj, cons)
  P.solve()

  return x.value

if __name__=='__main__':
  taskNum = 3
  period = 3
  difficulty = [180, 250, 200, 80, 110, 120]
  workTime = [2, 5, 1.5]
  timePerDate = [3, 8, 8]
  deadLine = [1, 0, 0, 0, 0, 0, 0, 2, 2]

  print(optTask(taskNum, period, difficulty, workTime, timePerDate, deadLine))
