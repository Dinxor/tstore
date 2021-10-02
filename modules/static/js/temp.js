$(document).ready(function(){ 
// Create a client instance
var clientId  = 'a:myOrgId:'+Math.random().toString(16).substr(2, 8);
client = new Paho.Client ("10.0.0.4", 1884, clientId);

// set callback handlers
client.onConnectionLost = onConnectionLost;
client.onMessageArrived = onMessageArrived;

// connect the client
client.connect({onSuccess:onConnect, 
  userName : "test",
  password : "test"});


// called when the client connects
function onConnect() {
  // Once a connection has been made, make a subscription and send a message.
  console.log("onConnect");
  client.subscribe("oil/#");
}

// called when the client loses its connection
function onConnectionLost(responseObject) {
  if (responseObject.errorCode !== 0) {
    console.log("onConnectionLost:"+responseObject.errorMessage);
  }
}


function onMessageArrived(message) {
  var dest = message.destinationName;
  var mrows = dest.split('/', 4)
  var rowId = '#'+mrows[1]+mrows[2]+mrows[3]; 
//  console.log("onMessageArrived:"+message.destinationName+" id: "+rowId);
  $(rowId).html(message.payloadString); 
  }
});