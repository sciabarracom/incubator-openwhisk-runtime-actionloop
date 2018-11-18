var main = require("./exec__")
var fs = require("fs")

process.stdin.setEncoding('utf8');
process.out = fs.createWriteStream(null, { fd: 3 });
//process.out.setEncoding('utf8')
process.stdin.on('readable', function() {
  var line = process.stdin.read();
  if (line !== null) {
    try {
        var args = JSON.parse(line)
        var value = args.value || {}
        var result = main(value)
        process.out.write(JSON.stringify(result)+"\n");
    } catch(err) {
        var error = {"error": err}
        process.out.write(JSON.stringify(error)+"\n");
    }
  }
})
