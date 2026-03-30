// (function(window) {
//   window["env"] = window["env"] || {};
  
//   _location = window.location.protocol + "//" + window.location.hostname + ":" + window.location.port
  
//   // Environment variables
//   window["env"]["debug"] = "${DEBUG}";
//   window["env"]["backUrl"] = "${BACKEND_URL}" || _location;
//   window["env"]["apiUrl"] = "${BACKEND_URL}/backend";
//   window["env"]["chronoUrl"] = "${BACKEND_URL}/chrono";
// })(this);

(function(window) {
  window["env"] = window["env"] || {};
  
  var _location = "${BACKEND_URL}"; 

  window["env"]["debug"] = false;
  window["env"]["backUrl"] = _location;
  window["env"]["apiUrl"] = _location + "/backend";
  window["env"]["chronoUrl"] = "http://localhost:5002"; 
})(this);