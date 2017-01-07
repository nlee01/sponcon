$(document).ready(function() {
    setTimeout(function() { $("#loading").fadeOut("slow"); }, 1000);
    setTimeout(function() {
        $(".intro-lead-in").fadeTo(1000, 1);
    }, 1500);
    setTimeout(function() {
        $("#intro-buttons").fadeTo(1000, 1);
    }, 2000);
});