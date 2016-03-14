<html>
<form action='/result' method="post">
<select name="activite">
	%for activite in activites:
<<<<<<< HEAD
	<option value="{{activite[1]}}">{{activite[0]}}</option>
	%end
</select>
<tr/>
<select name="ville">
	%for ville in villes:
	<option value="{{ville[0]}}">{{ville[0]}}</option>
	%end
</select>
<input type="submit" value="submit"/>
=======
	<option value="{{activite[0]}}">{{activite[1]}}</option>
	%end
</select>
&nbsp;
<select name="ville">
	%for ville in villes:
	<option value="{{ville[0]}}">{{ville[1]}}</option>
	%end
</select>
&nbsp;
<input type="submit" name="valide" value="Chercher">
>>>>>>> ee46ef855b23dbd4ddbb1a691ee2ffb78c667077
</form>
</html>
