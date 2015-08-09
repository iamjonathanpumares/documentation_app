function ajaxDeletePaquete (id, callback) {
	$.ajax({ 
		url: '/api/paquetes/' + id +'/',
		method: 'DELETE'
	})
	.done(function (data) {
		callback(data);
	});
}

function ajaxListPaquete (callback) {
	$.ajax({ 
		url: '/api/proyectos/',
		method: 'GET'
	})
	.done(function (data) {
		callback(data);
	});
}

function enumerarTabla(id_tabla)
{
	var $filas = $('#' + id_tabla).children('tr');

	for (var i = 0; i < $filas.length; i++)
	{
		var id_row = $filas[i].id;
		var $data = $('#' + id_row + ' td:first-child');
		$data.text(i + 1);

	}
}

function getNoFilasTabla(id_tabla)
{
	var no_filas = $('#' + id_tabla).children('tr').length;

	return no_filas;
}