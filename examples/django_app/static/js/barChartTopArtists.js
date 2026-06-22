
let chartTopArtists;

function renderTopArtists() {

    const data = JSON.parse(document.getElementById("dataTopArtists").textContent);
    const labels = data.map(x => x.master_metadata_album_artist_name);
    const values = data.map(x => x.total_min);
    
    const canvas = document.getElementById("canvasTopArtists");
    const ctx = canvas.getContext("2d");
    
    const max = Math.max(...values);

    chartTopArtists = new Chart(ctx, {
        type: "bar",
        data: {
            labels: labels,
            datasets: [{
                data: values,
                backgroundColor: values.map(v => interpolateColor(v, max)),
                hoverBackgroundColor: "#a3d482",
            }]
        },
        options: {
            indexAxis: "y",
            plugins: {
                // title:   { display: true, text: "Top Artists"} ,
                legend:  { display: false },
                tooltip: { enabled: false }
            },
            scales: {
                x: { grid: { display: false }, ticks: { display: false }, reverse: true },
                y: { position: "right", grid: { display: false } }
            },
            responsive: true,
            maintainAspectRatio: false
        },
        plugins: [valueLabelReversePlugin]
    });

}

renderTopArtists();
