var city1url = document.getElementById('city1_urltag').innerHTML;
var city2url = document.getElementById('city2_urltag').innerHTML;
var apiKey = config.key;
var apiPassword = config.password;
fetch_string = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities/" + city1url +"/distance?toCityId=" + city2url + "&distanceUnit=MI"
function getDistance(){
    fetch(fetch_string,{
        "method": "GET",
        "headers": {
            "x-rapidapi-host": apiKey,
            "x-rapidapi-key": apiPassword
        }
    })
        .then(res =>  res.json())
        .then(data => {
            var json_data = JSON.stringify(data);
            var json_short = json_data.slice(8);
            var json_shorter = json_short.slice(0, -1);
            var json_int = parseFloat(json_shorter)
            var distance = document.getElementById('distance');
            distance.innerHTML = json_int;
        })
}
function start_clock(){
    clock();
}
function clock(){
    var second = document.getElementById('clock').innerHTML
    second = parseInt(second);
    second--;
    document.getElementById('clock').innerHTML = second;
    if(second == 0){
        end_of_round();
    }
    setTimeout('clock()', 1000);
}
function end_of_round(){
    document.getElementById('clock').style.color = "white";
    var guess = document.getElementById('input').value;
    var actual = document.getElementById('distance').innerHTML;
    var actual_rounded = Math.round(actual)
    var score = parseFloat(guess) - parseFloat(actual_rounded);
    var abs_score = Math.abs(score);
    var finished_score = abs_score;
    document.getElementById('score').value = finished_score;
    document.getElementById('distance').innerHTML = actual_rounded;
    document.getElementById('score_string').innerHTML = "Your score was " + finished_score + "."
    document.getElementById('end_of_round_div').style.display = "block";
}
getDistance();
start_clock();