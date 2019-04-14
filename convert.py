def convert_to_minutes(num_hours):
    minutes = num_hours * 60
    return minutes

def convert_to_seconds(num_hours):
    minutes = convert_to_minutes(num_hours)
    seconds = minutes * 60
    return seconds

seconds = convert_to_seconds(2)
