let tripToParse = "Perdita 8 10 8";

/* étape 1 : rend une ligne du même format que les lignes de l'exemple, la décompose en mot 
(séparés par un espace) puis range ces mots dans une structure de donnée */

function parseTrip(trip) {
    const prospect = new Object();
    trip = trip.split(" ");
    prospect.client = trip[0];
    prospect.start = parseInt(trip[1]);
    prospect.duration = parseInt(trip[2]);
    prospect.price = parseInt(trip[3]);
    return prospect;
}

/* Etape 2 : Utilisez la fonction parseTrip(trip) dans une autre fonction parseTrips(trips) prenant en entrée une journée 
complète (donc plusieurs lignes) et retournant une liste de structures trips définies précédemment  ([]). */

let tripsToParse = [
    "Roger 0 5 10",
    "Pongo 3 7 14",
    "Perdita 8 10 8",
    "Anita 16 3 7",
];

function parseTrips(trips) {
    return trips.map(parseTrip);
}

/* Etape 3 :Pour optimiser vos journées, vous décidez d'écrire un code calculant l'enchaînement 
de clients le plus intéressant financièrement.
Créez une fonction `getTripsPrice` qui accepte en argument une liste de `voyages` et retourne 
la somme des prix de cet ensemble de `voyages`. */

function getTripsPrice(trips) {
    let sumPrices = 0;
    for (trip of trips) {
        sumPrices += trip.price;
    }
    return sumPrices;
}

/* Etape 4 : Créez une fonction `checkCompatibility(tripA, tripB)` qui comparent deux structures `voyages` et 
retourne un booléen déterminant si les structures sont compatibles ou non.
Il s'agit de déterminer si un vol (représenté par une structure `trips`) n'empiète pas sur les horaires d'un autre. */

function checkCompatibility(tripA, tripB) {
    return (
        tripA.start + tripA.duration <= tripB.start ||
        tripB.start + tripB.duration <= tripA.start
    );
}

/* Etape 5 : Développez une fonction findCompatibilities(trips) qui retourne, à partir d'une liste de voyages, tous les 
ensembles de voyages compatibles les uns avec les autres. */

function findCompatibilities(trips) {
    let compatibilityArray = [];
    for (let i = 0; i < trips.length; i++) {
        compatibilityArray.push([trips[i]]);
        for (let j = i + 1; j < trips.length; j++) {
            if (checkCompatibility(trips[i], trips[j])) {
                compatibilityArray.push([trips[i], trips[j]]);
            }
        }
    }
    console.log("Compatibilities are :", compatibilityArray);
    return compatibilityArray;
}

/* Etape 6 : Développez une dernière fonction findBestPrice(trips), qui renverra le combo ou le voyage
 seul qui rapportera le plus à votre entreprise. */

function findBestPrice(trips) {
    let compatibilities = findCompatibilities(trips);
    let maxPrice = 0;
    let bestCombo = [];
    for (i = 0; i < compatibilities.length; i++) {
        let temp = getTripsPrice(compatibilities[i]);
        if (temp > maxPrice) {
            maxPrice = temp;
            bestCombo = compatibilities[i];
        }
    }
    console.log("Best Combo is:", bestCombo);
    return bestCombo;
}

let tripsWellParsed = parseTrips(tripsToParse);
findBestPrice(tripsWellParsed);
