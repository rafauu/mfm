function send(){
    $.ajax({
        type: "get",
        url: "127.0.0.1",
        success:function(data)
        {
            console.log(data);

            setTimeout(function(){
                send();
            }, 1000);
        }
    });
}
send();
