function caesarCipherEncrypt(text, shift) {
    let encryptedText = '';
    for (let i = 0; i < text.length; i++) {
        let char = text[i];
        if (char.match(/[a-z]/i)) {
            let code = text.charCodeAt(i);
            if (code >= 65 && code <= 90) {
                char = String.fromCharCode(((code - 65 + shift) % 26) + 65);
            } else if (code >= 97 && code <= 122) {
                char = String.fromCharCode(((code - 97 + shift) % 26) + 97);
            }
        }
        encryptedText += char;
    }
    return encryptedText;
}

// Example usage
let text = "Hello, World!";
let shift = 3;
let encryptedText = caesarCipherEncrypt(text, shift);
console.log("Encrypted text:", encryptedText);

function xorEncryptDecrypt(text, key) {
    let encryptedText = '';
    for (let i = 0; i < text.length; i++) {
        encryptedText += String.fromCharCode(text.charCodeAt(i) ^ key.charCodeAt(i % key.length));
    }
    return encryptedText;
}

// Example usage
let text = "Hello, World!";
let key = "mysecretkey";
let encryptedText = xorEncryptDecrypt(text, key);
console.log("Encrypted text:", encryptedText);

// To decrypt, simply apply the same function again
let decryptedText = xorEncryptDecrypt(encryptedText, key);
console.log("Decrypted text:", decryptedText); 
