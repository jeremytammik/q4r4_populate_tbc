var client = require('./connection.js');
var inputfile = require('./qa.json');
var bulk = [];

var makebulk = function(qalist,callback){
  for (var current in qalist){
    bulk.push(
      { index: {_index: 'tbc', _type: 'qa' } },
      current );
  }
  callback(bulk);
}

var indexall = function(madebulk,callback) {
  client.bulk({
    maxRetries: 5,
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
