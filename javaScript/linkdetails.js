/**
 * 这个常见的JavaScript模块查询有href属性但没有title属性的所有<a>元素
 * 并给它们注册onmouseover事件处理程序
 * 这个事件处理程序使用XMLHttpRequest HEAD请求取得链接资源的详细信息
 * 然后把这些详细信息设置为链接的title属性
 * 这样它们将会在工具提示中显示
 */
whenReady(function() {
    // 是否有机会使用跨域请求？
    var supportCORS = (new XMLHttpRequest()).withCredentials !== undefined;

    // 遍历文档中的所有链接
    var links = document.getElementsByTagName('a');
    for (var i = 0; i < links.length; i++) {
        var link = links[i];
        if (!link.href) continue;
        if (link.title) continue;  // 跳过已经有工具提示的链接

        // 如果是一个跨域链接
        if (link.host !== location.host || link.protocol !== location.protocol) {
            link.title = '站外链接';          // 假设我们不能获取到任何信息
            if (!supportCORS) continue;     // 如果没有CORS支持（Cross-Origin Resourse Sharing，跨域资源共享））
        }

        if (link.addEventListener)
            link.addEventListener('mouseover', mouseoverHandler, false);
        else
            link.attachEvent('onmouseover', mouseoverHandler);
    };

    function mouseoverHandler(e) {
        var link = e.target || e.srcElement;
        var url = link.href;

        var req = new XMLHttpRequest();
        req.open('HEAD', url);  // 仅仅询问头信息
        req.onreadystatechange = function() {
            if (req.readyState !== 4) return;
            if (req.status === 200) {
                var type = req.getResponseHeader('Content-Type');
                var size = req.getResponseHeader('Content-Length');
                var date = req.getResponseHeader('Last-Modified');

                link.title = '类型: ' + type + ' \n' + '大小: ' + size + ' \n' + '时间: ' + date;
            } else {
                if (!link.title)
                    link.title = "Counln' t fetch details:\n" + req.status + ' ' + req.statusText;
            };
        };

        req.send(null);

        if (link.removeEventListener)
            link.removeEventListener('mouseover', mouseoverHandler, false);
        else
            link.detachEvent('onmouseover', mouseoverHandler);
    }
});