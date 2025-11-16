import pandas as pd;

data={
    "calories": [420,380,390],
    "duration":[50,40,45]
}

# Used the named index (e.g day1, doy2, etc) in the 'loc' attribute to return the specified row(s).
# The NUMBER of indexes (day1, day2, day3) should be EQUAL to the NUMBER of 'data.calories' should be EQUAL to NUMBER of'data.duration' i.e. THREE in this example
myDataFrame = pd.DataFrame(data,index=["day1","day2","day3"]);
day2 = myDataFrame.loc["day2"];
print("day 2: ");
print(day2)