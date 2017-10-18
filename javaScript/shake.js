

// 将e转为为相对定位的元素，使之左右“振动”
// 第一个参数可以是元素对象或者元素的id
// 如果第二个参数是函数，以e为参数，它将在动画结束时调用
// 第三个参数指定e震动的距离，默认是5像素
// 第四个参数指定震动多久，默认是500毫秒

function shake(e, oncomplete, distance, time) {
    // 句柄函数
    if (typeof e === 'string') e = document.getElementById(e);

    if (!time) time = 500;
    if (!distance) distance = 5;

    var originalStyle = e.style.cssText;         // 保存e的原始style
    e.style.position = 'relative';               // 使e相对定位
    var start = (new Date()).getTime();          // 注意，动画的开始时间
    animate();                                   // 动画开始

    // 函数检查消耗的时间，并更新e的位置
    // 如果动画完成，它将e还原为原始状态
    // 否则，它更新e的位置，安排它自身重新运行
    function animate() {
        var now = (new Date()).getTime();        // 得到当前时间
        var elapsed = now - start;               // 从开始依赖消耗了多长时间？
        var fraction = elapsed / time;           // 是总时间的几分之几?

        if (fraction < 1) {
            var x = distance * Math.sin(fraction*4*Math.PI);
            console.log(x)
            e.style.left = x + 'px';

            // 在25毫秒后或在总时间的最后尝试再次运行函数
            // 目的是为了产生每秒40帧的动画
            setTimeout(animate, Math.min(25, time - elapsed));
        }
        else {
            e.style.cssText = originalStyle;        // 恢复原始样式
            if (oncomplete) oncomplete(e);          // 调用完成后的回调函数
        }
    }
}
