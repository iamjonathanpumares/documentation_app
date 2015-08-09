function ajaxUpdateActor(id, callback)
{
	$.ajax({
		url: '/api/actores/' + id + '/',
		type: 'GET',
		dataType: 'json',
		error: function (xhr, status, error) {
			console.log(xhr.responseJSON);
			console.log(error);
		}
	})
	.done(function (data) {
		callback(data);
	});
}

function ajaxCreateTarea(data, callback)
{
	$.ajax({
		url: '/api/tareas/',
		type: 'POST',
		dataType: 'json',
		data: data
	})
	.done(function (data) {
		callback(null, data);
	})
	.fail(function (xhr, status, error) {
		callback(xhr, null);
	});
}