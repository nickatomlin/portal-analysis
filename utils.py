from dateutil import parser # For parsing times in the transcripts

def time_to_seconds(time_str):
    # Parse the time string
    dt = parser.parse(time_str)

    # Calculate total seconds
    total_seconds = dt.hour * 3600 + dt.minute * 60 + dt.second + dt.microsecond / 1e6

    return total_seconds