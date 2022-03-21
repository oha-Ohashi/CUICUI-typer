# Links
<ul>
	<li><a href="https://www.ketcha.xyz/cuicui">くいくいタイパー</a> </li>
	<li><a href="https://www.ketcha.xyz/ortho_heat">オルソリひーと | Ortho Heat</a> </li>
	<li><a href="https://www.ketcha.xyz/ortho_typing">オルソリふぉーる | Ortho Fall</a> </li>
</ul>


# How to build

python and flask required.

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
