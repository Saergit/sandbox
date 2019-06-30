# Wolt Backend Assignment
# Petteri Heinonen 2019
from flask import Flask, request
import csv, statistics, datetime, json

app = Flask(__name__)

# Convert csv into list
pickups_file = open('pickup_times.csv')
pickups_data = list(csv.reader(pickups_file, delimiter=','))

# Remove indexing from list
pickups_data.pop(0)

@app.route('/')
def index():
    text = 'Wolt backend assignment. <br> ©Petteri Heinonen 2019'
    return text


@app.route('/median_pickup_time/', methods=['GET'])
def median_pickup_time():

    median = 0
    loc_id = request.args.get('location_id')
    start  = request.args.get('start_time')
    end    = request.args.get('end_time')

    # Convert dates into datetime objects for comparison later
    input_stringtype = "%Y-%m-%dT%H:%M:%S"
    date_start = datetime.datetime.strptime(start, input_stringtype)
    date_end   = datetime.datetime.strptime(end, input_stringtype)
    times = list()

    for location in pickups_data:

        # Remove Zulu information since it's unsupported by python
        loc_date = str(location[1]).replace('Z', '')
        date_loc_start = datetime.datetime.strptime(loc_date, input_stringtype)
        if (location[0] == loc_id and date_start < date_loc_start and date_loc_start < date_end):

            # Append pickup time to list
            times.append(location[2])

    # Calculate median from the list of valid pickup times
    median = {
        'median': statistics.median(times)
    }

    # Return data as json
    return json.dumps(median)

if __name__ == '__main__':
    app.run(debug=True)