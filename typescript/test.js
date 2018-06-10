var t = 1;
var isDone = false;
var list = [1, 2, 3];
var list_2 = [1, 2, 3];
var isOk = 'dsf';
var Color;
(function (Color) {
    Color[Color["Red"] = 0] = "Red";
    Color[Color["Green"] = 1] = "Green";
    Color[Color["Blue"] = 2] = "Blue";
})(Color || (Color = {}));
;
var c = Color.Green;
var notSure = 4;
if (notSure) {
    alert('fd');
}
notSure = 'May Be';
notSure = false;
var list_3 = [1, false, 2, 'fds'];
function warnUser() {
    alert("this is my warning message");
}
var greet = function (name) {
    return "hi " + name;
};
var Character = /** @class */ (function () {
    function Character(firstname, lastname) {
        this.fullname = firstname + "/" + lastname;
    }
    Character.prototype.greet = function (name) {
        return "Hi ! " + name + " " + this.fullname;
    };
    return Character;
}());
var spark = new Character('jacob', 'keyes');
alert(spark.greet());
var Logger = /** @class */ (function () {
    function Logger() {
    }
    Logger.prototype.log = function (arg) {
        alert(arg);
    };
    return Logger;
}());
