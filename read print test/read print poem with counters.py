name_of_mydocument = 'tuesdayafternoon.txt'
file_input = open(name_of_mydocument, 'r')     #open file for reading

total_lines_in_file = 1
                                    #read the first few lines
line = file_input.readline()
firstline = line
total_lines_in_file = total_lines_in_file + 1

line = file_input.readline()
print(" " + firstline, line)
total_lines_in_file = total_lines_in_file + 1

line = file_input.readline()
line = file_input.readline()

stanza_counter = 1
song_line_counter = 0

while line != '':                  # while not a blank line

  if line == "\n":
    stanza_counter = stanza_counter + 1
    total_lines_in_file = total_lines_in_file + 1
    print()
    line = file_input.readline()

  else:
    total_lines_in_file = total_lines_in_file + 1               
    song_line_counter = song_line_counter + 1

    if song_line_counter < 10:
      print(str(song_line_counter)+ ')   ', line, end = '')
    else:

      print(str(song_line_counter) + ')  ', line, end = '')

    line = file_input.readline()

line = file_input.readline()

print ("\n-- End of Song ---")

print("\nTotal number of lines in the song are: " + str(song_line_counter) + ".")
print ("Total number of stanzas in this song are: " + str(stanza_counter) + ".")
print("Total number of lines in this file is " + str(total_lines_in_file) +".")
print("The song \"Tuesday Afternoon\" first appeared on the album \033[3mDays of Future Passed\033[0m in 1967.")
print ("This song first appeared in the album 'Days of Future Passed' in 1968.")
print ("The Moody Blues members are Mike Lodge, Graeme Edge, Justin Hayward, Ray Thomas, and John Lodge.")
