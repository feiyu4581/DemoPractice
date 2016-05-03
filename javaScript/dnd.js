/*
* DnD API相当复杂，且浏览器也不完全兼容
* 这个例子基本正确，但每个浏览器会有一点不同，每个似乎都有自身独有的bug
* 这些代码不会尝试浏览器独有的解决方案
*/
whenReady(function() {
    // 查找所有的<ul class='dnd'>元素，并对其调用dnd()函数
    var lists = document.getElementsByTagName('ul');
    var regexp = /\bdnd\b/;
    for (var i = 0; i < lists.length; i++)
        if (regexp.test(lists[i].className)) dnd(lists[i])

    // 为列表元素添加拖放事件处理程序
    function dnd(list) {
        var original_class = list.className;
        var entered = 0;

        // 当拖放对象首次进入列表时调用这个处理程序
        // 它会检查拖放对象包含的数据格式它是否能处理
        // 如果能，它返回false来表示有兴趣放置
        // 在这种情况下，它会高亮拖放目标，让用户知道该兴趣
        list.ondragenter = function(e) {
            e = e || window.event;
            var from = e.relatedTarget;

            // dragenter和dragleave事件冒泡
            // 它使得在像<ul>元素有<li>子元素的情况下，
            // 何时高亮显示或取消高亮显示元素变得棘手
            // 在定义relatedTarget的浏览器中，我们能跟踪它
            // 否则，我们需要通过统计进入和离开的次数

            // 如果从列表外面进入或第一次进入
            // 那么需要做一些处理
            entered++;
            if ((from && !ischild(from, list)) || entered == 1) {
                // 所有的DnD信息都在dataTransfer对象上
                var dt = e.dataTransfer;

                // dt.types对象列出可用的拖放数据的类型或格式
                // HTML5定义这个对象有contains()方法
                // 在一些浏览器中，它是一个有indexOf()的数组
                // 在IE8已经之前的版本中，它根本不存在
                var types = dt.types; // 可用数据格式是什么

                // 如果没有任何类型的数据或可用数据是纯文本格式，
                // 那么高亮显示列表让用户知道我们正在监听拖放，
                // 同时返回false让浏览器知晓
                if (!types || // IE
                    (types.contains && types.contains('text/plain')) || // HTML5
                    (types.indexOf && types.indexOf('text/plain') != -1)) // Webkit
                {
                    list.className = original_class + ' droppable';
                    return false;
                };

                // 如果我们无法识别数据类型，我们不希望拖放
                return; // 没有取消
            };

            return false;  // 如果不是第一次进入时，我们继续保持兴趣
        };

        // 当鼠标只在悬停在列表上，会调用这个处理程序
        // 我们必须定义这个处理程序并返回false，否则这个拖放操作将取消
        list.ondragover = function(e) { return false; };

        // 当拖放对象移除列表或从其子元素中移除时，会调用这个处理程序
        // 如果我们真正离开这个列表（不是仅仅从一个列表项到另一个），
        // 那么取消高亮显示它
        list.ondragleave = function(e) {
            e = e || window.event;
            var to = e.relatedTarget;

            // 如果我们要到列表以外的元素胡打破离开和进入次数的平衡
            // 那么取消高亮显示元素
            entered--;
            if ((to && !ischild(to, list)) || entered <= 0) {
                list.className = original_class;
                entered = 0;
            }

            return false;
        };

        // 当实际放置时，会调用这个程序
        // 我们会接受放下的文本并将放到一个新的<li>元素中
        list.ondrop = function(e) {
            e = e || window.event;
            // 获得放置的纯文本数据
            // "Text"是"text/plain"的昵称
            // IE不支持"text/plain"，所以在这里使用"Text"
            var dt = e.dataTransfer;  // dataTransfer对象
            var text = dt.getData('Text');  // 获取放置的纯文本数据

            // 如果得到了一个文本，把它放入列表尾部的新项中
            if (text) {
                var item = document.createElement('li');
                item.draggable = true;
                item.appendChild(document.createTextNode(text));
                list.appendChild(item);

                list.className = original_class;
                entered = 0;

                return false;
            }
        };
    };

    // 使原始所有列表项都可以移动
    var items = document.getElementsByTagName('li');
    for (var i = 0; i < items.length; i++) {
        items[i].draggable = true;

        items[i].ondragstart = function(e) {
            var e = e || window.event;
            var target = e.target || e.srcElement;
            // 如果他不是从<li>向上冒泡的，那么忽略它
            if (target.tagName !== 'LI') return false;
            var dt = e.dataTransfer;

            dt.setData('Text', target.innerText || target.textContent);
            dt.effectAllowed = 'copyMove';
        };

        // 当放置成功后，将调用这个程序
        items[i].ondragend = function(e) {
            e = e || window.event;
            var target = e.target || e.srcElement;

            // 这个这个拖放操作是move，那么要删除列表项
            // 在IE8中，他将是"none"，除非在之前的ondrop处理程序中显示设置他为move
            // 但为IE强制设置"none"会阻止其他浏览器给用户选择复制还是移动的机会
            if (e.dataTransfer.dropEffect === 'move')
                target.parentNode.removeChild(target);
        };
    }

    // 这时在ondragenter和ondragleave使用的工具函数
    // 如果a是b的子元素则返回true
    function ischild(a, b) {
        for (; a; a = a.parentNode) if (a === b) return true;
        return false;
    };
});