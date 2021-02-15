function toggleCompleted(element) {
    if (element.classList.contains('content-inprogress')) {
        element.classList.remove('content-inprogress');
        element.classList.add('content-completed');
        element.textContent = "Completed";
    } else {
        element.classList.remove('content-completed');
        element.classList.add('content-inprogress');
        element.textContent = "In Progress";
    }
}

$('.status-toggle').click(function(){
    let pk = $(this).attr("data-pk");
    let d = new Date();
    console.log(d.getTimezoneOffset());
    $.ajax({url: '/toggle_completed/'+ pk + '/' + d.getTimezoneOffset(), success: function(result){
        $('#date_completed'+pk).html(result)
    }});
});