
monthConversions = {
    "Jan": "January",
    "Feb": "Febuary",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions.get("Dec"))
print(monthConversions.get("Mar"))
print(monthConversions.get("Lay", "Not a value"))

monthConversions.update({"Big": "Fatty"})
print(monthConversions)

b = {"hot": "Summer", "cold": "winter"}
monthConversions.update(b)
print(monthConversions)

monthConversions.pop("Jan")
print(monthConversions)