const http = require('http');
const fs = require('fs');
const port = 8080;

const server = http.createServer((req, res) => {
  fs.readFile('./index.html', 'utf8', (err, data) => {
    if (err) {
      res.writeHead(500);
      res.end('Error reading the file.');
      return;
    }

    // Replace the placeholder with the environment variable value
    const appColor = process.env.APP_COLOR || 'gray';
    const modifiedData = data.replace(/#APP_COLOR#/g, appColor);

    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(modifiedData);
  });
});

server.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
