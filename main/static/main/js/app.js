$(document).ready(function(){
    validation = new Date()
    validation.setFullYear(validation.getFullYear() -18)
    format= `${validation.getFullYear()}-${(validation.getMonth()+1)}-${validation.getDate()}`
    console.log(format)
    $("#formulario").validate({
        errorClass:"is-invalid",
        rules:{
            nombre:{
                required:true
            },
            apellido:{  
                required:true
            },
            region:{
                required: true
            },
            correo:{
                required: true,
                email: true
            },
            correoconfi:{
                required: true,
                email: true
            },
            pass:{
                required: true
            },
            fnacimiento:{
                required:true,
                max:format
            },

        },
        messages:{
            nombre:{
                required:"Debe ingresar su nombre"
            },
            apellido:{
                required:"Debe ingresar su apellido"
            },
            region:{
                required:"Debe ingresar su región"
            },
            correo:{
                required:"Debe ingresar su correo",
                email:"Debe ingresar un correo valido"
            },

            correoconfi:{
                    required:"Debe confirmar su correo",
                    email:"Debe ingresar un correo valido"
            },

            pass:{
                required:"Debe ingresar una contraseña"
            },
            fnacimiento:{
                required:"Debes ingresar tu fecha de nacimiento",
                max:"Debes ser mayor de 18 años para continuar"
            },


        }
    })
})