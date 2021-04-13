const string = 'Hi! My name is Olga'

function reverse(string) {
    if (typeof string !== 'string') {
        return 'Restart with a string';
    }
    if (string.length <= 1) {
        return string;
    }
    else {
        const backwords = [];
        const totalItems = string.length - 1;
        for (i=totalItems; i >=0; i--) {
            backwords.push(string[i]);
        }
        return backwords.join('');
    }
}

function reverse2(string) {
    if (typeof string !== 'string') {
        return 'Restart with a string';
    }
    if (string.length <= 1) {
        return string;
    }
    else {
        return string.split('').reverse().join('');
    }
}

const reverse3 = str => [...str].reverse().join('');
reverse3(string)