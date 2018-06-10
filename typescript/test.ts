
const t: number = 1;

const isDone: boolean = false;

const list: number[] = [1, 2, 3]
const list_2: Array<number> = [1, 2, 3];

const isOk: boolean | string = 'dsf';

enum Color {Red, Green, Blue};

var c: Color = Color.Green;


var notSure: any = 4;

if (notSure) {
    alert('fd')
}
notSure = 'May Be';
notSure = false;

var list_3: Array<any> = [1, false, 2, 'fds']

function warnUser(): void {
    alert("this is my warning message");
}

var greet: (name: string) => string = function(name: string): string {
    return "hi " + name;
}


class Character {
    fullname: string;
    constructor (firstname: string, lastname: string) {
        this.fullname = `${firstname}/${lastname}`;
    }
    greet(name?: string) {
        return `Hi ! ${name} ${this.fullname}`
    }
}

var spark = new Character('jacob', 'keyes');
alert(spark.greet());

interface LoggerInterface {
    log(arg: boolean): void;
}

class Logger implements LoggerInterface {
    log(arg: string) {
        alert(arg);
    }
}