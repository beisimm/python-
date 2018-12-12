function(e) {
                var n = JSON.parse(e).data;
                if (0 == n.code) {
                    t.password = t.password.split("").reverse().join(""),
                    setMaxDigits(130);
                    var o = new RSA(n.e,"",n.n)
                      , r = encryptedString(o, t.password);
                    t.password = r,
                    t.rKey = n.rkey
                } else
                    toast("公钥获取失败"),
                    t.rKey = "";
                ajaxFunc("post", "http://activity.renren.com/livecell/ajax/clog", t, function(e) {
                    var e = JSON.parse(e).logInfo;
                    0 == e.code ? location.href = localStorage.getItem("url") || "" : toast(e.msg || "登录出错")
                })
            }