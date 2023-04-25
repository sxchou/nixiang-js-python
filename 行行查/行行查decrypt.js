const Cryptojs = require('crypto-js')  //安装crypto-js (npm install crypto-js)
c = "3sd&d2"
r = "4h@$udD2s"
a = "*"
function decrypt(n, e) {
    e = e || "".concat(c).concat(r).concat(a);
    var t = Cryptojs.enc.Utf8.parse(e)
      , i = Cryptojs.AES.decrypt(n, t, {
        mode: Cryptojs.mode.ECB,
        padding: Cryptojs.pad.Pkcs7
    });
    return Cryptojs.enc.Utf8.stringify(i).toString()
}


