const day0 = new Date("01-01-2020");
const dateParser = (day) => new Date( day0.getTime() + parseInt(day)*24000*3600);
const dayParser = (day) => dateParser(day).toUTCString().slice(5,16);
const stepParser = (day) => parseInt(parseInt(day)/2 -1);


