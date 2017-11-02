# Getting Your Assignments Back to the Instructor

## Open GitHub Desktop and Hide the Secret PyCharm files

When GitHub Desktop opens, pull down the Repository menu and select the "Repository Settings..." option.

It will show you the Remote repository.  

<img src="pix/repos settings first.png" >

Click on the "Ignored Files" tab.  At the bottom, add `**/.idea` and save.

<img src="pix/ignore idea files.png" />

This tells Git - every Git program you've got - to ignore those directories and any underlying files.

## Post back to GitHub

If you have had your GitHub desktop open, you may have noticed "changed file" listings changing as you work.  This is completely fine.  Look them over.  Git has collected all the changes in your python scripts, the log file and Jupyter `.ipynb` notebooks.

Look these over if you like.  If some look wrong, uncheck them at the left.  You should keep the `.gitignore` file.

Actual changes show up at the right, in a "diff" format.

<img src="pix/changes to gitignore.png" />

Here, of course, you're seeing the changes to my instructions!

At lower left, click into the Summary and enter that you have completed Lab 2 part A.  You can put any comments you want in the description.  Then hit the "commit" button at the bottom.  It won't let you commit until you enter at least the summary.




