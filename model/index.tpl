<html>
<form action='/result' method="post">
<select name="activite">
	%for activite in activites:
	<option value="{{activite[1]}}">{{activite[0]}}</option>
	%end
</select>
<select name="ville">
	%for ville in villes:
	<option value="{{ville[0]}}">{{ville[1]}}</option>
	%end
</select>
<input type="submit" name="valide" value="Chercher">
</form>
</html>
