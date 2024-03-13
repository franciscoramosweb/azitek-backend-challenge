import os
import requests
from datetime import datetime
import matplotlib.pyplot as plt

def process_api_request(timestamp, timestamp_end):
    api_key = os.getenv("API_KEY")

    headers = {
        "X-Api-Key": api_key
    }

    url = f"https://ivt-api.azitek.io/position_logs/187723572702721/{timestamp}?timestamp_end={timestamp_end}"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        data = response.json()


        beacon_counts = {}
        total_time_in_each_point = {}
        for entry in data:
            beacon_id = entry['beacon_id']
            if beacon_id not in beacon_counts:
                beacon_counts[beacon_id] = 0
                total_time_in_each_point[beacon_id] = 0

            beacon_counts[beacon_id] += 1

            last_seen_at = datetime.fromtimestamp(entry['last_seen_at'])
            seen_at = datetime.fromtimestamp(entry['seen_at'])

            total_time_in_each_point[beacon_id] += (last_seen_at - seen_at).total_seconds()

        avg_times = {beacon_id: total_time / beacon_counts[beacon_id] for beacon_id, total_time in total_time_in_each_point.items()}

        return beacon_counts, avg_times
    elif response.status_code == 404:
        print("Status code:", response.status_code)
        print("Não há dados para os intervalos de tempo solicitados")
        print("Start Date:", datetime.fromtimestamp(timestamp))
        print("End Date:", datetime.fromtimestamp(timestamp_end))
        return {}, {}
    else:
        print("Erro ao fazer solicitação:", response.status_code)
        return {}, {}

day1start = int(datetime(2023, 11, 17, 10, 0).timestamp()) # 10 am of 17th November 2023
day1end = int(datetime(2023, 11, 17, 17, 0).timestamp())  # 5 pm of 17th November 2023
day2start = int(datetime(2023, 11, 18, 10, 0).timestamp())  # 10 am of 18th November 2023
day2end = int(datetime(2023, 11, 18, 17, 0).timestamp())  # 5 pm of 18th November 2023

beacon_counts_1, avg_times_1 = process_api_request(int(day1start), int(day1end))
beacon_counts_2, avg_times_2 = process_api_request(int(day2start), int(day2end))

combined_beacon_counts = {}
combined_avg_times = {}

for beacon_id in set(list(beacon_counts_1.keys()) + list(beacon_counts_2.keys())):
    combined_beacon_counts[beacon_id] = beacon_counts_1.get(beacon_id, 0) + beacon_counts_2.get(beacon_id, 0)
    combined_avg_times[beacon_id] = (avg_times_1.get(beacon_id, 0) + avg_times_2.get(beacon_id, 0)) / 2

fig, ax1 = plt.subplots()

ax1.bar(combined_beacon_counts.keys(), combined_beacon_counts.values(), color='b')
ax1.set_xlabel('Beacon ID')
ax1.set_ylabel('Número de Ocorrências', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(combined_avg_times.keys(), combined_avg_times.values(), color='r')
ax2.set_ylabel('Tempo Médio (segundos)', color='r')
ax2.tick_params('y', colors='r')

for tick in ax1.get_xticklabels():
    tick.set_rotation(45)
    tick.set_ha('right')

plt.title('Número de Ocorrências de Beacons e Tempo Médio em Cada Ponto')
plt.tight_layout()

# Save the graph image to a folder
output_folder = "graphPlots"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

output_file = os.path.join(output_folder, "graph_plot.png")
plt.savefig(output_file)

plt.show()
