
function zero_first_format(value)
    {
        if (value < 10)
        {
            value='0'+value;
        }
        return value;
    }
function date_time()
    {
        var current_datetime = new Date();
        var day = zero_first_format(current_datetime.getDate());
        var month = zero_first_format(current_datetime.getMonth()+1);
        var year = current_datetime.getFullYear();

        return day+"."+month+"."+year;
    }

    /* выводим текущую дату и время на сайт в блок с id "current_date_time_block" */
    document.getElementById('current_date_time_block').innerHTML = date_time();

////////////////////////////////////

function newElement() {
  var tr = document.createElement("tr");
  var inputValue = document.getElementById("myInput").value;
  var inputDate = document.getElementById("myDate").value;
  var t = document.createTextNode(inputValue);
  var myDate = new Date(inputDate);
    var cell = document.createElement('TD');
    cell.innerText = zero_first_format(myDate.getDate())+
        "."+zero_first_format(myDate.getMonth())+
        '.'+zero_first_format(myDate.getFullYear());
    tr.appendChild(t);
    tr.appendChild(cell);

  if (inputValue === ''|| myDate === "") {
    alert("Вы должны что-то написать!");
  } else {
   document.getElementById("myUL").appendChild(tr);
  }
  document.getElementById("myInput").value = "";
  document.getElementById("myDate").value = "";
}

 var list = document.getElementById('myUL').childNodes;
        for (let i = 0; i <= list.length; i++) {
            const element = list[i];
            element.addEventListener('click', function(ev) {
                ev.target.classList.toggle('checked')
            });
        }