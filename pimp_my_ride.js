let tripToParse = "Perdita 8 10 8";

/* étape 1 : rend une ligne du même format que les lignes de l'exemple, la décompose en mot 
(séparés par un espace) puis range ces mots dans une structure de donnée */
function parseTrip(trip) {
    const prospect = new Object();
    trip = trip.split(" ");
    //console.log(trip);
    prospect.client = trip[0];
    prospect.start = trip[1];
    prospect.duration = trip[2];
    prospect.price = trip[3];
    //console.log(prospect);
    return prospect;
}

parseTrip(tripToParse);

/* Etape 2 : Utilisez la fonction parseTrip(trip) dans une autre fonction parseTrips(trips) prenant en entrée une journée 
complète (donc plusieurs lignes) et retournant une liste de structures trips définies précédemment  ([]). */

let tripsToParse = [
    "Roger 0 5 10",
    "Pongo 3 7 14",
    "Perdita 8 10 8",
    "Anita 16 3 7",
];

function parseTrips(trips) {
    const prospects = [];
    for (trip of trips) {
        //console.log(trip);
        prospects.push(parseTrip(trip));
    }
    //console.log(prospects);
    return prospects;
}

/* Etape 3 :Pour optimiser vos journées, vous décidez d'écrire un code calculant l'enchaînement 
de clients le plus intéressant financièrement.
Créez une fonction `getTripsPrice` qui accepte en argument une liste de `voyages` et retourne 
la somme des prix de cet ensemble de `voyages`. */

function getTripsPrice(trips) {
    let sumPrices = 0;
    let prospectsArray = parseTrips(trips);
    for (prospect of prospectsArray) {
        sumPrices += parseInt(prospect.price);
        console.log(sumPrices);
    }
    return sumPrices;
}

getTripsPrice(tripsToParse);
