$(document).ready(function() {
    $(function () {
        $('#myTab a:first').tab('show');
    });
    var nav = $("#myNavbar");
    nav.find("li").not(".dropdown").children("a").click(function(){
        $(".nav").find("li").removeClass("active");
        $(this).parent().addClass("active");
        $(this).parents(".dropdown").addClass("active");
    });
    var afterClick =  nav.find("a").filter(function(){
        return $(this).attr("href") == window.location.pathname;
    });
    afterClick.parent().addClass("active");
    afterClick.parents(".dropdown").addClass("active");

    $('.modalButton').click(function(){
        $(this).siblings('.myModal').modal('show')
    });
    $('.editable').click(function(){

    });

    yandex_map();
//    google_map();
});

function yandex_map(){
    var map_obj = $('#map');
    var coordinate = [map_obj.data('longitude'), map_obj.data('latitude')];
    var maptype = map_obj.data('maptype');
    ymaps.ready(init);
    var myMap;
    var placemark;

    function init(){
        myMap = new ymaps.Map("map", {
            center: coordinate,
            zoom: 12,
            type: maptype
        });
        placemark = new ymaps.Placemark(coordinate);
        myMap.geoObjects.add(placemark);
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