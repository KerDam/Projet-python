<html>
<form action='/result' method="post">
<select name="activite">
	%for activite in activites:
	<option value="{{activite}}">{{activite}}</option>
	%end
</select>
<tr/>
<select name="activite">
	%for ville in villes:
	<option value="{{ville}}">{{ville}}</option>
	%end
</select>
</form>
</html>
