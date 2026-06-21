
/* Full dataset fot the Monthly Listening Time */

const dataMonthlyListeningTime = JSON.parse(document.getElementById("dataMonthlyListeningTime").textContent);

/* Date Slider */

const slider = document.getElementById("dateSlider");

noUiSlider.create(slider, {
    start: [0, dataMonthlyListeningTime.length - 1],
    connect: true,
    range: {
        min: 0,
        max: dataMonthlyListeningTime.length - 1
    },
    step: 1
});

/* Render Chart function */

let chartMonthlyListeningTime;

function renderMonthlyListeningTime(data) {

    const labels = data.map(x => 
        new Date(x.month).toLocaleDateString("en-US", {
            month: "short", year: "2-digit"
        })
    );
    const values = data.map(x => x.total_hrs);
    
    const canvas = document.getElementById("canvasMonthlyListeningTime");
    const ctx = canvas.getContext("2d");
    
    const max = Math.max(...values);

    if (chartMonthlyListeningTime) { chartMonthlyListeningTime.destroy(); }

    chartMonthlyListeningTime = new Chart(ctx, {
        type: "line",
        data: {
            labels: labels,
            datasets: [{
                data: values,
                borderColor: "#a3d482",
                borderWidth: 2,
                pointRadius: 0,
                pointHoverRadius: 0,
                tension: 0.4,
                fill: false
            }]
        },
        options: {
            scales: {
                x: { grid:  { display: false } },
                y: { 
                    // title: { display: true, text: "Listening time [hrs]" },
                    grid:  { display: false } 
                }
            },
            plugins: {
                // title:   { display: true, text: "Monthly Listening Time" },
                legend:  { display: false } ,
                tooltip: { enabled: false }
            },
            responsive: true,
            maintainAspectRatio: false
        }
    });

}

renderMonthlyListeningTime(dataMonthlyListeningTime); // Render the first time

/* Re-render the Chart based on the slider */

slider.noUiSlider.on("update", (values) => {
    const start = Math.round(values[0]);
    const end   = Math.round(values[1]);

    const filteredData = dataMonthlyListeningTime.slice(start, end + 1);

    renderMonthlyListeningTime(filteredData);
})
