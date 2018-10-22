var args = process.argv.slice(2);

const CONFIG = require('./JS/config/Settings');
const CalendarAPI = require('node-google-calendar');
let cal = new CalendarAPI(CONFIG);



cal.CalendarList.list({})
    .then(resp => {
        console.log(resp);
    }).catch(err => {
    console.log(err.message);
});

// return;

let params = {
    timeMin: '2018-05-20T06:00:00+08:00',
    timeMax: '2018-06-25T22:00:00+08:00',
    singleEvents: true,
    orderBy: 'startTime'
}; 	//Optional query parameters referencing google APIs

cal.Events.list("primary", params)
    .then(json => {
        //Success
        console.log('List of events on calendar within time-range:');
        console.log(json);
    }).catch(err => {
    //Error
    console.log('Error: listSingleEvents -' + err.message);
});
