Cory Zou and I worked as a team and collaborated on this assignment.
His net ID is yz6350
My net ID is bw2427

## Here is all the data designed for this mission：

[the original data file](/data/DOHMH_Dog_Bite.tsv)

[the munged data file](/data/clean_data.csv)

[the spreadsheet file](/data/Data_analysis.csv)

Data is collected from reports received online, mail, fax or by phone to 311 or NYC DOHMH Animal Bite Unit. Each record represents a single dog bite incident. Information on breed, age, gender and Spayed or Neutered status have not been verified by DOHMH and is listed only as reported to DOHMH.Raw data file format: tsv
[Click here to jump to the original dataset](https://data.cityofnewyork.us/Health/DOHMH-Dog-Bite-Data/rsgh-akpg/data_preview)


Here are the first 20 rows of the source dataset：
|   UniqueID | DateOfBite      | Species   | Breed                                | Age   | Gender   | SpayNeuter   | Borough   |   ZipCode |
|-----------:|:----------------|:----------|:-------------------------------------|:------|:---------|:-------------|:----------|----------:|
|          1 | January 01 2018 | DOG       | UNKNOWN                              | nan   | U        | False        | Brooklyn  |     11220 |
|          2 | January 04 2018 | DOG       | UNKNOWN                              | nan   | U        | False        | Brooklyn  |       nan |
|          3 | January 06 2018 | DOG       | Pit Bull                             | nan   | U        | False        | Brooklyn  |     11224 |
|          4 | January 08 2018 | DOG       | Mixed/Other                          | 4     | M        | False        | Brooklyn  |     11231 |
|          5 | January 09 2018 | DOG       | Pit Bull                             | nan   | U        | False        | Brooklyn  |     11224 |
|          6 | January 03 2018 | DOG       | BASENJI                              | 4Y    | M        | False        | Brooklyn  |     11231 |
|          7 | January 01 2018 | DOG       | UNKNOWN                              | nan   | U        | False        | Brooklyn  |       nan |
|          8 | January 03 2018 | DOG       | Pit Bull                             | nan   | U        | False        | Brooklyn  |     11233 |
|          9 | January 04 2018 | DOG       | American Pit Bull Mix / Pit Bull Mix | 5Y    | M        | False        | Brooklyn  |     11235 |
|         10 | January 10 2018 | DOG       | MIXED                                | 3Y    | F        | False        | Brooklyn  |     11208 |
|         11 | January 06 2018 | DOG       | nan                                  | nan   | U        | False        | Brooklyn  |     11215 |
|         12 | January 07 2018 | DOG       | Yorkshire Terrier Crossbreed         | 7     | M        | True         | Brooklyn  |     11208 |
|         13 | January 06 2018 | DOG       | Great Dane                           | 6     | F        | True         | Brooklyn  |       nan |
|         14 | January 01 2018 | DOG       | Pit Bull                             | nan   | U        | False        | Brooklyn  |     11220 |
|         15 | January 09 2018 | DOG       | Labradoodle                          | 5     | F        | True         | Brooklyn  |     11238 |
|         16 | January 01 2018 | DOG       | West High White Terrier              | nan   | M        | False        | Brooklyn  |     11207 |
|         17 | January 14 2018 | DOG       | American Pit Bull Terrier/Pit Bull   | nan   | U        | False        | Brooklyn  |     11205 |
|         18 | January 07 2018 | DOG       | nan                                  | nan   | U        | False        | Brooklyn  |     11209 |
|         19 | January 13 2018 | DOG       | MIXED                                | 7     | M        | False        | Brooklyn  |     11237 |
|         20 | January 10 2018 | DOG       | American Pit Bull Terrier/Pit Bull   | nan   | U        | False        | Brooklyn  |     11233 |

The original dataset is a tsv file containing a large number of missing values and data in different formats, which needs to be transformed and processed. Consider the process for dealing with missing values:
### Fill in the missing age values
    ```
    if row[4] == '':
        row[4] = 'Unknown'
    ```
### Fill in the missing zip codes
    ```
    if row[8] == '':
        row[8] = 'Unknown'
    ```
### processing gender data, mainly for its data format conversion
    ```
    if row[5] == 'U':
        row[5] = 'Unknown'
    elif row[5] == 'M':
        row[5] = 'Male'
    elif row[5] == 'F':
        row[5] = 'Female'
    ```
## Analysis of data
Through the sorting of the data set, it was found that the years involved were all the dog bites from 2015 to 2021. Therefore, I mainly analyzed the data in the column of DateOfBite, used the formula in excel to sort out, and made summary statistics on the number of bites in each month of the year. (For example, for the number of bites in January 2015: =COUNTIF(clean_data! B2:clean_data! B22664,"January**2015")).
### Based on the above statistical results,
1. We sorted out the number of all bites in each year and the average number of bites in each year and made a bar chart and line chart to see the corresponding total number and changing trend. According to the statistical results, from 2015 to 2021, In 2015, 2017, 2018, and 2019, the number of bites was basically the same, maintaining around 3,500, and in 2016, it was slightly lower, around 3,200. However, in 2020 and 2021, the number of bites dropped even more, to 2,551 in 2020 and 2,931 in 2021, so it is possible that the government or related organizations have taken some measures to reduce the incidence of dog bites

![pic1](/images/pic1.png)
![pic2](/images/pic2.png)
![pic3](/images/pic3.png)


2. We sorted out the maximum number of bites, the minimum number of bites and their corresponding months in each year. According to the statistical results, June, July and August are the peak times of dog bites, and January and February are the lowest months of dog bites, which is more consistent with our daily habits.