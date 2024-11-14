// 帮我写一个网页, 浏览器打开本地的 5555 端口,会显示一个"Hello World!"
import { createServer } from 'http';
const port = 5555;
const server = createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World!');
});
server.listen(port);
