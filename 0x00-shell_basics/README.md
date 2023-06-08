script 0-current_working_directory :  print the absolute path of the current directory
script 1-listit :  display list of your current directory
script 2-bring_me_home : changes the working directory to user's home directory
script  3-listfiles  : display current directory in a long foramt
script 4-listmorefiles: display current directory contents , including hidden files in long format
script 5-listfilesdigitonly : ls dir contents ,hidden files  with long format , user a group with numerical
script 6-firstdirectory : creates directory my_first_directory in /tmp/
script 7-movethatfile : Move the file betty from /tmp/ to /tmp/my_first_directory
script 8-firstdelete : delete /tmp/my_first_directory/betty
script 9-firstdirdeletion: Delete the directory my_first_directory that is in the /tmp directory
script 10-back : changes the working directory to the previous one
script 11-lists : lists all files  in the current directory and the parent of the working directory and the /boot directory (in this order)
script 12-file_type : Write a script that prints the type of the file named iamafile
script 13-symbolic_link : Create a symbolic link to /bin/ls, named __ls__
script 14-copy_html : Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory
script 100-lets_move : Create a script that moves all files beginning with an uppercase letter to the directory /tmp/u
script 101-clean_emacs :Create a script that deletes all files in the current working directory that end with the character ~
script 102-tree : creates the directories  welcome/to/school in the current directory
script 103-commas : Write a command that lists all the files and directories of the current directory, separated by commas (,).

Directory names should end with a slash (/)
Files and directories starting with a dot (.) should be listed
The listing should be alpha ordered, except for the directories . and .. which should be listed at the very beginning
Only digits and letters are used to sort; Digits should come first
You can assume that all the files we will test with will have at least one letter or one digit
The listing should end with a new line

