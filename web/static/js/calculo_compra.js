function calcular_campos(campo){

    var cantidad = document.getElementById("cant_prod").value;
    var precio_costo =  document.getElementById("precio_costo").value;
    var resultado1 = 0 ;
    var resultado2 = 0;
    switch(campo){
        case 'subtotal': {
            resultado1 = parseFloat(cantidad) * parseFloat(precio_costo);
            document.getElementById("subtotal_compra").value = resultado1;
        }break;
        case 'total':{
            resultado2= parseFloat(cantidad) * parseFloat(precio_costo);
            document.getElementById("total_compra").value = resultado2;
        }break;
    }

    }



