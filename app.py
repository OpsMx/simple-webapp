import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # Get the background color from the APP_COLOR environment variable (default: gold)
    color = os.environ.get('APP_COLOR', '#FFD700')
    
    # Get the container name from the host
    container_name = os.environ.get('HOSTNAME', 'Unknown')

    html_content = f'''
    <!DOCTYPE html>
    <html>
    <head>
      <title>Sample Web Application</title>
      <style>
        body {{
          background-color: {color};
          color: white;
          font-family: Arial, sans-serif;
          text-align: center;
          padding-top: 100px;
        }}
      </style>
    </head>
    <body>
      <h1>Welcome to Container: {container_name}</h1>
    </body>
    </html>
    '''
    return html_content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
