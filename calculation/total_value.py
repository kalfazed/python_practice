# what is the salary of this month :)

import re
import sys
import string

salary_per_hour = 1600
salary_per_hour_over = salary_per_hour * 1.25

working_time = string.atof(sys.argv[1]);
additional_time = string.atof(sys.argv[2]);

regular_time = working_time - additional_time;

salary_I_got = regular_time * salary_per_hour + additional_time * salary_per_hour_over

print "My salary is %10d" % salary_I_got
