var Printer = require('node-printer');
var options = {
    media: 'Custom.200x600mm',
    n: 1
};
// Get available printers list
console.log(Printer.list());
 
// Create a new Pinter from available devices
var printer = new Printer('HP_ENVY_Photo_7800_Orya');

var filePath = '/Users/nasz/Documents/tray/sample.pdf';
printer.printFile(filePath, options);
 
