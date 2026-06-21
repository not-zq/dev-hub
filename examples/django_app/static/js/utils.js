
Chart.defaults.font.family = '"Google Sans", sans-serif';
Chart.defaults.color = "#e8eaed";

/* value-normalized color interpolation per bar */

const lowColor  = [109, 169, 242];
const highColor = [227,  77,  77];

function interpolateColor(value, max) {
    const t = value / max;

    const r = Math.round(lowColor[0] + (highColor[0] - lowColor[0]) * t);
    const g = Math.round(lowColor[1] + (highColor[1] - lowColor[1]) * t);
    const b = Math.round(lowColor[2] + (highColor[2] - lowColor[2]) * t);

    return `rgb(${r}, ${g}, ${b})`;
}

/* Bar Chart Plugin | Column Value Label */

const valueLabelPlugin = {
    id: "valueLabelPlugin",
    afterDatasetDraw(chart) {
        const { ctx } = chart;

        ctx.save();
        ctx.font = "12px Google Sans";
        ctx.fillStyle = "#e8eaed";

        chart.data.datasets.forEach((dataset, i) => {
            const meta = chart.getDatasetMeta(i);

            meta.data.forEach((bar, index) => {
                const value = dataset.data[index];

                ctx.fillText(
                    value, bar.x + 6, bar.y + 4
                );
            });
        });
        ctx.restore();
    }
};

// 


