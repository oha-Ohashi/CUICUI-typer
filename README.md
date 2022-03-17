# くいくいタイパー

友達とリアルタイム対戦できることがウリの、CUIライクタイピングゲーム！！

[プレイはこちらから](https://www.ketcha.xyz/cuicui "くいくいタイパー")


# 環境構築

python, flaskが必要です。

[注意]このリポジトリをクローンして`app.py`を実行しただけでは動作しません！

このようなファイル構成を作った上、

├── server.py

├── cuicui

│   ├── app.py

│   └── 

server.pyにこのように記述してください。
```python:server.py
from cuicui.app import app

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
```
