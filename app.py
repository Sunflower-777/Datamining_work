from flask import Flask, request, render_template
import numpy as np
from apps.optTask import optTask

app= Flask(__name__)


@app.route('/')
def index():
  comment = "テスト表示だよ"
  return render_template('index.html', comment=comment)

@app.route('/result', methods=['POST'])
def optimize_task():
  if request.method == 'POST':
    taskName = request.form.getlist("taskName")
    neededTime = request.form.getlist("neededTime")
    upperDifficulty = request.form.getlist("upperDifficulty")
    lowerDifficulty = request.form.getlist("lowerDifficulty")
    deadLine = request.form.getlist("deadLine")
    usableTime = request.form.getlist("usableTime")

    taskNum = len(taskName)
    period = len(usableTime)
    # print(taskNum)
    # print(period)
    difficulty = [float(h) for h in (upperDifficulty+lowerDifficulty)*period]
    # print(difficulty)
    workTime = [float(t) for t in neededTime]
    timePerDate = [float(t) for t in usableTime]
    deadLine = [float(t) for t in deadLine]
    
    comment = "データ送信済みだよ"

    task = np.array(optTask(taskNum, period, difficulty, workTime, timePerDate, deadLine))

    task = task.reshape([period, -1])
    daylyTasks = dict()
    for i, t in enumerate(task):
      daylyTask = {}
      for n in range(taskNum):
        key = taskName[n]
        daylyTask[key] = workTime[n] * (t[n] + t[n+taskNum])
      daylyTasks[i+1] = daylyTask

    return render_template('todo.html', daylyTasks=daylyTasks)
  else:
    comment = "ちゃんと入れてね"


  return render_template('index.html', comment=comment)

if __name__ == '__main__':
  app.run(debug=True)