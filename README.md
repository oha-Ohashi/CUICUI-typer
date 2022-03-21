[https://www.ketcha.xyz/cuicui](https://www.ketcha.xyz/cuicui "くいくいタイパー")

[オルソリひーと | Ortho Heat](https://www.ketcha.xyz/ortho_heat "オルソリひーと | Ortho Heat")

[オルソリふぉーる | Ortho Fall](https://www.ketcha.xyz/ortho_typing "オルソリふぉーる | Ortho Fall")

# How to build

python, flas required.

files and folders:

├── server.py<br>
├── cuicui(this repository)<br>
│   ├── app.py<br>
│   └── <br>

`server.py`
```python:server.py
from cuicui.app import app

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
```
