import http from 'http';
import url from 'url';

//Porta del server
const port = 3001;

//Dichiarazione array
const tmpArr = [];

http.createServer((req, res) => {
    if (req.method === 'GET') {

        //Parametri raccolti dal form
        let parametri = url.parse(req.url, true);
        let tmp_max = parseFloat(parametri.query.tmp_max);
        let tmp_min = parseFloat(parametri.query.tmp_min);
        let citta = parametri.query.citta;
        const timestamp = Date.now();

        //Array
        tmpArr.push({
            cittaArr: citta,
            tmp_max_Arr: tmp_max,
            tmp_min_Arr: tmp_min,
            timestamp: timestamp,
        });

        //Pagina di raccolta
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write('<!DOCTYPE html>');
        res.write('<html lang="en">');
        res.write('<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Riepilogo Dati</title></head>');
        res.write('<body>');

        res.write('<h2>Dati Raccolti:</h2>');
        res.write('<ul>');
        tmpArr.forEach((data) => {
            res.write(`<li>${data.cittaArr} - Max: ${data.tmp_max_Arr}, Min: ${data.tmp_min_Arr}</li>`);
        });
        res.write('</ul>');

        res.write('<h2>Media temperature</h2>');
        //

        res.write('</body></html>');
        res.end();
    }
}).listen(port);

// function zone(cittaArr) {
//     const zoneObj = {
//         'Trento': 'Nord',
//         'Milano': 'Nord',
//         'Torino': 'Nord',
//         'Firenze': 'Centro',
//         'Bologna': 'Centro',
//         'Roma': 'Centro',
//         'Napoli': 'Sud',
//         'Bari': 'Sud',
//         'Messina': 'Sud',
//     };
//     return zoneObj[cittaArr];
// }
