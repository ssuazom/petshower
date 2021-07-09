

$(document).ready(function(){
  $("#enviar").click(function(){
    $.get("http://127.0.0.1:8000/api/lista_mascotas",
        function(data){
            $.each(data, function(i, item){
                $("#Rescata").append("<tr><td>"+item.idMascota+"</td><td><img src='"+item.image_mascota+"'>"+
                                      "</td><td>"+item.nombre+""+
                                      "</td><td>"+item.edad+"</td><td>"+item.tipo+"</td><tr>");
            });
        });
  })
})





/****************************************************** Bloqueo ID Formulario Modificar  ******************************************************/
$(document).ready(function(){
    $('#id_idProducto').attr('readonly','readonly')
    $('#id_idIntegrante').attr('readonly','readonly')
    $('#id_idVeterinario').attr('readonly', 'readonly')
});



/****************************************************** Estilos Valores Monetario Tiempo Real  ******************************************************/

$(document).ready(function() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open ('GET', 'https://mindicador.cl/api', true)
    xmlhttp.send ();

    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) 
        {
            var data = JSON.parse(this.responseText);
        }
        document.getElementById("v_UF").innerHTML = new Intl.NumberFormat('es-CL',{style:'currency',currency:'CLP',maximumFractionDigits:2}).format(data.uf.valor);
        document.getElementById("v_Dolar").innerHTML =  new Intl.NumberFormat('es-CL',{style:'currency',currency:'CLP',maximumFractionDigits:2}).format(data.dolar.valor);
        document.getElementById("v_Euro").innerHTML =  new Intl.NumberFormat('es-CL',{style:'currency',currency:'CLP',maximumFractionDigits:2}).format(data.euro.valor);
    }
});




/****************************************************** Estilos Conversor Monetario  ******************************************************/

function convertir() {

    var valor = parseFloat(document.getElementById("cantidad").value);
    document.getElementById("valor").innerHTML = "<b>"+valor+"</b>";
    var de=document.getElementById("de").value;
    var a=document.getElementById("a").value;

    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open ('GET', 'https://mindicador.cl/api', true)
    xmlhttp.send ();

    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) 
        {
            var data = JSON.parse(this.responseText);
        }
        var dolar = data.dolar.valor;
        var euro = data.euro.valor;



        //peso a Dolar
        if(de==1&&a==2)
        {
            resultado=valor/dolar;
        }
        //peso a Euro
        else if(de==1&&a==3)
        {
            resultado=valor/euro;
        }
        //Dolar a peso
        else if(de==2&&a==1)
        {
            resultado=valor*dolar;
        }
        //Dolar a Euro
        else if(de==2&&a==3)
        {
            resultado=valor*(dolar/euro);
        }
        //Euro a peso
        else if(de==3&&a==1)
        {
            resultado=valor*euro;
        }
        //Euro a Dolar
        else if(de==3&&a==2)
        {
            resultado=valor*(euro/dolar);
        }
        //peso a peso, Dolar a Dolar, Euro a Euro
        else
        {
            resultado=valor;
        }
        document.getElementById("resultado").innerHTML = "Resultado: $"+resultado.toFixed(2);
    }
}


/****************************************************** Validador del Formulario  ******************************************************/
function isEmptyStr(value){
    return !value || value.trim() === "";
  }
  
  function hasNumbers(value){
    const regex = /\d/;
    return regex.test(value)
  }
  
  function validateEmail(email){
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
  }
  
  function  validateNumbers(value) {
    const reg = /^\d+$/;
    return reg.test(value);
  }
  
  function validateRut(value){
      let i; 
    let s; 
    let f; 
    let result;
      f = "32765432";
      r = value;
      largo=r.length - 2;
      result=false;
      s=0;
      for (i=0;i<largo;i++){
          s=s+(parseInt(r.charAt(i)) * parseInt(f.charAt(i)));
      }
      dv=11-(s%11);
      if (dv==10 && (r.charAt(9)=='K' || r.charAt(9)=='k')){
          result=true;
      }else{
          if (dv==11 && r.charAt(9)=='0'){
              result=true;
          }else{
              if (dv==parseInt(r.charAt(9))){
                  result=true;
              }else{
                  result=false;
              }
          }
      }
      return result;
  }
  
  
  const submitBtn = document.getElementById("btn-contact");
  const inputs = {
    Rut: {
        element: document.getElementById("input-rut"),
        msg: document.getElementById("input-rut-error-msg"),
        validator: (value) =>  {
          const errors = []
          if(isEmptyStr(value)){
            errors.push("Campo requerido")
            return errors;
          }
    
          if(!validateRut(value)) {
            errors.push("Rut incorrecto")
            return errors;
          }
          return errors;
        },
      },

    firstname: {
      element: document.getElementById("input-firstname"),
      msg: document.getElementById("input-firstname-error-msg"),
      validator: (value) => {
        const errors = []
        if(isEmptyStr(value)){
          errors.push("Campo requerido");
          return errors;
        }
        if(hasNumbers(value)) errors.push("Nombre no debe poseer números")
        return errors;
      },
    },
    lastname: {
      element: document.getElementById("input-lastname"),
      msg: document.getElementById("input-lastname-error-msg"),
      validator: (value) => {
        const errors = []
        if(isEmptyStr(value)){
          errors.push("Campo requerido")
          return errors;
        }
        if(hasNumbers(value)) {
          errors.push("Apellido no debe poseer números");
          return errors;
        }
  
        return errors;
      },
    },
  
    edad: {
        element: document.getElementById("input-edad"),
        msg: document.getElementById("input-edad-error-msg"),
        validator: (value) =>  {
          const errors = []
          if(isEmptyStr(value)){
            errors.push("Campo requerido")
            return errors;
          }
    
          if(!validateNumbers(value)) {
            errors.push("Edad no debe contener letras");
            return errors
          }
  
          if (!validateEdad(value)) {
              errors.push("Debes ser mayor de edad");
              return errors
          }
          return errors;
        },
      },

    email: {
        element: document.getElementById("input-email"),
        msg: document.getElementById("input-email-error-msg"),
        validator: (value) => {
          const errors = []
          if(isEmptyStr(value)){
            errors.push("Campo requerido");
            return errors;
          }
          if(!validateEmail(value)) errors.push("Email inválido")
          return errors;
        },
      },
  
    Telefono: {
      element: document.getElementById("input-telefono"),
      msg: document.getElementById("input-telefono-error-msg"),
      validator: (value) =>  {
        const errors = []
        if(isEmptyStr(value)){
          errors.push("Campo requerido");
          return errors;
        }
  
        //Si no es numero retornar error.
        if(!validateNumbers(value)) {
          errors.push("Número de telefono solo puede contener numeros");
          return errors
        }
        return errors;
      },
    },
  
    city: {
      element: document.getElementById("input-city"),
      msg: document.getElementById("input-city-error-msg"),
      validator: (value) => {
        const errors = []
        if(isEmptyStr(value)){
          errors.push("Campo requerido")
        }
        return errors;
      },
    },
  }
  
  function initValidation(){
    for(const key of Object.keys(inputs)){
      const input = inputs[key];
      input.element.addEventListener("keyup", function(event){
        const val = event.target.value;
        const errors = input.validator(val);
        const valid = errors.length === 0;
        if(valid){
          input.msg.innerHTML = "";
          input.msg.style.display = "hidden";
        } else {
          input.msg.innerHTML = `${errors}`;
          input.msg.style.display = "visible";
        }
      })
    }
  }
  
  function validateAll(){
    let validForm = true;
    for(const key of Object.keys(inputs)){
      const input = inputs[key];
      const val = input.element.value;
      const errors = input.validator(val);
      const valid = errors.length === 0;
      if(valid){
        input.msg.innerHTML = "";
        input.msg.style.visibility = "hidden";
      } else {
        input.msg.innerHTML = `${errors}`;
        input.msg.style.visibility = "visible";
        validForm = false;
      }
    }
    return validForm;
  }
  submitBtn.addEventListener("click", function(event){
    event.preventDefault();
    const valid = validateAll();
    if(valid){
      alert("Formulario enviado!")
    }
  })
  initValidation()  




/****************************************************** Estilos Valores Monetario Tiempo Real  ******************************************************/

$(document).ready(function() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open ('GET', 'https://mindicador.cl/api', true)
    xmlhttp.send ();

    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) 
        {
            var data = JSON.parse(this.responseText);
        }
        document.getElementById("v_UF").innerHTML = new Intl.NumberFormat('es-CL',{style:'currency',currency:'CLP',maximumFractionDigits:2}).format(data.uf.valor);
        document.getElementById("v_Dolar").innerHTML =  new Intl.NumberFormat('es-CL',{style:'currency',currency:'CLP',maximumFractionDigits:2}).format(data.dolar.valor);
        document.getElementById("v_Euro").innerHTML =  new Intl.NumberFormat('es-CL',{style:'currency',currency:'CLP',maximumFractionDigits:2}).format(data.euro.valor);
    }
});



