var client = require('./connection.js');

client.indices.delete({index: 'tbc'},function(err,resp,status) {  
  console.log("delete",resp);
});
