// variable from server(we have this part in html):
// let quiz= {{quiz|tojson}}

// Get which radio button is seelected by the user
function get_selected() {
    selected = -1;
    if ($("#option1").is(":checked")) {
        selected = 0;
    }
    if ($("#option2").is(":checked")) {
        selected = 1;
    }
    if ($("#option3").is(":checked")) {
        selected = 2;
    }
    if ($("#option4").is(":checked")) {
        selected = 3;
    }
    return selected;
}
function load_selected(cur_quiz) {
    selected = cur_quiz.selected;
    if (selected != -1) {
        if (selected == 0) {
            $("#option1").attr("checked", true);
        }
        if (selected == 1) {
            $("#option2").attr("checked", true);
        }
        if (selected == 2) {
            $("#option3").attr("checked", true);
        }
        if (selected == 3) {
            $("#option4").attr("checked", true);
        }
    }
}

function post_selected(cur_quiz) {
    selected = -1;
    selected = get_selected();
    cur_quiz.selected = selected;
    // TODO: Post quiz to server
    $.ajax({
        type: "POST",
        url: "/update",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(cur_quiz),
        success: function (item) {
            console.log("success");
        },
        error: function (request, status, error) {
            console.log("Error");
            console.log(request);
            console.log(status);
            console.log(error);
        },
    });
}

function display_wrong_q(data) {
    $.each(data[2], function (index) { 
        var $newCustomer = $( "#wrong-ans-id" ).clone().prop('id', 'klon'+index )
        $newCustomer.find("strong").append(data[2][index])
        $newCustomer.find("mark").append(data[3][index])
        $newCustomer.removeAttr("style");
        $newCustomer.appendTo( ".wrong-ans-container" )
        var $newCustomer = 0
    });
}

$(document).ready(function () {
    if(window.location.pathname.endsWith("quiz/end")) {
        display_wrong_q(result);
        console.log(result[3]);
    }
    // update navbar
    $("#quiz_id").css("background-color", "white").css("border-radius", "5px");

    // update progress bar
    progress = parseFloat(quiz.quiz_id);
    p_str = "" + ((progress * 100) / 9).toFixed(1) + "%";
    console.log(progress);
    let msg = quiz.quiz_id + " of 8";
    $("#progress-bar-id").html(msg);
    $("#progress-bar-id").css("width", p_str);



    // load previous answer
    load_selected(quiz);

    $("#next_button").click(function () {
        post_selected(quiz); // Call post_selected() to update data on server
        if (quiz.next_quiz == "end") {
            
            console.log(quiz.next_quiz);
            window.location.href = "/quiz/end";
            // window.location.href = "/quiz/1"
        } else {
            window.location.href = "/quiz/" + quiz.next_quiz;
        }
    });
    $("#back_button").click(function () {
        post_selected(quiz); // Call post_selected() to update data on server
        if (quiz.quiz_id > 1) {
            window.location.href = "/quiz/" + quiz.prev_quiz;
        } else {
            window.location.href = "/quiz/" + quiz.quiz_id;
        }
    });
});
