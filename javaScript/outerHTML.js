

// 为那些不支持它的浏览器实现outerHTML属性
// 假设浏览器确实支持innerHTML，并有个可扩展的Element.prototype
// 并且可以定义getter和setter

(function() {
    // 如果outerHTML存在，则直接返回
    if (document.createElement('div').outerHTML) return;

    // 返回this所引用元素的外部HTML
    function outerHTMLGetter() {
        var container = document.createElement('div');  // 虚拟元素
        container.appendChild(this.cloneNode(true));    // 复制到该虚拟节点
        return container.innerHTML;                     // 返回该虚拟节点的innerHTML
    }

    // 用指定的值设置元素的外部HTML
    function outerHTMLSetter(value) {
        // 创建一个虚拟元素，设置其内容为指定的值
        var container = document.createElement('div');
        container.innerHTML = value;
        // 将虚拟元素中的节点全部移动到文档中
        while (container.firstChild)  // 循环，知道container没有子节点为止
            this.parentNode.insertBefore(container.firstChild, this);

        // 删除所被取代的节点
        this.parentNode.removeChild(this);
    }

    // 现在使用这两个函数作为所有Element对象的outerHTML属性的getter和setter
    // 如果它存在则使用ES5的Object.defineProperty()方法
    // 否则，退而求其次，使用__defineGetter__()和__defineSetter__()
    if (Object.defineProperty) {
        Object.defineProperty(Element.prototype, 'outerHTML', {
            get: outerHTMLGetter,
            set: outerHTMLSetter,
            enumerable: false, configurable: true
        });
    } else {
        Element.__defineGetter__('outerHTML', outerHTMLGetter);
        ELement.__defineSetter__('outerHTML', outerHTMLSetter);
    }

}());
