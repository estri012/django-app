$(document).ready(function(){
    $.datepicker.setDefaults({
        dateFormat: 'yy-mm-dd'
      });
      $("#firstdatepicker").datepicker();
      $("#lastdatepicker").datepicker();
      $("#filter").click(function() {
        var from_date = $("#firstdatepicker").val();
        var to_date = $("#lastdatepicker").val();
        if (from_date != '' && to_date != '') {
          console.log(from_date, to_date);
          var endpoint = '/api/data';
  
      $.ajax({
        method: "GET",
        url: endpoint,
        data: {
          from_date: from_date,
          to_date: to_date
        },
        success: function(data){
          console.log(data); //get all data
          //get data by fields
          var gyro_y = [], time = [];
          for (var i=0; i<data.length; i++){
            gyro_y.push(data[i].gyro_y);
            time.push(data[i].timestamp);
         }
          console.log(gyro_y);
          console.log(time);
        //plot the chart
          
          var ctx = document.getElementById("gyroyChart").getContext('2d');
          var gyroyChart = new Chart(ctx, {
              type: 'line',
              data: {
                  labels: time,
                  datasets: [{
                      label: 'Gyro-y (theta)',
                      data: gyro_y,
                      fill: false,
                      borderColor: "#80b6f4",
                    pointBorderColor: "#80b6f4",
                    pointBackgroundColor: "#80b6f4",
                    pointHoverBackgroundColor: "#80b6f4",
                    pointHoverBorderColor: "#80b6f4",
                    pointBorderWidth: 10,
                    pointHoverRadius: 10,
                    pointHoverBorderWidth: 1,
                    pointRadius: 1,
                    borderWidth: 4,
                  }]
              },
              options: {
                  reponsive: true,
                  scales: {
                      yAxes: [{
                          ticks: {
                              beginAtZero:false,
                              stepSize:0.5
                          },
                            scaleLabel: {
                            display:     true,
                            labelString: 'Gyro sb.y (theta)'
                        }
                      }],
                      xAxes: [{
                       
                              display: true,
                              type: "time",
                              time: {
                                    minUnit: "hour",
                                    unit: "hour",
                                    unitStepSize: 6,
                                    min: moment(from_date).toDate(),//Date object type
                                    max: moment(to_date).toDate()//Date object type
                              },
                            scaleLabel: {
                            display:     true,
                            labelString: 'Time'
                        }
                      }]
                  }
              }
          });
        },
        error: function(error_data){
          console.log(error_data)
        }
      });
    } else {
      alert("Please Select Date");
    }
      });    
  });