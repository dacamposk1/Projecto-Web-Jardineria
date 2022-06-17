const listarDonadores = async () => {
    const response = await fetch("https://venta-jardineria-c4c18-default-rtdb.firebaseio.com/donadores/.json");
    const data = await response.json();
    // console.log(data);

   data.forEach((dat, index) => {
        console.log(data);
        tableBody += `<tr>
        <td>${data.correo}</td>
        <td>${data.monto}</td>
        <td>${data.nombre}</td>
        </tr>`
    });

    tableBody_Data.innerHTML = tableBody;
};

window.addEventListener("load", function () {
    listarDonadores();

});