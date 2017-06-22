var client = require('./connection.js');
var inputfile = require('./input/qa.json');
var bulk = [];

var makebulk = function(qalist,callback){
  var action = { index: {
    _index: 'tbc',
    _type: 'qa' }
  };
  for (var i in qalist){
    var a = qalist[i];
    bulk.push( action, a );
  }
  callback(bulk);
}

var indexall = function(madebulk,callback) {
  client.bulk({
    index: 'tbc',
    type: 'qa',
    body: madebulk
  },function(err,resp,status) {
      if (err) {
        console.log(err);
      }
      else {
        callback(resp.items);
      }
  })
}

makebulk(inputfile,function(response){
  console.log('Bulk content prepared');
  indexall(response,function(response){
    console.log(response);
  })
});
