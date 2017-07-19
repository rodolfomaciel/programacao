var listaData = function() {
  var l = [];
  return {
     addFirst: function(i){ return l.unshift(i) },
     addLast: function(i){ return l.push(i) },
     addItem: function(index, item){ return l.splice(index, 0, item) },
     removeFirst: function(){ return l.shift() },
     removeLast: function(){ return l.pop() },
     removeItem: function(index){ return l.splice(index, 1) },
     replaceItem: function(index, item){ return l.splice(index, 1, item) },
     firstItem: function(){ return l.slice(0,1) },
     lastItem: function(){ return l.slice(l.length - 1,)},
     theList: function(){ return l.slice() },
     theTail: function(){ return l.slice(1,l.length) },
     theInit: function(){ return l.slice(0,l.length - 1) },
     sizeList: function(){ return l.length }        
 }
}
