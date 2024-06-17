
// Function to pad text
function pad(text) {
    let blockSize = 16;
    let padLength = blockSize - (text.length % blockSize);
    return text + String.fromCharCode(padLength).repeat(padLength);
}

// Function to unpad text
function unpad(text) {
    let padLength = text.charCodeAt(text.length - 1);
    return text.slice(0, -padLength);
}

// AES encryption
function aesEncrypt(text, key) {
    let paddedText = pad(text);
    let keyBytes = CryptoJS.enc.Utf8.parse(key);
    let iv = CryptoJS.lib.WordArray.random(16);
    let encrypted = CryptoJS.AES.encrypt(CryptoJS.enc.Utf8.parse(paddedText), keyBytes, { iv: iv });
    return iv.concat(encrypted.ciphertext).toString(CryptoJS.enc.Base64);
}

// AES decryption
function aesDecrypt(encryptedText, key) {
    let keyBytes = CryptoJS.enc.Utf8.parse(key);
    let data = CryptoJS.enc.Base64.parse(encryptedText);
    let iv = CryptoJS.lib.WordArray.create(data.words.slice(0, 4));
    let ciphertext = CryptoJS.lib.WordArray.create(data.words.slice(4));
    let decrypted = CryptoJS.AES.decrypt({ ciphertext: ciphertext }, keyBytes, { iv: iv });
    let decryptedText = decrypted.toString(CryptoJS.enc.Utf8);
    return unpad(decryptedText);
}

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
