// ----------
// Left Pane
// ----------

// Number of symptons entered
var symptoms = 0;

// coverts the symptoms to a json and send them to the server
function main() {
   // send(convertToJSON());
   diagnose();
}

//Adds another symptom input box to the website
function appendSymptom() {
    symptoms += 1;
    $("#symptomForm").append("<br><input id = " + symptoms + " placeholder = \"Enter Symptom\" value = \"\" name = \"" + symptoms + "\"></input>");
}  

// Sends the JSON to the server
function send(symptomsJSON) {
    console.log("Sending: "+ symptomsJSON);
    $.ajax({
        type: 'POST',
        contentType: 'application/json',
        url: 'http://ec2-18-208-194-254.compute-1.amazonaws.com:5000/webSubmit',
        data: symptomsJSON,
        crossDomain: true,
        dataType: 'text',
        success: function(data) { diagnose(data); },
        error: function() { alert('Failed!'); }
    });
}

// converts the symptoms to a JSON
function convertToJSON() {
    
    var el;
    var symptomsArr = [];
    for(var i  = 0; el = document.getElementById(i); i++) {
        if(document.getElementById(i).value != "") {
            symptomsArr[i] = document.getElementById(i).value;
        }

    }

   symptomsJSON = JSON.stringify(symptomsArr);
    return symptomsJSON;
}

// ----------
// Right Pane
// ----------

// Runs once the diagnosis data is returned, updates the right pane
function diagnose(data){
data = {
    "diseases":
        [
            {
                "label":"cold",
                "value":.83
            },
            {
                "label":"fever",
                "value":.10
            },
            {
                "label":"bold",
                "value":.7
            }
        
        ]
    }

    var testing = JSON.parse("[{\"label\": \"friends\", \"value\": 30}, {\"label\": \"allies\", \"value\": 15}]");

    //console.log(data.diseases);
    var rightPane = document.getElementById("rightPane");
    var HTMLData = "";
    for(i in data.diseases) {
        data.diseases[i].value = (data.diseases[i].value * 100);
        HTMLData = HTMLData + data.diseases[i].label + ": " + data.diseases[i].value + "%" + "<br>";
    }
    rightPane.innerHTML = HTMLData;
    
    console.log(data.diseases);
    console.log(testing);
Morris.Donut({
    element: "pie-chart", data: data.diseases
});

}