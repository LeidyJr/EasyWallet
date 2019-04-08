  $(document).ready(function(){
      $.get('{% url "usuarios:getGraficPie" %}', function(data) {
          console.log(data)
          var colors = ["primary","success","info","warning","danger","secondary"]
          for (var i = 0; i < data.length; i++) {
            var ctx = document.getElementById(data[i].nombre);
            console.log(data[i].nombre);
            var tamañoCategoria = data[i].categorias.length;
            var labelsIn = []
            var dataIn = []
            for (var x = 0; x < tamañoCategoria; x++) {
              //console.log(data[i].categorias[x].categoria_nombre);
              labelsIn.push(data[i].categorias[x].categoria_nombre);
              dataIn.push(data[i].categorias[x].categoria_planeado);              
              var addDiv = $(document.getElementById(data[i].nombre+"_"+data[i].total_planeado));
              $(addDiv).append(" <span class='mr-2'><i class='fas fa-circle text-"+colors[x]+"'></i> "+data[i].categorias[x].categoria_nombre+"</span>");
              var addProgress = $(document.getElementById("body_"+data[i].nombre));
              var porcentaje = data[i].categorias[x].categoria_actual/data[i].categorias[x].categoria_planeado
              porcentaje = Math.trunc(porcentaje*100)
              console.log("PORCENTAJE : "+porcentaje)
              $(addProgress).append("<h4 class='small font-weight-bold'>"+data[i].categorias[x].categoria_nombre+"<span class='float-right'>"+porcentaje+"%</span></h4>");
              $(addProgress).append("<div class='progress mb-4'><div class='progress-bar bg-"+colors[x]+"' role='progressbar' style='width: "+porcentaje+"%' aria-valuenow='0' aria-valuemin='0' aria-valuemax='100' ></div></div>");
            }
            new Chart(ctx, {
              type:'doughnut',
              data:{
                labels: labelsIn,
                datasets: [{
                  data: dataIn,
                  backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc','#f6c23e','#e74a3b','#858796'],
                  hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf'],
                  hoverBorderColor: "rgba(234, 236, 244, 1)",
                }],
              },
              options: {
                maintainAspectRatio: false,
                tooltips: {
                  backgroundColor: "rgb(255,255,255)",
                  bodyFontColor: "#858796",
                  borderColor: '#dddfeb',
                  borderWidth: 1,
                  xPadding: 15,
                  yPadding: 15,
                  displayColors: false,
                  caretPadding: 10,
                },
                legend: {
                  display: false
                },
                cutoutPercentage: 80,
              },
            });
          }
      });
  });