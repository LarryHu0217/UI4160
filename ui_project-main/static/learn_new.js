function displayNames(data) {
    for (const [key, value] of Object.entries(data)) {
        console.log(key, value);
        $("#people_container").append($("<div>").append("page " + value));
    }
}

function get_and_save_name() {
    let name = lesson.lesson_id + ": " + $("#new_name").val();
    let data_to_save = { name: name };
    $.ajax({
        type: "POST",
        url: "add_name",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(data_to_save),
        success: function (result) {
            let all_data = result["data"];
            console.log(all_data);
            data = all_data;
            // displayNames(data)
            if (lesson.next_lesson == "end") {
                displayNames(data);
            }
            $("#new_name").val("");
        },
        error: function (request, status, error) {
            console.log("Error");
            console.log(request);
            console.log(status);
            console.log(error);
        },
    });
}
$(document).ready(function () {
    $("#learn_id").css("background-color", "white").css("border-radius", "5px");
    progress = parseFloat(lesson.lesson_id);
    len = "" + ((progress * 100) / 8).toFixed(1) + "%";
    p_str = progress + " of 8";
    console.log(progress);
    $("#bar").html(p_str);
    $("#bar").css("width", len);

    // load text into learning page
    $("#text-learn-id").html(lesson.text);

    if (lesson.next_lesson == "end") {
        get_and_save_name();
    }

    $("#submit_name").click(function () {
        get_and_save_name();
    });

    $("#next_button").click(function () {
        if (lesson.next_lesson == "end") {
            console.log(lesson.next_lesson);
            // window.location.href = "/"
            window.location.href = "/quiz/1";
        } else if (lesson.next_lesson == "7") {
            window.location.href = "/learn/i6";
        } else {
            window.location.href = "/learn/" + lesson.next_lesson;
        }
    });
    $("#back_button").click(function () {
        if ((lesson.lesson_id > 1) & (lesson.prev_lesson != "7")) {
            window.location.href = "/learn/" + lesson.prev_lesson;
        } else if (lesson.prev_lesson == "7") {
            window.location.href = "/learn/i6";
        } else {
            window.location.href = "/learn/" + lesson.lesson_id;
        }
    });
});
