$(document).ready(function(){
	
	
	$('#boton_registrar').on("click", function(){
		$.notify({
	
			message: 'El registro se ha completado con éxito' 
			},{
			
			type: 'success',
			placement: {
				from: "bottom",
				align: "right"
			},
		});
	})

	$('#datepicker').datepicker();
	$.datepicker.regional['es'] = {
	closeText: "Cerrar",
	prevText: "&#x3C;Ant",
	nextText: "Sig&#x3E;",
	currentText: "Hoy",
	monthNames: [ "Enero","Febrero","Marzo","Abril","Mayo","Junio",
	"Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre" ],
	monthNamesShort: [ "Ene","Feb","Mar","Abr","May","Jun",
	"Jul","Ago","Sep","Oct","Nov","Dic" ],
	dayNames: [ "Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado" ],
	dayNamesShort: [ "Dom","Lun","Mar","Mié","Jue","Vie","Sáb" ],
	dayNamesMin: [ "D","L","M","X","J","V","S" ],
	weekHeader: "Sm",
	dateFormat: "dd/mm/yy",
	firstDay: 1,
	isRTL: false,
	showMonthAfterYear: false,
	yearSuffix: "" };


	$.datepicker.setDefaults($.datepicker.regional['es'] );

	$(window).on( "resize", function(){
			anchopantalla = $(window).innerWidth();
		if (anchopantalla < 768){
			$('#navbar_ordenador').css("display","none");
			$('#div_botonanterior_ordenador').css("display","none");
			$('#navbar_movil').css("display", "block");
		}
		else{
			$('#navbar_movil').css("display", "none");
			$('#navbar_ordenador').css("display", "block");
			$('#div_botonanterior_ordenador').css("display","block");
		}
	});	
	
	$(window).resize();

} )