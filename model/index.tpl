<html>
<form action='/result' method="post">
<select name="activite">
	%for activite in activites:
	<option value="{{activite[0]}}">{{activite[1]}}</option>
	%end
</select>
<tr/>
<select name="ville">
	%for ville in villes:
	<option value="{{ville[0]}}">{{ville[1]}}</option>
	%end
</select>
</form>
</html>
