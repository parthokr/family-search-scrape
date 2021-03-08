class Help:
    def __init__(self):
        pass
    
    def help(self):
            help_text = """
            -> Main command: python run.py

                                            Available parameters
            |---------------------------------------------------|----------------------------------------------------|
            |       Parameters    |     Required |     Optional |     Description                                    |
            |---------------------|--------------|--------------|----------------------------------------------------|
            |--row=<ROW_COUNT>    |       YES    |       NO     |Fetch in range. Start row = 1 end row = <ROW_COUNT> |
            |---------------------|--------------|--------------|----------------------------------------------------|
            |--match=approximate  |       YES    |       NO     |Perform an approximate search                       |
            |---------------------|--------------|--------------|----------------------------------------------------|
            |--match=exact        |       YES    |       NO     |Perform an exact search (default)                            |
            |---------------------|--------------|--------------|----------------------------------------------------|
            |--resume             |       NO     |       YES    |Resume from previous session                        |
            |---------------------|--------------|--------------|----------------------------------------------------|
            |--merge              |       NO     |       YES    |Merge partially downloaded XLSX                     |
            |---------------------|--------------|--------------|----------------------------------------------------|
            |--clear              |       NO     |       YES    |Remove log and history                              |
            |---------------------|--------------|--------------|----------------------------------------------------|
            |--set-secret         |       NO     |       YES    |Set account credentials and collection id           |
            |---------------------|--------------|--------------|----------------------------------------------------|
            |--status             |       NO     |       YES    |Log current fetch status and account details        |
            |---------------------|--------------|--------------|----------------------------------------------------|
            |--help               |       NO     |       YES    |List all parameters and examples                    |
            |---------------------|--------------|--------------|----------------------------------------------------|

            Example:
            python run.py --row=100
            python run.py --row=100 --match=approximate
            python run.py --row=100 --resume
            python run.py --merge
            python run.py --clear
            python run.py --status
            python run.py --set-secret

            python run.py --help

            """
            print(help_text)