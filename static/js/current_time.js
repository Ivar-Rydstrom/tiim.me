
created_time = document.getElementById('created_time');

var update_time = function() {
  current_time = get_current_time_ISO();
  created_time.value = current_time;
  setTimeout('update_time()', 1000)
}()
