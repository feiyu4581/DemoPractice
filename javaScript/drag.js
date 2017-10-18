/**
 * Drag.js 拖动绝对定位的HTML元素
 * 这个模块定义了一个drag()函数，它用于mousedown事件处理程序的调用
 * 随后的mousemove事件将移动指定元素，mouseup事件将终止拖动
 * 这些实现能同标准和IE两种事件模型一起工作
 * 参数：
 * elementToDrag：接收mousedown事件的元素或某些包含元素
 * 它必须是绝对定位的元素
 * 它的style.left和style.top值讲随着用户的拖动而改变
 *
 * event: mousedown事件对象
 **/

// 以一个对象的x和y属性的方式返回滚动条的偏移量
function getScrollOffsets(w) {
    // 只用指定的窗口，如果不带参数则使用当前窗口
    w = w || window;

    // 除了IE8及更早的版本以外，其他浏览器都可以使用
    if (w.pageXOffset != null) return {x: w.pageXOffset, y: w.pageYOffset};
    // 对标准模式下的IE（或任何其他浏览器）
    var d = window.document;
    if (document.compatMode == 'CSS1Compat')
        return { w: d.documentElement.scrollLeft, h: d.documentElement.scrollTop };

    // 对怪异模式下的浏览器
    return { x: d.body.scrollLeft, y: d.body.scrollTop };
}

function drag(elementToDrag, event) {
    var scroll = getScrollOffsets();
    var startX = event.clientX + scroll.x;
    var startY = event.clientY + scroll.y;

    // 在文档坐标下，待拖动元素的初始位置
    // 因为elementToDrag是绝对定位
    // 所以我们可以假设它的offsetParent就是文档的body元素
    var origX = elementToDrag.offsetLeft;
    var origY = elementToDrag.offsetTop;

    // 计算mousedown事件和元素左上角之间的距离
    // 我们将它另存为鼠标移动的距离
    var deltaX = startX - origX;
    var delatY = startY - origY;

    // 注册用于响应接着mousedown事件发生的mousemove和mouseup事件的事件处理程序
    if (document.addEventListener) {  // 标准事件模型
        // 在document对象上注册捕获事件处理程序
        document.addEventListener('mousemove', mouveHandler, true);
        document.addEventListener('mouveup', upHandler, true);
    }
    else if (document.attachEvent) {  // 用于IE5~8的IE事件模型
        // 在IE事件模型中
        // 捕获事件是通过调用元素上的setCapture()捕获它们
        elementToDrag.setCapture();
        elementToDrag.attachEvent('onmousemove', moveHanlder);
        elementToDrag.attachEvent('onmouseup', upHandler);
        // 作为mouseup事件看待鼠标捕获的丢失
        elementToDrag.attachEvent('onlosecapture', upHandler);
    }

    // 我们处理了这个事件，不让任何其他元素看到它
    if (event.stopPropagation) event.stopPropagation();  // 标准模型
    else event.cancelBubble = true;                      // IE

    // 现在组织任何默认操作
    if (event.preventDefault) event.preventDefault();    // 标准模型
    else event.returnValue = false;                      // IE

    /**
     * 当元素正在被拖动时，这就是捕获mousemove事件的处理程序
     * 它用于移动这个元素
    **/
    function moveHanlder(e) {
        if (!e) e = window.event;  // IE事件模型

        // 通过这个元素到当前鼠标位置
        // 通过滚动条的位置和初始单击的偏移量来调整
        var scroll = getScrollOffsets();
        elementToDrag.style.left = (e.clientX + scroll.x - deltaX) + 'px';
        elementToDrag.style.top = (e.clientY + scroll.y - deltaY) + 'px';
        //同时不让任何其他元素看到这个事件
        if (e.stopPropagation) e.stopPropagation();  // 标准
        else e.cancelBubble = true;                  // IE
    }

    /**
     * 这是一个在拖动结束时发生的最终mouseup事件的处理程序
     **/
    function upHandler(e) {
        if (!e) e = window.event;  // IE事件模型

        // 注销捕获事件
        if (document.removeEventListener) {  // DOM事件模型
            document.removeEventListener('mouseup', upHandler, true);
            document.removeEventListener('mousemove', moveHanlder, true);
        } else if (document.attachEvent)  {// IE5+ 事件模型
            elementToDrag.detachEvent('onlosecapture', upHandler);
            elementToDrag.detachEvent('onmouseup', upHandler);
            elementToDrag.detachEvent('onmousemove', moveHanlder);
            elementToDrag.releaseCapture();
        }

        // 并且不让事件进一步传播
        if (e.stopPropagation) e.stopPropagation();  // 标准模型
        else e.cancelBubble = true;                  // IE模型
    }
}

<!-- 要拖动的元素 -->
<div style='position:absolute; left:100px; top:100px; width:250px; background-color: white; border: solid black'>
    <div style='background-color:gray; border-bottom: dotted black; padding: 3px; font-weight: bold;' onmousedown='drag(this.parentNode, event);'>
        拖动我
    </div>
</div>