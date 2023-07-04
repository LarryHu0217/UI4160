$(document).ready(function () {
    $("#learn_id").css("color", "red").css("font-weight", "bold");

    $("#next_button").click(function () {
        // if (lesson.next_lesson == "end") {
        //     console.log(lesson.next_lesson)
        //     // window.location.href = "/"
        //     window.location.href = "/quiz/1"
        // }
        // else if (lesson.next_lesson=="7"){
        //      window.location.href = "/learn/n7"
        //
        // }
        // else {
        //     window.location.href = "/learn/"+lesson.next_lesson
        // }
        window.location.href = "/learn/8";
    });
    $("#back_button").click(function () {
        window.location.href = "/learn/6";
    });
});
