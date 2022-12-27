import re
from tabulate import tabulate

groups = [["QAT","SEN","ECU","NED"],
["ENG","IRN","USA","WAL"],
["ARG","KSA","MEX","POL"],
["FRA","AUS","DEN","TUN"],
["ESP","CRC","GER","JPN"],
["BEL","CAN","MAR","CRO"],
["BRA","SRB","SWI","CMR"],
["POR","GHA","KOR","URU"]]

def main():

    print()

    print("Welcome to World Cup 2022 Group Stage Simulator!")

    print()
    print("This simulator requires the predicted conclusion of the match which could be a win,\
loss or draw.")


    print()
    for i in range(len(groups)):
        print(f"Group {chr(65+i)}: {', '.join(groups[i])}")

    while True:
        print()
        group = input("Which group would you like to select: ")

        try:
            group = check_textin(group, r"^([ABCDEFGH])$")[0]

        except ValueError:
            print("Sorry, you did not enter the answer in the specific format. Please re-enter.")

        else:
            break

    group_data = get_groupdata(group)
    rank, sorted_group_data = rankingpts(group_data)

    rank = handle_drawrank(sorted_group_data,rank)

    out = tabulate(rank,headers=["Ranking","Country"],tablefmt="fancy_grid")
    print(out)




def check_textin(textin, checker):
    textin = textin.strip().upper()
    if matches := re.search(checker,textin):
        out = matches.groups()
        return out

    raise ValueError




def get_groupdata(group):
    game = []
    group_data = {}

    global groups
    group = ord(group.upper())-65

    n = len(groups[group])

    for i in range(int(((n*n)-n)/2)):

        if len(game) == 0:
            print("No matches entered yet")
            print()
        else:
            print("Matches Entered: \n")
            for i in game:
                print(" - ".join(i))
                print()

        while True:
            x = input("Enter the match in the format XXX - XXX: ")
            print()
            try:
                x = check_textin(x,r"^(\w{3}) ?- ?(\w{3})$")
            except ValueError:
                print("Sorry, you did not enter the answer in the specific format. Please re-enter.")
                print()
            else:

                if x[0] in groups[group] and x[1] in groups[group]:
                    if x[0] != x[1]:
                        if x not in game and x[::-1] not in game:
                            game.append(x)
                            break
                        else:
                            print("You have already entered input for this match. Please re-enter.")
                            print()

                    else:
                        print("The countries you have entered are the same. Please re-enter.")
                        print()

                else:
                    print("The countries you have entered are not in this group. Please re-enter.")
                    print()

        if len(group_data.keys()) == 0:
            group_data[x[0]] = {"pts":0,"gs":0,"gc":0}
            group_data[x[1]] = {"pts":0,"gs":0,"gc":0}

        else:
            for i in range(2):
                if x[i] not in group_data:
                    group_data[x[i]] = {"pts":0,"gs":0,"gc":0}

        group_data = get_matchdata(x,group_data)

    return group_data




def get_matchdata(x,group_data):

    while True:
        score = input("Enter score for match entered in the format W-L for a winner and D-D for a draw: ")
        print()
        try:
            score = check_textin(score,r"^([WDL]+) ?- ?([WDL]+)$")
        except ValueError:
            print("Sorry, you did not enter the answer in the specific format. Please re-enter.")
            print()

        else:
            if score == ("D","D") or score == ("W","L") or score[::-1] == ("W","L"):
                break

    for i in range(len(score)):
        if score[i] == "W":
            group_data[x[i]]["pts"] += 3

        elif score[i] == "D":
            group_data[x[i]]["pts"] += 1

    return group_data





def rankingpts(group_data):
    rank = []
    sorted_group_data = sorted(group_data.items(),key=lambda x:x[1]["pts"],reverse=True)

    for i in range(len(sorted_group_data)):
        rank.append([i+1,sorted_group_data[i][0]])

    return rank, sorted_group_data




def handle_drawrank(sorted_group_data,rank):
    pts = []
    done = []
    dupe = []

    for i in sorted_group_data:
        pts.append(i[1]["pts"])

    for i in range(len(pts)):
        if pts.count(pts[i]) > 1 and pts[i] not in done:
            dupe.append({"start":i, "end": i+pts.count(pts[i])})
            done.append(pts[i])

    count = 0
    while count != len(dupe):
        ind = rank[dupe[count]["start"]][0]
        for i in range(dupe[count]["start"],dupe[count]["end"]):
            rank[i][0] = ind

        count += 1

    return rank



if __name__ == "__main__":
    main()