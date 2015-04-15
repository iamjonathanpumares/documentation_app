$('.delete').on('click', function (e) {
	e.preventDefault();
	var Pid = $(this).attr('id');
	var name = $(this).data('name');
	$('#modal_id_proyecto').val(Pid);
	$('#js-spanNameProject').text(name);
});

var options = {
	dataType: 'json',
	success: function(response)
	{
	  if(response.action == "Eliminar")
	  {
	    if(response.status=="True"){
	      alert("Eliminado!");
	      var idProy = response.proyecto_id;
	      var elementos= $('#js-rowProject > div').length;
	      if(elementos==1) 
	      {
	        location.reload();
	      }

	      else 
	      {
	        $('#div'+idProy).remove();
	        $('#myModal').modal('hide');
	      }

	    }

	    else
	    {
	      alert("Hubo un error al eliminar!");
	      $(nombre_ventana_modal).modal('hide');
	    }
	  }
	  
	}
};

$('#js-frmEliminar').ajaxForm(options);