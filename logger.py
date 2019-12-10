# This is essentially a useful logger that adds additional
#   information about each output
import consts
import datetime

out_file = open(consts.OUT_FILE_PATH, 'w')

def log(output):
    # log the output string to both the console and to file
    final_string = datetime.datetime.now().strftime('%b-%d-%G %I:%M%p\n')
    final_string += output
    print(final_string)
    out_file.write(final_string)
