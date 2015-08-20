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
		$data.text(i);

	}
}

function getNoFilasTabla(id_tabla)
{
	var no_filas = $('#' + id_tabla).children('tr').length;

	return no_filas;
}

function deleteElement(id_container, id_form, id_modal)
{
	var options = {
	  dataType: 'json',
	  success: function(response)
	  {
	    if(response.status=="True"){
	      alert("Eliminado!");
	      var id = response.id;
	      var no_elementos= $('#' + id_container).children('div').length;

	      if(no_elementos==1) 
	      {
	        location.reload();
	      }
	      else 
	      {
	        $('#div' + id).remove();
	        $('#' + id_modal).modal('hide');
	      }
	    }
	    else
	    {
	      alert("Hubo un error al eliminar!");
	      $('#' + id_modal).modal('hide');
	    }
	  }
	};
	
	$('#' + id_form).ajaxForm(options);
}

function ajaxCreateObject(url, datos, callback)
{
	$.ajax({
		url: url,
		type: 'POST',
		dataType: 'json',
		data: datos
	})
	.done(function (data) {
		callback(null, data);
	})
	.fail(function (xhr, status, error) {
		callback(xhr, null);
	});
}

function ajaxUpdateObject(url, datos, callback)
{
	$.ajax({
		headers: {
		        'X-HTTP-Method-Override': 'PUT'
		},
		url: url,
		type: 'POST',
		dataType: 'json',
		data: datos
	})
	.done(function (data) {
		callback(null, data);
	})
	.fail(function (xhr, status, error) {
		callback(xhr, null);
	});
}

function ajaxDeleteObject(url, datos, callback)
{
	$.ajax({
		headers: {
		        'X-HTTP-Method-Override': 'DELETE'
		},
		url: url,
		type: 'POST',
		//dataType: 'json',
		data: datos
	})
	.done(function (data) {
		callback(null, data);
	})
	.fail(function (xhr, status, error) {
		callback(xhr, null);
	});
}