import re # regex!

files = [open("Wheel S33 Compendium.html", "r"), open("Wheel S34 Compendium.html", "r"), open("Wheel S35 Compendium.html", "r"), open("Wheel S36 Compendium.html", "r"), open("Wheel S37 Compendium.html", "r"), open("Wheel S38 Compendium.html", "r"), open("Wheel S39 Compendium.html", "r"), open("Wheel S40 Compendium.html", "r"), open("Wheel S41 Compendium.html", "r"), open("Wheel S42 Compendium.html", "r")]

fout = open("wheeldata.csv", "w")
fout.write("Puzzle,Category,Date\n")

for f in files:
    table = f.readlines()[637:] # line 637 is where all of the tables of puzzles begin, because the HTML files are similar

    for i in range(0,len(table)-7,7):
        entry = table[i:i+7]
        if entry[5].strip() == '<td align=\"center\">BR</td>': #this entry in the table is what type of puzzle this is 
            puzzle = re.sub("<td align=\"center\">", "", entry[1])[:-6]       # why [:-6]? we want to get rid of the </td>\n tag
            category = re.sub("<td align=\"center\">", "", entry[2])[:-6]
            date = re.sub("<td align=\"center\">", "", entry[3])[:-6]

            if puzzle and category and date:
                fout.write(puzzle + "," + category + "," + date + "\n")

    f.close()

fout.close()