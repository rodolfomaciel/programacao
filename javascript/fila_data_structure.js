var filaData = function(){
    var l = [];
    return {
        addLast: function(i){ return l.push(i) },
        removeFirst: function(){ return l.shift() },
        theList: function(){ return l.slice() },
        sizeList: function(){ return l.length },
    }
}
