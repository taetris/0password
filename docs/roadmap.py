""" 
    Notes:
    -flask --app frontend run
    
    
    - at this point, kinda unsure what to do: we're following 2 tangents here: building an extension and an actually app
    - and both seem to be logically distinct from each other for this reason, will take this at hault here
----------------TO DO----------------------------
    - connect input to ui
    
    - first generate should also copy to clipboard
    - can use API ninjas
    - if entry already exists, then should not overwrite, should not have duplicates
    - flask
    - autofiller
    - try-catch here in all blocks and if one failed then all reverted, ofcourse returning from all these functions
    - putting other functions in another file
    - where to really store
    - alternatives to master password: Zero knowledge authentication
    - storing backups SAFELY
    - How to make an extension and work in background
    ----------------DONE------------------------------
    - 
    - still to be compleletly solved: the salt-creds storing part isnt actually atomic: this was due to already present redundancies in the database. due to which push to creds was allowed but not to noon
    - Store and retrieve salts in a separate database
    - How to interface with applications : clipboard
    ----------------CAN BE DONE------------------------------
    - having to whitelist your IP every single time
    - how to handle duplicate entries
    - agile and scrum
    - AWS Lambda and MongoDB
    - JSON webtokens 
    - Github actions for release build for CI/CD
    ----------------IDEAS REJECTED---------------------------
    - MongoDB not very compatible with Django (mostly supports tabular databases)
    - small project, so flask chosen
    """