var pilhaData = function(){
    var l = [];
    return {
       theList: function(){ return l.slice() },
       sizeList: function(){ return l.length },
       addLast: function(i){ return l.push(i) },
       removeLast: function(){ return l.pop() }
    }
}
