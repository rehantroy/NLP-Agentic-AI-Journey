marks = {
    "Shubham": 100,
    "Rehant": 98,
    "Rohan": 78

}

print(marks)
print(marks["Rehant"])

print(marks.values())
print(marks.keys())

marks.update({"Rehant": 100, "Ravi":98})
print(marks)

print(marks.get("Rehant")) # Print non is key is not available in dict

print(marks["Rehant"]) # reurnt error if not available 