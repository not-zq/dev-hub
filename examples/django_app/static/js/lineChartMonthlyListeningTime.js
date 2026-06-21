
let chartDailyListeningTime;

function renderDailyListeningTime() {

    const data = JSON.parse(document.getElementById("dataMonthlyListeningTime").textContent);
    // const labels = data.map(x => x.month);
    const labels = data.map(x => 
        new Date(x.month).toLocaleDateString("en-US", {
            month: "short", year: "2-digit"
        })
    );
    const values = data.map(x => x.total_hrs);
    
    const canvas = document.getElementById("canvasMonthlyListeningTime");
    const ctx = canvas.getContext("2d");
    
    const max = Math.max(...values);

    chartDailyListeningTime = new Chart(ctx, {
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
                    title: { display: true, text: "Listening time [hrs]" },
                    grid:  { display: false } 
                }
            },
            plugins: {
                title:   { display: true, text: "Monthly Listening Time" },
                legend:  { display: false } ,
                tooltip: { enabled: false }
            },
            responsive: true,
            maintainAspectRatio: false
        }
    });

}

renderDailyListeningTime();
