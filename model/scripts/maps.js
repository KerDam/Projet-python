var mymap = $('mapid');
$('document').ready(function(){
    var mapSet = false;
    $("tr").each(function(index){
        var tds = $(this).children("td");
        if(!mapSet){
            mapInit([tds.eq(2).text(),tds.eq(1).text()]);
            mapSet = true;
        }
        addToMap([tds.eq(2).text(),tds.eq(1).text()],tds.eq(0).text());
    });
});
function mapInit(coordonates){
    mymap = L.map('mapid').setView(coordonates, 11);
    L.tileLayer('http://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="http://openstreetmap.org/copyright">OpenStreetMap</a> contributors',
            maxZoom: 18,
            }).addTo(mymap);
}
function addToMap(coordonates, informations){
    var marker = L.marker(coordonates).addTo(mymap);
    marker.bindPopup(informations).openPopup();
}
