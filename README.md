# json-based-database[This project is no longer maintained]

## A simple json-based-database

### How to use it?


Create a  file : `main.dob`

    main.dob
<hr>

    create~
    admin~
    var~x=10
    print_var~x
    add~(5)
    delete~2

Create a database

    create~

Add somthing to the database

    add~(add)

Delete (specify the number)

    delete~1

Open up the admin panel
The admin panel opens up at localhost:5000

    admin~


#### Admin urls
add 

    /add/thing_to_add

delete

    /delete/id_of_thing_to_delete


### Connectors

Available for

 - JavaScript(`jsdob`)
 - Python(`pydob`)
