<html>
<<<<<<< HEAD
<table>
	%for result in results:
<tr>
	<td>{{result[0]}}</td>
	<td>{{result[1]}}</td>
	<td>{{result[2]}}</td>
	<td>{{result[3]}}</td>
	<td>{{result[4]}}</td>
</tr>
	%end
</table>
</html>
=======


    <head> <!--https://openclassrooms.com/courses/google-maps-javascript-api-v3-->

        <title>Résultat</title>
        <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />

        <!-- Elément Google Maps indiquant que la carte doit être affiché en plein écran et
        qu'elle ne peut pas être redimensionnée par l'utilisateur -->
        <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />

        <!-- Inclusion de l'API Google MAPS -->
        <!-- Le paramètre "sensor" indique si cette application utilise détecteur pour déterminer la position de l'utilisateur -->
        <script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=false"></script>

        <script type="text/javascript">

            function initialiser(longitudes, latitudes) {

                var latlng = new google.maps.LatLng(47.4117977, -1.9425131);

                //objet contenant des propriétés avec des identificateurs prédéfinis dans Google Maps permettant
                //de définir des options d'affichage de notre carte

                var options = {
                    center: latlng,
                    zoom: 7,
                    mapTypeId: google.maps.MapTypeId.ROADMAP
                };            

                //constructeur de la carte qui prend en paramêtre le conteneur HTML
                //dans lequel la carte doit s'afficher et les options
                var carte = new google.maps.Map(document.getElementById("carte"), options)          
                

                for(i=0; i<longitudes.length; i++) {
                    var marqueur = new google.maps.Marker({
    	        		position: new google.maps.LatLng(longitudes[i], latitudes[i]),
    	        		map: carte
        			});
                }
            }

        </script>

    </head>


    <body>

        <p> Bonjour est-ce que ça maaaaaarche ? </p>

        %longitudes, latitudes = [], []
    	%for installation in installations :
            %longitudes.append(float(installation[4]))
            %latitudes.append(float(installation[5]))
        <script> initialiser({{longitudes}}, {{latitudes}}); </script>

        <div id="carte" style="width:50%; height:50%"></div>

    </body>

</html>
>>>>>>> ee46ef855b23dbd4ddbb1a691ee2ffb78c667077
