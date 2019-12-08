<h1>GET REQUEST</h1>


<h2>url :</h2><h1>http://127.0.0.1:8000/</h1>                    //sends the url where notes are stored
{
    "note": "http://127.0.0.1:8000/note/"
}




<h3>structure of note</h3>
[
    {
        "id": ,
        "title": ,
        "description": ,
        "creation_date": ,
        "updated_on_date": ,
        "url": 
    }
}




<h2>url :</h2><h1>http://127.0.0.1:8000/note</h1>  //sends all the notes created
[
    {
        "id": 4,
        "title": "Ram",
        "description": "Ramayan book is famous",
        "creation_date": "2019-12-08T20:10:00.536289Z",
        "updated_on_date": "2019-12-08T20:10:00.536289Z",
        "url": "http://127.0.0.1:8000/note/4/"
    },
    {
        "id": 3,
        "title": "Physics",
        "description": "You can do anything if you the Science behind it.",
        "creation_date": "2019-12-08T19:58:27.965613Z",
        "updated_on_date": "2019-12-08T19:58:27.965613Z",
        "url": "http://127.0.0.1:8000/note/3/"
    },
    {
        "id": 2,
        "title": "Biology",
        "description": "Nice Subjects .",
        "creation_date": "2019-12-08T19:57:59.168590Z",
        "updated_on_date": "2019-12-08T19:57:59.168590Z",
        "url": "http://127.0.0.1:8000/note/2/"
    },
    {
        "id": 1,
        "title": "maths",
        "description": "do homework of maths.",
        "creation_date": "2019-12-08T19:57:43.945218Z",
        "updated_on_date": "2019-12-08T19:57:43.945218Z",
        "url": "http://127.0.0.1:8000/note/1/"
    }
]






<h2>url :</h2><h1>http://127.0.0.1:8000/note/1</h1>       //Can retrieve a note with it's id number
{
    "id": 1,
    "title": "maths",
    "description": "do homework of maths.",
    "creation_date": "2019-12-08T19:57:43.945218Z",
    "updated_on_date": "2019-12-08T19:57:43.945218Z",
    "url": "http://127.0.0.1:8000/note/1/"
}



<h1>POST REQUEST</h1>

<h2>url :</h2><h1>http://127.0.0.1:8000/note/</h1>   //Creation of new note
{
    "title": [
        "This field is required."
    ],
    "description": [
        "This field is required."
    ]
}



<h1>PUT REQUEST</h1>
<h2>url :</h2><h1>http://127.0.0.1:8000/note/1/</h1>         //POST UPDATION Using it's id number
{
    "title": [
        "This field is required."
    ],
    "description": [
        "This field is required."
    ]
}

<h1>DELETE REQUEST</h1>
<h2>url :</h2><h1>http://127.0.0.1:8000/note/3/</h1>        //Dekete by id number


