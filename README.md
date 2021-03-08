# How to set up?
> Make sure you have python version 3 installed 
1. Unzip 'family-search-scrapper.zip' 
2. Open terminal in the unzipped folder
3. Enter the following commands one by one

    3.1 `pip install -r requirements.txt`

    3.2 python run.py --row=<NO_OF_ROWS_IN_INPUT_CSV>

        > You will be prompted to enter account details and collection id. 

        > For 'United Kingdom, World War I Service Records, 1914-1920' the collection id is 2125045
4. Sit back and wait until this is finished
5. Output will be at out/ directory

# For next run
> This time you don't have to setup just run any commands from the table 'Available Commands'

> For any help enter `python run.py --help' in project directory

Available commands:

1. python run.py --row=<NUMBER_OF_ROWS>
> Fetch <NUMBER_OF_ROWS> rows from input CSV

> Hidden parameters  --clear --merge  --match=exact

2. python run.py --clear
> Clear history and cache

3. python run.py --merge 
> Merge partially downloaded files 

4. python run.py --resume
> Resume scraping since last run

5. python run.py --row=<NUMBER_OF_ROWS> --match=approximate
> Perform an approximate search. This may fetch humongous amount of data. 

6. python run.py --set-secret
> Set account credentials and collection id   

7. python run.py --status
> Log current fetch status and account details  

8. python run.py --help
> List all parameters and examples    

