/* Author: 

*/
var node = new Backbone.Model({
    name: "Node1"
});

$(document).ready(function(){
    setInterval ( "doSomething()", 100 );

    $.get("/nodes",
        function(data){
            $(data).each(function(i, item){
                var newnode = document.createElementNS('http://www.w3.org/2000/svg', "image");
                newnode.setAttribute("id", "node-" + item.pk );
                newnode.setAttribute("x", item.fields.posx);
                newnode.setAttribute("y", item.fields.posy);
                newnode.setAttribute("width", 80);
                newnode.setAttribute("height", 80);
                newnode.setAttribute("opacity", 0.5);
                newnode.setAttributeNS("http://www.w3.org/1999/xlink","href", "/static/svg/" + item.fields.nodetype + ".svg");

                if (item.fields.enabled) {
                    newnode.setAttribute("opacity", 1);
                }


                $("svg").append(newnode);
            });
            
            $("svg image").click(function(){
                $.fancybox(
                    '<h2>Hi!</h2><p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam quis mi eu elit tempor facilisis id et neque<a href="ssh://127.0.0.1">Connect</a></p>',
                    {
                    'autoDimensions'    : false,
                    'width'             : 500,
                    'height'            : 'auto',
                    'transitionIn'      : 'swing',
                    'transitionOut'     : 'none'
                    }
                );
            });
        }
    , "json");
    
});

function doSomething ( ) {
    var value = parseInt($("svg path").css('stroke-dashoffset'), 10);

    value = (value + 1) % 14;

    $("svg path").css('stroke-dashoffset', value + 'px');
}
    

