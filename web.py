from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!doctype html>
<html>
<head>
    <title>TCP/IP</title>
    <style>
        body {
            background-color: skyblue;
            font-family: Arial, sans-serif;
            margin: 40px;
        }
        h1 {
            color: darkblue;
            text-align: center;
        }
        h3 {
            background-color: white;
            padding: 20px;
            border-radius: 10px;
        }
        ul {
            line-height: 1.8;
        }
        .footer {
            margin-top: 50px;
        }
        .top-button {
            position: fixed;
            bottom: 20px;
            right: 20px;
            padding: 10px;
            background-color: navy;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
    <script>
        function scrollToTop() {
            window.scrollTo({top: 0, behavior: 'smooth'});
        }
    </script>
</head>
<body>
    <h1>TCP/IP PROTOCOLS</h1>
    <h3>
        <ul>
            <li><b>Application layer protocols:</b> HTTP, FTP, SSH, DNS, TELNET</li>
            <li><b>Transport layer protocols:</b> TCP, UDP</li>
            <li><b>Internet layer protocols:</b> IPv4, IPv6</li>
            <li><b>Physical layer protocols:</b> ETHERNET</li>
        </ul>
        <div class="footer">
            Name: F.S.STEFFY AAVLIN RAJ<br>
            Register no: 212224040330
        </div>
    </h3>
    <button class="top-button" onclick="scrollToTop()">Back to Top</button>
</body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET request received...")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver")
server_address = ('', 8000)
httpd = HTTPServer(server_address, MyServer)
httpd.serve_forever()
