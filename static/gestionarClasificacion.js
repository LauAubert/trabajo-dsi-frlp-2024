var clasificacion = [];
function agregarClasificacion() {
    const posicion = document.getElementById('posicion').value;
    const equipo = document.getElementById('equipo').value;
    const equipoNombre = document.getElementById('equipo').options[document.getElementById('equipo').selectedIndex].text;
    const clasificacionInput = document.getElementById('clasificacion-input');

    if (posicion && equipo) {
        const tabla = document.getElementById('tabla-clasificacion').getElementsByTagName('tbody')[0];
        const nuevaFila = tabla.insertRow();
        nuevaFila.innerHTML = `
            <td>${posicion}</td>
            <td>${equipoNombre}</td>
            <td><button class="btn btn-danger btn-sm" onclick="eliminarClasificacion(this)">Eliminar</button></td>
        `;

        // Limpiar los campos de entrada
        document.getElementById('posicion').value = '';
        document.getElementById('equipo').value = '';
        clasificacion.push({ posicion, equipo });
        console.log(clasificacion);
    }
}

function eliminarClasificacion(btn) {
    const row = btn.parentNode.parentNode;
    row.parentNode.removeChild(row);
    clasificacion.splice(row.rowIndex - 1, 1);
    console.log(clasificacion);
}
