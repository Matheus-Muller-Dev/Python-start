const http = require('http');

const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-type': 'application/json' });

    const clientInfo = {
        // method: req.method,
        // url: req.url,
        headers: req.headers,
        // remoteAddress: req.connection.remoteAddress,
        // remotePort: req.connection.remotePort,
    }
    res.end(JSON.stringify(clientInfo, null, 2));''
});

const PORT = 5000;
server.listen(PORT, () => {
    console.log(`Servidor rodando em http://localhost:${PORT}`)
})