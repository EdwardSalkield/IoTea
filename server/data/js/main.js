var requesturl = "/"

function submitValues(temp, time) {
    //alert(temp + " " + time);
    request("enqueue", {temp: temp, time: time, mode: "brew"}, function(r){
        //alert(":O");
    });
    return false;
}

function rinse() {
    request("enqueue", {temp: 0, time: 0, mode: "rinse"}, function(r){
        //alert(":D");
    });
}

function request(func, data, _callback) {
    var r;
    var error;
    var url = requesturl + func;
    $.post(url, data, function(ret, status, xhr){
        if (status == "success") {
            r = ret;
            console.log(r);
            if (r.success == true) { //to make sure callback is always called if leaving/ending
                _callback(r);
            }
            else {
                alert(r.error);
            }
        }
        else {
            //error
        }
    }, "json");
}
function messagebar(error) {
    var messagebar = "<div class='alert alert-success alert-dismissable fade in'> <a href='#' class='close' data-dismiss='alert' aria-label='close'>&times;</a><strong>%s</strong> %s</div>";
    var eb = $(sprintf(errorbar, "Info", error));
    $("#alerts").append(eb);
    setTimeout(function() {
        eb.remove();
    }, 5000);
}

