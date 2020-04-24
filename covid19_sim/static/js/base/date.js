const today = new Date();
const dateParser = (day) => new Date( today.getTime() + parseInt(day)*24000*3600);
const dayParser = (day) => dateParser(day).toUTCString().slice(5,16);
const stepParser = (day) => parseInt(parseInt(day)/2 -1);


