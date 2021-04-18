try{
    let loginBtn = document.querySelector("#btnLogin");
    loginBtn.addEventListener("click",login);
    
} catch (error) {
    
}



// Función para inicar sesión
function login(){
    // Obteniendo valores de los inputs usuario y contraseña
    let userName = document.querySelector("#username").value;
    let password = document.querySelector("#passwordI").value;
    
    // Este if verificará que los input de usuario y contraseña no esten vacios
    if(userName != "" && password != ""){
        // Haciendo una petición al servidor de alojamiento
        fetch("",{
            //En este caso se utiliza un método POST
            method:"POST",
            headers:{
                'Content-Type':'application/json'
            },
            body: JSON.stringify({
                "user_name": userName,
                "password":password                
            })
        }).then(back => back.json())
        .catch(err  => {
            //Si ocurre un error con el servidor nos mostrará este mensaje
            window.alert("Ocurrio un error al intentar iniciar sesión, intente de Nuevo")
        })
        .then(res => {
            // Verificando estado de respuesta y cambiando vista a login
            if(res.state == "ok"){
                window.alert(res.message)
                window.location = "/SpartanStore-Client/index.html"
                localStorage.setItem("logged", true);
                localStorage.setItem("userName", userName);
                localStorage.setItem("userRole", res.userRole);
            }
            else{
                window.alert(res.message)
            }
        })
    }
    else{
        window.alert("Debes llenar Todos los campos para poder iniciar Sesión")
    }
}