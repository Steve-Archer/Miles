var city1url = document.getElementById('city1_urltag').innerHTML;
var city2url = document.getElementById('city2_urltag').innerHTML;
var apiKey = config.key;
var apiPassword = config.password;
fetch_string = "https://wft-geo-db.p.rapidapi.com/v1/geo/cities/" + city1url +"/distance?toCityId=" + city2url + "&distanceUnit=MI"
const getDistance= ()=> {
    fetch(fetch_string,{
        "method": "GET",
        "headers": {
            "x-rapidapi-host": apiKey,
            "x-rapidapi-key": apiPassword
        }
    })
        .then(res =>  res.json())
        .then(data => {
            let json_data = JSON.stringify(data);
            let json_short = json_data.slice(8);
            let json_shorter = json_short.slice(0, -1);
            let json_int = parseFloat(json_shorter)
            let distance = document.getElementById('distance');
            distance.innerHTML = json_int;
        })
}
const start_clock= ()=> {
    clock();
}
const clock = () => {
    let second = document.getElementById('clock').innerHTML
    second = parseInt(second);
    second--;
    document.getElementById('clock').innerHTML = second;
    if(second == 0){
        end_of_round();
    }
    setTimeout('clock()', 1000);
}
const end_of_round = () => {
    document.getElementById('clock').style.color = "white";
    let guess = document.getElementById('input').value;
    let actual = document.getElementById('distance').innerHTML;
    let actual_rounded = Math.round(actual)
    let score = parseFloat(guess) - parseFloat(actual_rounded);
    let abs_score = Math.abs(score);
    let finished_score = abs_score;
    document.getElementById('score').value = finished_score;
    document.getElementById('distance').innerHTML = actual_rounded;
    document.getElementById('score_string').innerHTML = "Your score was " + finished_score + "."
    document.getElementById('end_of_round_div').style.display = "block";
}
getDistance();
start_clock();