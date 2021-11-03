from flask import Flask, request, render_template

app= Flask(__name__)


@app.route('/')
def index():
  comment = "テスト表示だよ"
  return render_template('index.html', comment=comment)

@app.route('/result', methods=['POST'])
def optimize_task():
  if request.method == 'POST':
    data = request.form.getlist("deadLine")
    print(data)
    comment = "テスト表示だよ"
  return render_template('index.html', comment=comment)

if __name__ == '__main__':
  app.run(debug=True)