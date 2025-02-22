// 帮我写一个网页, 浏览器打开本地的 5555 端口,会显示一个"Hello World!"
import { createServer } from 'http';
const port = 5555;
const server = createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World!');
});
server.listen(port);

// 我使用 protobuf 时发生报错:
// Error while extracting response for type [class com.nowcoder.ut.idl.HomeRecV8$HomeRankV8Response] and content type [application/x-protobuf];nested exception is com.google.protobuf.InvalidProtocolBufferException:
// While parsing a protocol message, the input ended unexpectedly in the middle of a field. 
// This could mean either that the input has been truncated or that an embedded message misreported its own length.
// feign.codec.DecodeException:
// Error while extracting response for type [class com.nowcoder.ut.idl.HomeRecV8$HomeRankV8Response] and content type [application/x-protobuf];
// nested exception is com.google.protobuf.InvalidProtocolBufferException:
// While parsing a protocol message, the input ended unexpectedly in the middle of a field. 
// This could mean either that the input has been truncated or that an embedded message misreported its own length.