$(function(){
	$('button').click(function(){
		var user = $('#inputUsername').val();
		var pass = $('#inputPassword').val();
		$.ajax({
			url: '//127.0.0.1:5000/trivifree/api/v1/quest/1',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
				alert("success");
				 
				var parsed = JSON.parse(response);
    			alert(parsed.status);
    			alert(parsed.user);
    			document.getElementById('response_message').innerHTML = parsed.user;
				document.getElementById('opt1').innerHTML = parsed.OP1;
				document.getElementById('opt2').innerHTML = "Copernico";
				document.getElementById('opt3').innerHTML = "Kepler";
				
			},
			error: function(error){
				console.log(error);
				alert("error");
			}
		});
	});
});