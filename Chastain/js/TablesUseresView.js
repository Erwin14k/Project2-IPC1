get_patients();


function get_patients(){
    let patients_Table = document.querySelector("");
    fetch("",{
        method:"GET",
        headers:{
            'Content-Type':'application/json'
        }
    }).then(res => res.json())
    .catch(err  => {
        console.log("ha ocurrido un error"+err)
    })
    .then(res => {
        var array = response.data;
        res.forEach(patient => {
            for (let i = 0; i < array.length; i++) {
                new_html += `\n<tr>
                <td>`+ array[i].name + `</td>
                <td>`+ array[i].last_name + `</td>
                <td>`+ array[i].user_name + `</td>
                <td>`+ array[i].speciality + `</td>
            </tr>`

            }   
        });
    })        
}