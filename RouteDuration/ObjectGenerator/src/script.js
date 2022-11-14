let paths = [];
let missing = [];
let str = "";
let lookup = {
    "Wiesen Davos":"13",
    "Monstein alt Davos":"12",
    "Monstein neu Davos":"11",
    "Glaris Davos":"9",
    "Frauenkirch Davos":"8",
    "Sertig Davos":"10",
    "Pauluskirche Davos":"7",
    "Marienkirche Davos":"5",
    "St. Johann Davos":"6",
    "Alexanderhaus Davos":"14",
    "Englische Kirche Davos":"4",
    "Herz Jesu Davos":"3",
    "St. Theodul Davos":"1",
    "Tschuggen Davos":"2",
    "Laret Davos":"0",
};
class Path {
    constructor() {
        this.id = "";
        this.from = "";
        this.to = "";
        this.carDuration = "";
        this.bicycleDuration = "";
        this.transitDuration  = "";
        this.walkingDuration = "";
    }
}

async function fetchAsync () {
    let url = "https://raw.githubusercontent.com/Elanduir/pythonChaos/main/RouteDuration/responseNew.txt"
    let response = await fetch(url);
    let json = await response.json();
    console.log(json.length);
    for(var i = 0; i < json.length-3; i+=4){
        /*
        {
            "id": "222",
            "from": "12",
            "to": "11",
            "carDuration": "100",
            "bicycleDuration": "100",
            "transitDuration": "100",
            "walkingDuration": "100"
        },
        */


        let obj1 = json[i];
        let obj2 = json[i+1];
        let obj3 = json[i+2];
        let obj4 = json[i+3];
        let origin = obj1["destination_addresses"].indexOf(obj1["origin_addresses"][0]);

        for(var x = 0; x < obj1["destination_addresses"].length; x++){
            let p = new Path;
            p.from = origin.toString();
            p.to = x.toString();
            try{
                p.carDuration = obj1["rows"][0]["elements"][x]["duration"]["value"].toString();
            }catch{
                p.carDuration = "-1";
            }
            try{
                p.bicycleDuration = obj2["rows"][0]["elements"][x]["duration"]["value"].toString();
            }catch{
                p.bicycleDuration = "-1";
            }
            try{
                p.transitDuration = obj3["rows"][0]["elements"][x]["duration"]["value"].toString();
            }catch{
                p.transitDuration = "-1";
            }
            try{
                p.walkingDuration = obj4["rows"][0]["elements"][x]["duration"]["value"].toString();
            }catch{
                p.walkingDuration = "-1";
            }
            paths.push(p);
        }

    }

    for(var x = 0; x < paths.length; x++){
        str += paths[x].toString();
        paths[x].id = x.toString();
        if(Object.values(paths[x]).indexOf("-1") > 0){
            missing.push(x);
            console.log(missing);
        }
    }

    console.log(paths);

}

fetchAsync();
