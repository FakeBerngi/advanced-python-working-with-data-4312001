# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r", encoding="utf-8") as datafile:
    data = json.load(datafile)

#MY solution
# 1: How many quakes are there in total?
total_quakes = len(data["features"])
print(f"Total quakes: {total_quakes}")

# 2: How many quakes were felt by at least 100 people?
quakes_felt_by_100 = [quake for quake in data["features"] if quake["properties"].get("felt", 0) >= 100]
print(f"Total quakes felt by at least 100 people: {len(quakes_felt_by_100)}")

# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
most_felt_quake = max(data["features"], key=lambda quake: quake["properties"].get("felt", 0))
most_felt_place = most_felt_quake["properties"]["title"]
most_felt_reports = most_felt_quake["properties"]["felt"]
print(f"Most felt reports: {most_felt_place}, reports: {most_felt_reports}")

# 4: Print the top 10 most significant events
top_significant_events = sorted(data["features"], key=lambda quake: quake["properties"].get("sig", 0), reverse=True)
print("The 10 most significant events were:")
for quake in top_significant_events[:10]:
    title = quake["properties"]["title"]
    significance = quake["properties"]["sig"]
    print(f"Event: {title}, Significance: {significance}")

#Professional solution analysis
# 1: We can just use the provided data, or we can use len() to get the length of the "features"
print(f"Total quakes: {data['metadata']['count']}")


# 2: This is a straightforward filtering process
def feltreport(q):
    f = q["properties"]["felt"]
    return (f is not None and f >= 100)


feltreports = list(filter(feltreport, data["features"]))
print(f"Total quakes felt by at least 100 people: {len(feltreports)}")


# 3: We can use the max function here to find the maximum # of felt reports
def getfelt(q):
    f = q["properties"]["felt"]
    if f is not None:
        return f
    return 0


mostfeltquake = max(data["features"], key=getfelt)
print(
    f"Most felt reports: {mostfeltquake['properties']['title']}, reports: {mostfeltquake['properties']['felt']}")


# 4: This is a sorting operation
def getsig(q):
    s = q["properties"]["sig"]
    if s is not None:
        return s
    return 0


sigevents = sorted(data["features"], key=getsig, reverse=True)
print("The 10 most significant events were:")
for i in range(0, 10):
    print(
        f"Event: {sigevents[i]['properties']['title']}, Significance: {sigevents[i]['properties']['sig']}")
