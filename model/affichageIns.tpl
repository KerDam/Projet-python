<html>
<head>
  <script src="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js"></script>
  <script src="scripts/jquery-1.12.1.min.js"></script>
  <script src="scripts/maps.js"></script>

  <link rel="stylesheet" href="semantic/semantic.css" />
  <link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css" />
</head>
<body>
<div class="ui middle gridequal width center aligned padded grid">
%for ins in installations:
    <div class="olive three wide column">{{ins[0]}}</div>
    <div class="black three wide column">{{ins[1]}}</div>
    <div class="olive three wide column">{{ins[2]}}</div>
    <div class="black three wide column">{{ins[3]}}</div>
    <div class="olive three wide column">{{ins[4]}}</div>
%end
</div>
<div id="mapid" style="height:500px">
</div>
<table style="visibility:hidden">
%for ins in installations:
<tr>
<td>{{ins[0]}}</td>
<td>{{ins[5]}}</td>
<td>{{ins[6]}}</td>
</tr>
%end
</body>
</html>
