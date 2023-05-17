import re
from settings import mysql_connection

#select ticket and ids
def select_movie(movie_id, no_of_tickets):
    mydb=mysql_connection()
    sql=mydb.cursor()
    ##take movie id and no of tickets as inputs
    
    ## only 5 tickets for a person condition validation
    if no_of_tickets>5:
        return "you can't book more than 5 tickets"
    ##select movie_id and avaibility from the database
    
    query=(f"select movie_id,availability,movie_name from movies where movie_id='{movie_id}'")
    sql.execute(query)
    res=sql.fetchall()
    available=0
    ##validate if a particular movie id is available
    if res:
        for row in res:
            ## Display how many tickets available
            print(f"{row[1]} tickets available for movie {row[2]}")
            if int(row[1])<0:
                return False
            available=int(row[1])
        sql.close()
    
        update_ticket=int(available-no_of_tickets)
        
         #update the tickets dynamically into database (Change the type to int) (tickets available - ticket booked)
        
        sql=mydb.cursor()
        
        ## this is to maintain realistic records
    
        ## write update query, change from int to string record where movie_id = 'value'
    
        sql.execute(f"update movies set availability='{update_ticket}' where movie_id='{movie_id}'")
        mydb.commit()
        sql.close()
        #return True when success
        return True

    ## assume that payment gateway has processed (at the counter)
    
    
    #default return should be False
    return False

    ##challenge since the ticket count is in varchar format in table, you have to dynamically convert type and validate


#do not delete following function
def task_runner():
    print(select_movie(1001, 2))
    
task_runner()