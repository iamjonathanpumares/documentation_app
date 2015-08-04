function ajaxDeletePaquete (id, callback) {
	$.ajax({ 
		url: '/api/paquetes/' + id +'/',
		method: 'DELETE'
	})
	.done(function (data) {
		callback(data);
	});
}