function toggleCompleted(element) {
    if (element.classList.contains('content-inprogress')) {
        element.classList.remove('content-inprogress');
        element.classList.add('content-completed');
        element.textContent = "完了";
    } else {
        element.classList.remove('content-completed');
        element.classList.add('content-inprogress');
        element.textContent = "未完";
    }
}