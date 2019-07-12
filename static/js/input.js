
var title = document.getElementById('title');

title.onfocus = function() {
  if (title.value == 'Event Name') {
    title.value = '';
  }
}

title.onblur = function() {
  if (title.value == '') {
    title.value = 'Event Name';
  }
}


var description = document.getElementById('description');

description.onfocus = function() {
  if (description.value == 'Description') {
    description.value = '';
  }
}

description.onblur = function() {
  if (description.value == '') {
    description.value = 'Description';
  }
}


var end_time = document.getElementById('end_time');


var today = new Date();
var second = String(0);
var minute = String(today.getMinutes()).padStart(2, '0');
var hour = String(today.getHours()).padStart(2, '0');
var day = String(today.getDate()).padStart(2,'0');
var month = String(today.getMonth() + 1).padStart(2, '0');
var year = String(today.getFullYear());
today_string = year + '-' + month + '-' + day + 'T' + hour + ':' + minute;
end_time.value = today_string;
