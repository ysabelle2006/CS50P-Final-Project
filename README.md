## Project Title: World Cup 2022 Group Stage Simulator

### Video Demonstration: [Video Link](https://youtu.be/tIOcmfAcc_8)

### Project Description:

This project was created for the World Cup 2022 season. In the World Cup group stage, countries are split into groups of 4, with a total of 8 groups. In their groups, each country's football team will play a match against all other countries in their group with no extra time nor penalty shoot-out. For every match a country wins, they will earn 3 points while the country that lost will not receive any points for that match. If the match ends in a draw, both countries will earn 1 point each. After all matches are played, the 2 countries with the most points will move on to the knockout stage.

As these rules may be quite complex to calculate, given the number of matches and countries involved, this project was created to give a simple ranking of the countries in a group at the end of all matches. Users can enter which group they would like to simulate, from Group A to H, with information of the countries in the groups given. The user would then be prompted for the match between which 2 countries and the final conclusion of the match which can be a win, loss or draw. The program will calculate the points given to each country in the group based on the matches played and rank them accordingly, with the country with the most points earned as Rank 1.

As this is meant to be a simple ranking which only takes into consideration the conclusion of each match and not the specific scores, the ranking will not consider goal difference and goals for. Hence, when there is a draw in points between 2 countries, they will be given the same ranking. For example, in Group C of the World Cup 2022 group stage, both Mexico and Poland earned 4 points each where they would be second in terms of points. This program will rank them as both in second place. However, in the World Cup, their goal difference and goals for which is based on the specific score in each match will be used to break the tie.



### File Description


#### `project.py` file

In this file, there are 6 functions, including the `main()` function. 

The functions are:

- `main()`
- `check_textin()`
- `get_groupdata()`
- `get_matchdata()`
- `rankingpts()`
- `handle_drawrank()`

The global variable `groups` is a list containing lists of countries in a group with the list of countries in Group A at index 0. It is defined at the start of the file. The libraries `re` and  `tabulate` are also imported and used in this file.


##### `main()` function

In the `main()` function, the program will print an introduction to the simulator as well as the information needed to use the simulator. It will also print the different groups of countries participating. It would then prompt the user to choose which group they would like to simulate with error-checking using the `check_textin()` function. The `main()` function would then call the `get_groupdata()` function, the `rankingpts()` function and the `handle_drawrank()` function before printing the ranking table using the library `tabulate`.


##### `check_texin()` function

The `check_textin()` function takes in user input as a string and a regular expression as parameters. The function will strip the empty space before and after the string and set all its letters to uppercase. It will then match the string against the regular expression. If they match, the function will return the values of the string that are supposed to be returned which are indicated in the regular expression as.a tuple. If they do not match, the function will raise a `ValueError`. This function us used to do a basic check for user inputs in the `main()`, `get_groupdata()` and `get_matchdata()` functions.


##### `get_groupdata()` function

The `get_groupdata()` function takes in a string which is one of the characters A, B, C, D, E, F, G, H in uppercase to identify the group which the user has chosen. The parameter is known as `group`. The argument `group` passed in is then converted to its ASCII code and subtracted by 65 to find the index of the list of countries in that group in the global variable `groups`. The number of matches played within that group is calculated using the formula ((n * n) - n) / 2, where n is the number of countries in the group. For each match, the user will input the country code of the countries playing in the format XXX - XXX. The function will validate that the input is in the correct format, the countries entered are not the same, the countries are from the correct group and that the match has not been entered before. After validation is complete, it will create a tuple which contains the country codes of the countries playing in the match which is known as the variable `x`. If the country has not been entered before, a new dictionary of dictionaries will be initialised in the variable `group_data`. The key to the outer dictionary is the country code while the inner dictionary has 3 key-value pairs of `pts` which refers to the points scored, `gc` which refers to goals conceded and `gs` which refers to goals scored. The value of the 3 keys are initialised to be 0. For each match, the function will call the the `get_matchdata()` function. After all the matches have been entered, it will return the `group_data` variable.


##### `get_matchdata()` function

The `get_matchdata()` function takes in the tuple known as `x` and the dictionary of dictionaries known as `group_data` from the `get_groupdata()` function. For each match, after the `get_groupdata()` function has prompted the user which match will be simulated currently, the `get_matchdata()` function will prompt the user for the results of the match in the format W - L or L - W for a clear win or loss and D - D for a draw which should be corresponding to the order of countries entered in the `get_groupdata()` function. For each country in that match entered, it will check if it is a "W", "L" or "D" where it would add 3, 0 and 1 point respectively to the `group_data` variable where the key to the outer dictionary is the country code and the key to the inner dictionary is `pts` so the value of the key `pts` would change from its initialised value of 0. It would then return the `group_data` variable to the `get_groupdata()` function.


##### `rankingpts()` function

The `rankingpts()` function takes in `group_data` which is a dictionary of dictionaries which is the return value of `get_matchdata()` function. It passes the return value of `items()` of `group_data` which is a list of tuples, where each tuple contains a key-value pair, into the `sorted()` function as an argument with the `key` parameter being an anonymous function which for each tuple in the list of tuples, returns value of the key `pts` in the dictionary which is at index 1 for each tuple. The `reverse` parameter in the `sorted()` function set as `True`. The result is a list of tuples which are arranged with the country with the highest points at index 0 which is known as `sorted_group_data`. The rank number and the country is then extracted from `sorted_group_data` into the list `rank` where the rank number is at index 0 and the country code at index 1. The function then returns the list `rank` and the list of tuples `sorted_group_data`.


##### `handle_drawrank()` function

The `handle_drawrank()` function takes in `sorted_group_data` and `rank` which are the return values of the `rankingpts` function. From `sorted_group_data`, the points from each country are extracted and appended to a list known as `pts`. If there are countries with the same number of points, the function will append to the empty list `dupe` a dictionary with the first key `start` and the value being the first index in `pts` which the duplicated points first appeared and the second key `end` with the value being the sum of the value of the first key and the number of times the duplicated point appeared in `pts`. The function will then change the ranking of countries in `rank` based on the `start` and `end` key-value pairs in `dupe` such that if countries have the same number of points they will be ranked the same. The `handle_drawrank()` function will then return the list `rank` to the `main()` function.



#### `test_project.py` file

The `test_project.py` file contains tests for the functions `check_textin()`, `rankingpts()` and `handle_drawrank()` in `project.py`. The file imports the `pytest` library and the respective functions from `project.py`.


##### `test_check_textin()` function

The `test_check_textin()` function is used to test the `check_textin()` function. It tests different values for the different uses of `check_textin()` function. They include tests to check the use of the `check_textin()` function to verify the user input for the group names, match names and scores as well as tests that check for the presence of a `ValueError` if the user input does not match the regular expression for the different uses.


##### `test_rankingpts()` function

The `test_rankingpts()` function is used to test to `rankingpts()` function. It tests different situations of user input that the `rankingpts()` function will face. These situations are if there is a draw in points among a few countries and if there is no draw.


##### `test_handle_drawrank()` function

The `test_handle_drawrank()` function is used to test to `handle_drawrank()` function. It tests different situations of user input that the `handle_drawrank()` function will face. These situations are if there is a draw in points among a few countries, if there is no draw and if all the countries in the group have a draw in points.



#### `requirements.txt` file

This file contains the list of libraries that were imported and used in the `project.py` and `test_project.py` files.
