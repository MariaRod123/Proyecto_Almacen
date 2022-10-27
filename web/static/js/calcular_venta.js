function calcular_venta(){
    var cantidad = document.getElementById("cantidad").value;
    var preciounit =  document.getElementById("subtotal").value;
    var total_venta = parseFloat(cantidad) * parseFloat(preciounit);

    document.getElementById("total").value = total_venta;

    }

