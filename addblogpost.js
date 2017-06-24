var client = require('./connection.js');
var inputfile = require('./bulk/blogpost.json');

var handleError = function(err) {  
  if(!err) return false;
  console.log(err);
  return true;
};

var indexall = function(blogpostlist,callback){
  console.log('Items left to index: '+(blogpostlist.length/2));
  segment = blogpostlist.splice(0,500);
  if (segment.length){
    bulkindex(segment,function(response){
      indexall(blogpostlist,callback);
      callback(response);
    })
  }
  else {
    callback('No more blog posts to index');
  }
}

var bulkindex = function(segment,callback){  
  client.bulk({
    index: 'tbc',
    type: 'blogpost',
    body: segment
  },function(err,resp){
    if (err) {
      console.log(err);
      callback(err);
    }
    else {
      console.log('Items',resp.items.length);
      setTimeout(function() { callback('Indexed '+resp.items.length+' items'); }, 2000);
    }
  })
}

indexall(inputfile,function(response){  
  console.log(response);
});
