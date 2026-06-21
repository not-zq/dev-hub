
let chartTopSongs;

function renderTopSongs() {
    const data = JSON.parse(document.getElementById("dataTopSongs").textContent);
    const labels = data.map(x => x.master_metadata_track_name);
    const values = data.map(x => x.total_min);
    
    const canvas = document.getElementById("canvasTopSongs");
    const ctx = canvas.getContext("2d");

    const max = Math.max(...values);

    if (chartTopSongs) { chartTopSongs.destroy(); }

    /* https://www.chartjs.org/docs/latest/charts/bar.html */

    chartTopSongs = new Chart(ctx, {
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
                // title:   { display: true, text: "Top Songs"} ,
                legend:  { display: false } ,
                tooltip: { enabled: false }
            },
            scales: {
                x: { grid: { display: false }, ticks: { display: false }, reverse: true },
                y: { position: "right", grid: { display: false } }
            },
            responsive: true,
            maintainAspectRatio: false,
        },
        plugins: [valueLabelReversePlugin]
    });
}

renderTopSongs();

/* ------ */

function updateTopSongsChart(data) {
    const labels = data.map(x => x.master_metadata_track_name);
    const values = data.map(x => x.total_min);

    const max = Math.max(...values);

    chartTopSongs.data.labels = labels;
    chartTopSongs.data.datasets[0].data = values;
    chartTopSongs.data.datasets[0].backgroundColor = values.map(v => interpolateColor(v, max));

    chartTopSongs.update();
}

document.getElementById("artistDropdown").addEventListener("change", async (e) => {
    const artist = e.target.value;

    const res  = await fetch(`/getTopSongs/?artistDropdown=${artist}`);
    const data = await res.json();

    updateTopSongsChart(data);
});
