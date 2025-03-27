document.addEventListener("DOMContentLoaded", () => {
    function updateTrafficData() {
        fetch("/traffic_data")
            .then(response => response.json())
            .then(data => {
                document.getElementById("lane1-count").innerText = data.lane_1_count;
                document.getElementById("lane2-count").innerText = data.lane_2_count;
                document.getElementById("signal-status").textContent = data.signal_status;

                const lane1Signal = document.getElementById("lane1-signal");
                const lane2Signal = document.getElementById("lane2-signal");
                const recommendation = document.getElementById("recommendation-text");

                if (data.signal_status.includes("Lane 1: Green")) {
                    lane1Signal.innerText = "🟢 Green";
                    lane1Signal.className = "signal light-green";

                    lane2Signal.innerText = "🔴 Red";
                    lane2Signal.className = "signal light-red";

                    recommendation.innerText = "Lane 1 is open, redirecting cars to balance traffic.";
                } else {
                    lane1Signal.innerText = "🔴 Red";
                    lane1Signal.className = "signal light-red";

                    lane2Signal.innerText = "🟢 Green";
                    lane2Signal.className = "signal light-green";

                    recommendation.innerText = "Lane 2 is open, redirecting cars to balance traffic.";
                }
            })
            .catch(error => {
                console.error("Error fetching traffic data:", error);
            });
    }

    // Update traffic data every 3 seconds
    setInterval(updateTrafficData, 3000);
});
