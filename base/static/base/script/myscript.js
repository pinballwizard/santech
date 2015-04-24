$(document).ready(function() {
    $(function () {
        $('#myTab a:first').tab('show');
    });
    $("#myNavbar").find("li").not(".dropdown").children("a").click(function(){
        $(".nav").find("li").removeClass("active");
        $(this).parent().addClass("active");
        $(this).parents(".dropdown").addClass("active");
    });
    var afterClick =  $("#myNavbar").find("a").filter(function(){
        return $(this).attr("href") == window.location.pathname;
    });
    afterClick.parent().addClass("active");
    afterClick.parents(".dropdown").addClass("active");

    $(".modalImage").click(function(){
        console.log("hello")
        $(this).siblings(".myModal").modal('show')
    })

    yandex_map();
//    google_map();
});

function yandex_map(){
    var longitude = $('#map').data('longitude');
    var latitude = $('#map').data('latitude');
    var coordinate = [longitude, latitude];
    ymaps.ready(init);
    var myMap, myPlacemark;
    function init(){
        myMap = new ymaps.Map("map", {
            center: coordinate,
            zoom: 12
        });
        myPlacemark = new ymaps.Placemark(coordinate);
        myMap.geoObjects.add(myPlacemark);
    }
}

//function google_map() {
//    var apiKey = 'AIzaSyDkTrVxNe0ZMrZ0FBNGtO8n0MEyrpB07vI';
//    var mapOptions = {
//        center: new google.maps.LatLng(56.00394079, 92.85553912),
//        zoom: 8,
//        mapTypeId: google.maps.MapTypeId.TERRAIN
//    };
//    map = new google.maps.Map(document.getElementById("map"), mapOptions);
//}