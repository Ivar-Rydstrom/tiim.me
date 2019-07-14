
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
  if (description.value == 'Event Description') {
    description.value = '';
  }
}

description.onblur = function() {
  if (description.value == '') {
    description.value = 'Event Description';
  }
}


var end_time = document.getElementById('end_time');
end_time.value = get_current_time_ISO();
