# txt-parser-date
Parses txt-files for dates and logs their contents in a json-file for easy access

## txt-parser

### Description

Opens `text.txt` file, splits it along `\n` and removes all empty list items.
Then parses for date and time formats. Saves the date inta **dictionary** which then itself becomes a dictionary further containing the **time**, whose value is the text coming *after* said time

For the time to be inserted into a date's dictionary, the previous 100 lines are checked for a date format. If no such format is found or an **IndexError** occurs, the while-loop is exited and an error message is written into the console

<!-- tbd -->