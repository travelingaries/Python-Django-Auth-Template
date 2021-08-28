function create_random_pin() {
    let random = Math.floor(Math.random() * 1000000);
    let num_digits = String(random).length;
    let prefix = ''
    if(num_digits < 6) {
        prefix = '0' * (6 - num_digits);
    }
    return prefix + String(random);
}

function validateEmail(email) {
    const reg = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return reg.test(String(email).toLowerCase());
}

function validateName(name) {
    const reg = /^(?![\s-]+$)[가-힣a-zA-Z\s-]{1,150}$/;
    return reg.test(name);
}

function validateNickname(nickname) {
    const reg = /^(?![\s-]+$)[가-힣a-zA-Z0-9\s-]{1,150}$/;
    return reg.test(nickname);
}

function validatePassword(password) {
    const reg = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{6,20}$/;
    return reg.test(password);
}

function validatePhone(phone) {
    const reg = /^[0-9]{10,12}$/;
    return reg.test(phone);
}
