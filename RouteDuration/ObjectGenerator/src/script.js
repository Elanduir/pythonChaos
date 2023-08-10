let paths = [];
let missing = [];
let str = "";
let lookup = {
    "7494 Wiesen, Switzerland":"13",
    "Monstein, 7278 Davos, Switzerland":"11",
    "Monstein, 7278 Davos, Switzerland":"12",
    "Glaris, 7277 Davos, Switzerland":"9",
    "Frauenkirch, 7276 Davos, Switzerland":"8",
    "Sertig-Dörfli, 7272 Davos, Switzerland":"10",
    "Bahnhofstrasse 9, 7270 Davos Platz, Switzerland":"7",
    "Praviganweg, 7270 Davos, Switzerland":"5",
    "Berglistutz 3, 7270 Davos, Switzerland":"6",
    "Tobelmühlestrasse 2, 7270 Davos, Switzerland":"14",
    "Scalettastrasse 1, 7270 Davos Platz, Switzerland": "4",
    "Aelastrasse 1, 7260 Davos, Switzerland":"3",
    "Davos Dorf, Promenade 159, 7260 Davos Dorf, Switzerland":"1",
    "Tschuggen, 7260 Davos, Switzerland":"2",
    "Laret, 7265 Davos, Switzerland":"0"
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
        let origin = lookup[obj1["origin_addresses"][0]];

        for(var x = 0; x < obj1["destination_addresses"].length; x++){
            let p = new Path;
            p.from = origin.toString();
            p.to = lookup[obj1["destination_addresses"][x]];
            try{
                p.carDuration = obj1["rows"][0]["elements"][x]["duration"]["value"].toString();
            }catch{
                p.carDuration = "0";
            }
            try{
                p.bicycleDuration = obj2["rows"][0]["elements"][x]["duration"]["value"].toString();
            }catch{
                p.bicycleDuration = "0";
            }
            try{
                p.transitDuration = obj3["rows"][0]["elements"][x]["duration"]["value"].toString();
            }catch{
                p.transitDuration = "0";
            }
            try{
                p.walkingDuration = obj4["rows"][0]["elements"][x]["duration"]["value"].toString();
            }catch{
                p.walkingDuration = "0";
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
