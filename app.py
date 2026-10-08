from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>CI/CD Reactive App</title>
    <style>body { font-family: Arial; text-align: center; padding: 50px; }</style>
</head>
<body>
    <h1>System Status: <span id="status" style="color: red;">Offline</span></h1>
    <button onclick="checkStatus()">Run Diagnostics</button>
    <script>
        function checkStatus() {
            let statusEl = document.getElementById("status");
            statusEl.innerText = "Checking...";
            statusEl.style.color = "orange";
            setTimeout(() => {
                statusEl.innerText = "Online & Deployed!";
                statusEl.style.color = "green";
            }, 1000);
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

@app.route('/api/health')
def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)