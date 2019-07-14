// Store default values for parametric updating
var default_event = 'Event Name';
var default_description = 'Event Description';


// Returns current String time in ISO format
var get_current_time_ISO = function() {
  var today = new Date();
  var second = String(0);
  var minute = String(today.getMinutes()).padStart(2, '0');
  var hour = String(today.getHours()).padStart(2, '0');
  var day = String(today.getDate()).padStart(2,'0');
  var month = String(today.getMonth() + 1).padStart(2, '0');
  var year = String(today.getFullYear());
  today_string = year + '-' + month + '-' + day + 'T' + hour + ':' + minute;
  return today_string;
}


// enforce minimum date settable through form
var datetime = document.getElementById('end_time');
datetime.min = get_current_time_ISO();
