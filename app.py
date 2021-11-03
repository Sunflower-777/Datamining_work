from flask import Flask, request, render_template

app= Flask(__name__)


@app.route('/')
def optimize_task():
  comment = "テスト表示だよ"
  return render_template('index.html', comment=comment)



if __name__ == '__main__':
  app.run(debug=True)