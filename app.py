from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# Flag fayli
FLAG_FILE = os.path.abspath("flag.txt")

# HTML dizayni
HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Online Book Store</title>
    <style>
        body {
            margin:0;
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            color: #333;
        }
        header {
            background: #2c3e50;
            color: white;
            padding: 20px 0;
            text-align: center;
        }
        .container {
            width: 90%%;
            margin: 20px auto;
        }
        .books {
            display: grid;
            grid-template-columns: repeat(auto-fill,minmax(200px,1fr));
            gap: 20px;
        }
        .book {
            background: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 0 5px rgba(0,0,0,0.2);
            text-align: center;
            cursor: default;
        }
        .book img {
            max-width: 100%%;
            height: 250px;
            object-fit: cover;
            border-radius: 5px;
        }
        .book h3 {
            margin: 10px 0 5px 0;
            font-size: 18px;
        }
        .book p {
            font-size: 14px;
            color: #666;
        }
        .output-box {
            background: #0d1117;
            color: #c9d1d9;
            padding: 15px;
            border-radius: 5px;
            margin-top: 30px;
            white-space: pre-wrap;
            max-height: 300px;
            overflow-y: auto;
        }
    </style>
</head>
<body>
    <header>
        <h1>📚 Shadow Root Online Book Store</h1>
    </header>
    <div class="container">
        <div class="books">
            <div class="book">
		<img src=x>
                <a href="/?page=encrypt.txt">Cryptography</a>
                <p>Abdumutalov.B</p>
            </div>
            <div class="book">
                <img src=x>
		<a href="/?page=kitob.txt">Cybersecurity 1</a>
                <p>Abdumannonov.Sh</p>
            </div>
            <div class="book">
                <img src=x>
                <a href="/?page=osint.txt">Osint</a>
                <p>Aleksandrov.T</p>
            </div>
            <div class="book">
                <img src=x>
                <a href="/?page=social.txt">Social Enginering</a>
                <p>Pirimqulov.X</p>
            </div>
        </div>

        {% if content %}
        <div class="output-box">
            <strong>📄 File Output:</strong>\n
            {{ content }}
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    page = request.args.get("page")
    content = ""
    if page:
        try:
            path = os.path.abspath(page)
            with open(path, "r") as f:
                content = f.read()
        except Exception as e:
            content = f"[ERROR] {str(e)}"

    return render_template_string(HTML, content=content)


if __name__ == "__main__":
    print("CTF LFI Book Store running on http://0.0.0.0:5010")
    app.run(host="0.0.0.0", port=5010)

