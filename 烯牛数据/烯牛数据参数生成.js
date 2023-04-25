var crypto = require("crypto")
var _keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    , _p = "W5D80NFZHAYB8EUI2T649RT2MNRMVE2O"

function _u_e(e) {
    if (null == e)
        return null;
    e = e.replace(/\r\n/g, "\n");
    for (var t = "", n = 0; n < e.length; n++) {
        var r = e.charCodeAt(n);
        r < 128 ? t += String.fromCharCode(r) : r > 127 && r < 2048 ? (t += String.fromCharCode(r >> 6 | 192),
            t += String.fromCharCode(63 & r | 128)) : (t += String.fromCharCode(r >> 12 | 224),
            t += String.fromCharCode(r >> 6 & 63 | 128),
            t += String.fromCharCode(63 & r | 128))
    }
    return t
}

function e1(e) {
    if (null == e)
        return null;
    for (var t, n, r, o, i, a, c, u = "", s = 0; s < e.length;)
        o = (t = e.charCodeAt(s++)) >> 2,
            i = (3 & t) << 4 | (n = e.charCodeAt(s++)) >> 4,
            a = (15 & n) << 2 | (r = e.charCodeAt(s++)) >> 6,
            c = 63 & r,
            isNaN(n) ? a = c = 64 : isNaN(r) && (c = 64),
            u = u + _keyStr.charAt(o) + _keyStr.charAt(i) + _keyStr.charAt(a) + _keyStr.charAt(c);
    return u
}

function e2(e) {
    if (null == (e = _u_e(e)))
        return null;
    for (var t = "", n = 0; n < e.length; n++) {
        var r = _p.charCodeAt(n % _p.length);
        t += String.fromCharCode(e.charCodeAt(n) ^ r)
    }
    return t
}

function sig1(e) {
    return md5(e + _p).toUpperCase()
}

function md5(text) {

    return crypto.createHash('md5').update(text).digest('hex');

}

function main() {
    // 分页参数
    h = {}
    pay1 = {
        "tagId": 604330,
        "size": 5
    }
    h['payload'] = e1(e2(JSON.stringify(pay1)))
    h['sig'] = sig1(h['payload'])
    return h
}

