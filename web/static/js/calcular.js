function calcular(){
    var costo = document.getElementById("precio_costo").value;
    var porcentaje_utilidad =  document.getElementById("utilidad").value;
    var porcentaje_utilidad = parseFloat(costo) * parseFloat((porcentaje_utilidad) / 100);

    var precioventa= parseFloat(costo) + parseFloat(porcentaje_utilidad);
    document.getElementById("precio_venta").value = precioventa;
}


